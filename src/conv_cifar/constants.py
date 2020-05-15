import tensorflow as tf
from tensorflow import keras

"""
    Hyperparameters, data and constants for the convolutional networks (Conv-2, Conv-4)
"""

SETTINGS_CONV2 = {
    'n_epochs' : 10,
    'use_es': True,
    'split': 0.1,
    'use_random_init': False,
    'eval_test': True,
    'patience' : 1,
    'use_dropout' : True,
    'dropout_rate' : 0.3,
    'pruning_percentages' : [0.1, 0.2, 0.1],
    'batch_size': 60
}

SETTINGS_CONV4 = {
    'n_epochs' : 10,
    'use_es': True,
    'split': 0.1,
    'use_random_init': False,
    'eval_test': True,
    'patience' : 1,
    'use_dropout' : True,
    'dropout_rate' : 0.3,
    'pruning_percentages' : [0.1, 0.2, 0.1],
    'batch_size': 60
}

SETTINGS_CONV6 = {
    'n_epochs' : 1,
    'use_es': True,
    'split': 0.1,
    'use_random_init': False,
    'eval_test': True,
    'patience': 1,
    'use_dropout': True,
    'dropout_rate' : 0.3,
    'pruning_percentages' : [0.15, 0.2, 0.1],
    'batch_size': 60
}

TRIALS = 5

OPTIMIZER_CONV2 = tf.keras.optimizers.Adam(learning_rate=2e-4)
OPTIMIZER_CONV4 = tf.keras.optimizers.Adam(learning_rate=3e-4)
OPTIMIZER_CONV6 = tf.keras.optimizers.Adam(learning_rate=3e-4)

CIFAR10_DATA = keras.datasets.cifar10