import tensorflow as tf
from tensorflow import keras
from keras.callbacks import EarlyStopping
from constants import LAYERS, PRUNING_PERCENTAGES, OPTIMIZER_FC
from tqdm import tqdm
import numpy as np

class FC_NETWORK:
    def __init__(self, batch_size=60, use_earlyStopping=False, loaded_model=None):
        """
            Lenet-300-100 (Lenet-5) Architecture replica, 
            to use on both MNIST and Fashion MNIST
        """
        self.batch_size = batch_size
        self.pruning_rates = PRUNING_PERCENTAGES
        self.early_stopping = use_earlyStopping

        if loaded_model == None:
            self.model = keras.Sequential()
            self.model.add(keras.layers.Flatten(input_shape=(28, 28)))
            for layer in LAYERS:
                (units, activation) = LAYERS[layer]
                self.model.add(keras.layers.Dense(units, activation=activation))
        
        
            self.model.compile(optimizer=OPTIMIZER_FC,
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])
        else:
            self.model = loaded_model

        if use_earlyStopping:
            self.es = EarlyStopping(monitor='val_loss', patience=10)
    
    def fit(self, data, labels, n_epochs=10):
        self.model.fit(x=data, y=labels, batch_size=self.batch_size, 
        validation_split=0.1 if self.early_stopping else None, epochs=n_epochs,
        callbacks=[self.es] if self.early_stopping else None)

    def shuffle_in_unison(self, x_train, y_train,split=0.1):
        n = np.size(x_train,axis=0)
        p = np.random.permutation(len(x_train))
        cutoff = int(split*n)
        p_val = p[0:cutoff]
        p_train = p[cutoff:]
        return x_train[p_train], y_train[p_train], x_train[p_val], y_train[p_val]

    def mask_weights(self,mask,weights_init):  
        new_weights = list()
        for idx, layer in enumerate(self.model.layers):
            if len(layer.get_weights())>0:
                new_weights.append(weights_init[idx]*mask[idx])
                new_weights.append(layer.get_weights()[1])
            else:
                continue
        return new_weights

    def fit_batch(self,data,labels,mask,weights_init,epochs=10):
        n = np.size(data,axis=0)
        n_batch = self.batch_size
        for e in range(0, epochs):
            x_train, y_train,x_val,y_val = self.shuffle_in_unison(data,labels)
            self.evaluate_model(x_val,y_val)

            print("Epoch " + str(e+1) + "/" + str(epochs))
            for j in tqdm(range(int(n / n_batch))):
                new_weights = self.mask_weights(mask, weights_init)
                self.model.set_weights(new_weights)
                j_start = j*n_batch
                j_end = (j+1)*n_batch
                Xbatch = x_train[j_start:j_end,:,:]
                Ybatch = y_train[j_start:j_end]
                self.model.train_on_batch(Xbatch,Ybatch)
        new_weights = self.mask_weights(mask, weights_init)
        self.model.set_weights(new_weights)

    def evaluate_model(self, test_data, test_labels):
        test_loss, test_acc = self.model.evaluate(test_data, test_labels, verbose=2)
        return test_loss, test_acc
    
    def save_model(self, filename):
        self.model.save('models/' + str(filename))

    def get_summary(self):
        return self.model.summary()