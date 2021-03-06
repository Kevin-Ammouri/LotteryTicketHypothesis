import numpy as np
from tensorflow.keras import layers

def prune(network,conv_percent,dense_percent,output_percent):
    weights = network.get_weights()
    mask = {}
    for idx, layer in enumerate(network.model.layers):
        perc = 0            
        if isinstance(layer,layers.Conv2D): # If convolutional layer, mask becomes an array of kernel binaries. 0 means the entire kernel is pruned. (Lowest sum kernels are pruned)
            """perc = 1-conv_percent
            rows, cols, kernel, filt = weights[idx].shape
            kernel_toggle = np.ones(filt)
            k = np.round(filt*perc).astype(int)
            kernels = np.sum(np.abs(weights[idx]),axis=(0,1,2))
            partition = np.argpartition(kernels,k)[0:k]
            kernel_toggle[partition] = 0
            mask.append(kernel_toggle) """
            perc = 1-conv_percent
            rows, cols,kernel,filt = weights[idx].shape
            temp = np.ones((rows, cols,kernel,filt))
            k = np.round(rows*cols*kernel*filt*perc).astype(int)
            flat_weights = weights[idx].flatten()
            flat_mask = temp.flatten()
            partition = np.argpartition(np.abs(flat_weights),k)[0:k]
            flat_mask[partition] = 0
            mask[idx] = flat_mask.reshape((rows,cols,kernel,filt))
            
        elif isinstance(layer,layers.Dense): # If Dense layer, the lowest magnitude weights are pruned. Mask is a matrix of shape weights.
            perc=1-dense_percent
            if(idx == len(network.model.layers)-1):
                perc = 1-output_percent
            rows, cols = weights[idx].shape
            temp = np.ones((rows, cols))
            k = np.round(rows*cols*perc).astype(int)
            flat_weights = weights[idx].flatten()
            flat_mask = temp.flatten()
            partition = np.argpartition(np.abs(flat_weights),k)[0:k]
            flat_mask[partition] = 0
            mask[idx] = flat_mask.reshape((rows,cols))
        else:
            mask[idx] = []
    return mask