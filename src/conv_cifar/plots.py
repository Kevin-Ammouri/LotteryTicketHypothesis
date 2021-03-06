import numpy as np
import matplotlib.pyplot as plt
from tools import generate_percentages
from constants import SETTINGS_CONV2, SETTINGS_CONV4, SETTINGS_CONV6

# Create consistent mapping for all plots

percentages24, _ = generate_percentages([1.0, 1.0, 1.0], 0.02, SETTINGS_CONV2['pruning_percentages'])
percentages_list_conv24 = list()
percentages_list_conv24.append(100.0)
for i in range(len(percentages24)):
    percentages_list_conv24.append(percentages24[i][1]*100)

percentages6, _ = generate_percentages([1.0, 1.0, 1.0], 0.02, SETTINGS_CONV6['pruning_percentages'])

percentages_list_conv6 = list()
percentages_list_conv6.append(100.0)
for i in range(len(percentages6)):
    percentages_list_conv6.append(percentages6[i][1]*100)

def plot_dropout():
    """
        Plots network accuracy and early-stop epoch for networks 
        with and without dropout applied.
    """
    conv2_dropout_hist = np.load("data/conv2_rand-False_bn-False_dropout.npz", allow_pickle=True)['histories']
    conv2_dropout_epochs = np.load("data/conv2_rand-False_bn-False_dropout.npz", allow_pickle=True)['es_epochs']

    conv4_dropout_hist = np.load("data/conv4_rand-False_bn-False_dropout.npz", allow_pickle=True)['histories']
    conv4_dropout_epochs = np.load("data/conv4_rand-False_bn-False_dropout.npz", allow_pickle=True)['es_epochs']

    conv6_dropout_hist = np.load("data/conv6_rand-False_bn-False_dropout.npz", allow_pickle=True)['histories']
    conv6_dropout_epochs = np.load("data/conv6_rand-False_bn-False_dropout.npz", allow_pickle=True)['es_epochs']

    conv2_hist = np.load("data/conv2_rand-False_bn-False.npz", allow_pickle=True)['histories']
    conv2_epochs = np.load("data/conv2_rand-False_bn-False.npz", allow_pickle=True)['es_epochs']

    conv4_hist = np.load("data/conv4_rand-False_bn-False.npz", allow_pickle=True)['histories']
    conv4_epochs = np.load("data/conv4_rand-False_bn-False.npz", allow_pickle=True)['es_epochs']

    conv6_hist = np.load("data/conv6_rand-False_bn-False.npz", allow_pickle=True)['histories']
    conv6_epochs = np.load("data/conv6_rand-False_bn-False.npz", allow_pickle=True)['es_epochs']

    # Plots test accuracy at early-stop for all percentages of weights remaining

    plt.plot(percentages_list_conv6, conv6_dropout_hist, label="Conv-6 dropout", marker='v', color='g')
    plt.plot(percentages_list_conv6, conv6_hist, label="Conv-6", marker='v', color='g', linestyle='--')

    plt.plot(percentages_list_conv24, conv4_dropout_hist, label="Conv-4 dropout", marker='o', color='k')
    plt.plot(percentages_list_conv24, conv4_hist, label="Conv-4", marker='o', color='k', linestyle='--')

    plt.plot(percentages_list_conv24, conv2_dropout_hist, label="Conv-2 dropout", marker='+', color='b')
    plt.plot(percentages_list_conv24, conv2_hist, label="Conv-2", marker='+', color='b', linestyle='--')

    plt.legend()
    plt.title("Test accuracy for different ConvNets both with and without dropout applied")
    plt.xlabel("Percent of Weights Remaining")
    plt.ylabel("Accuracy at Early-Stop (Test)")

    plt.xlim(left=100.5, right=1.5)
    #plt.ylim(bottom=0.6, top=0.8)
    plt.xscale('log')
    plt.grid()
    plt.xticks([100, 51.4, 26.5, 13.7, 7.1, 3.7, 1.75], [100, 51.4, 26.5, 13.7, 7.1, 3.7, 1.75])
    plt.show()

    # Plots the epoch at which early-stop was occured for all percentages of weights remaining

    plt.plot(percentages_list_conv6, conv6_dropout_epochs, label="Conv-6 dropout", marker='v', color='g')
    plt.plot(percentages_list_conv6, conv6_epochs, label="Conv-6", marker='v', color='g', linestyle='--')

    plt.plot(percentages_list_conv24, conv4_dropout_epochs, label="Conv-4 dropout", marker='o', color='k')
    plt.plot(percentages_list_conv24, conv4_epochs, label="Conv-4", marker='o', color='k', linestyle='--')

    plt.plot(percentages_list_conv24, conv2_dropout_epochs, label="Conv-2 dropout", marker='+', color='b')
    plt.plot(percentages_list_conv24, conv2_epochs, label="Conv-2", marker='+', color='b', linestyle='--')

    plt.legend()
    plt.title("Early-stop epoch for different ConvNets both with and without dropout applied")
    plt.xlabel("Percent of Weights Remaining")
    plt.ylabel("Early-Stop Epoch (Val.)")

    plt.xlim(left=100.5, right=1.5)
    plt.ylim(bottom=0., top=20)
    plt.xscale('log')
    plt.grid()
    plt.xticks([100, 51.4, 26.5, 13.7, 7.1, 3.7, 1.75], [100, 51.4, 26.5, 13.7, 7.1, 3.7, 1.75])
    plt.show()
    
def plot_no_reg():
    """
        Plots the figures both winning ticket and reinit with 
        no regularisation applied (accuracy and early-stop epoch).
    """
    # Load the data
    conv2_hist = np.load("data/conv2_rand-False_bn-False.npz", allow_pickle=True)['histories']
    conv2_epochs = np.load("data/conv2_rand-False_bn-False.npz", allow_pickle=True)['es_epochs']

    conv4_hist = np.load("data/conv4_rand-False_bn-False.npz", allow_pickle=True)['histories']
    conv4_epochs = np.load("data/conv4_rand-False_bn-False.npz", allow_pickle=True)['es_epochs']

    conv6_hist = np.load("data/conv6_rand-False_bn-False.npz", allow_pickle=True)['histories']
    conv6_epochs = np.load("data/conv6_rand-False_bn-False.npz", allow_pickle=True)['es_epochs']

    conv2_hist_reinit = np.load("data/conv2_rand-True_bn-False.npz", allow_pickle=True)['histories']
    conv2_epochs_reinit = np.load("data/conv2_rand-True_bn-False.npz", allow_pickle=True)['es_epochs']

    conv4_hist_reinit = np.load("data/conv4_rand-True_bn-False.npz", allow_pickle=True)['histories']
    conv4_epochs_reinit = np.load("data/conv4_rand-True_bn-False.npz", allow_pickle=True)['es_epochs']

    conv6_hist_reinit = np.load("data/conv6_rand-True_bn-False.npz", allow_pickle=True)['histories']
    conv6_epochs_reinit = np.load("data/conv6_rand-True_bn-False.npz", allow_pickle=True)['es_epochs']
    
    # Plots test accuracy at early-stop for all percentages of weights remaining

    plt.plot(percentages_list_conv6, conv6_hist, label="Conv-6", marker='v', color='g')
    plt.plot(percentages_list_conv6, conv6_hist_reinit, label="Conv-6 (reinit)", marker='v', color='g', linestyle='--')

    plt.plot(percentages_list_conv24, conv4_hist, label="Conv-4", marker='o', color='k')
    plt.plot(percentages_list_conv24, conv4_hist_reinit, label="Conv-4 (reinit)", marker='o', color='k', linestyle='--')

    plt.plot(percentages_list_conv24, conv2_hist, label="Conv-2", marker='+', color='b')
    plt.plot(percentages_list_conv24, conv2_hist_reinit, label="Conv-2 (reinit)", marker='+', color='b', linestyle='--')
    
    plt.legend()
    plt.title("Test accuracy for different ConvNets (No regularisation applied)")
    plt.xlabel("Percent of Weights Remaining")
    plt.ylabel("Accuracy at Early-Stop (Test)")

    plt.xlim(left=100.5, right=1.5)
    plt.ylim(bottom=0.6, top=0.8)
    plt.xscale('log')
    plt.grid()
    plt.xticks([100, 51.4, 26.5, 13.7, 7.1, 3.7, 1.75], [100, 51.4, 26.5, 13.7, 7.1, 3.7, 1.75])
    plt.show()

    # Plots the epoch at which early-stop was occured for all percentages of weights remaining

    plt.plot(percentages_list_conv6, conv6_epochs, label="Conv-6", marker='v', color='g')
    plt.plot(percentages_list_conv6, conv6_epochs_reinit, label="Conv-6 (reinit)", marker='v', color='g', linestyle='--')

    plt.plot(percentages_list_conv24, conv4_epochs, label="Conv-4", marker='o', color='k')
    plt.plot(percentages_list_conv24, conv4_epochs_reinit, label="Conv-4 (reinit)", marker='o', color='k', linestyle='--')

    plt.plot(percentages_list_conv24, conv2_epochs, label="Conv-2", marker='+', color='b')
    plt.plot(percentages_list_conv24, conv2_epochs_reinit, label="Conv-2 (reinit)", marker='+', color='b', linestyle='--')

    plt.legend()
    plt.title("Early-stop epoch for different ConvNets using early-stop criterion (No regularisation applied)")
    plt.xlabel("Percent of Weights Remaining")
    plt.ylabel("Early-Stop Epoch (Val.)")

    plt.xlim(left=100.5, right=1.5)
    plt.xscale('log')
    plt.grid()
    plt.xticks([100, 51.4, 26.5, 13.7, 7.1, 3.7, 1.75], [100, 51.4, 26.5, 13.7, 7.1, 3.7, 1.75])
    plt.show()


def plot_BN():
    """
        Plots the figures both winning ticket and reinit for batch normalization (accuracy and early-stop epoch),
        given one has the required data files.
    """
    #Load the data
    conv2_hist_reinit = np.load("data/conv2_rand-True_bn-True.npz", allow_pickle=True)['histories']
    conv2_epochs_reinit = np.load("data/conv2_rand-True_bn-True.npz", allow_pickle=True)['es_epochs']

    conv4_hist_reinit = np.load("data/conv4_rand-True_bn-True.npz", allow_pickle=True)['histories']
    conv4_epochs_reinit = np.load("data/conv4_rand-True_bn-True.npz", allow_pickle=True)['es_epochs']

    conv6_hist_reinit = np.load("data/conv6_rand-True_bn-True.npz", allow_pickle=True)['histories']
    conv6_epochs_reinit = np.load("data/conv6_rand-True_bn-True.npz", allow_pickle=True)['es_epochs']

    conv2_hist = np.load("data/conv2_rand-False_bn-True.npz", allow_pickle=True)['histories']
    conv2_epochs = np.load("data/conv2_rand-False_bn-True.npz", allow_pickle=True)['es_epochs']

    conv4_hist = np.load("data/conv4_rand-False_bn-True.npz", allow_pickle=True)['histories']
    conv4_epochs = np.load("data/conv4_rand-False_bn-True.npz", allow_pickle=True)['es_epochs']

    conv6_hist = np.load("data/conv6_rand-False_bn-True.npz", allow_pickle=True)['histories']
    conv6_epochs = np.load("data/conv6_rand-False_bn-True.npz", allow_pickle=True)['es_epochs']
    
    # Plots test accuracy at early-stop for all percentages of weights remaining

    plt.plot(percentages_list_conv6, conv6_hist, label="Conv-6", marker='v', color='g')
    plt.plot(percentages_list_conv6, conv6_hist_reinit, label="Conv-6 (reinit)", marker='v', color='g', linestyle='--')

    plt.plot(percentages_list_conv24, conv4_hist, label="Conv-4", marker='o', color='k')
    plt.plot(percentages_list_conv24, conv4_hist_reinit, label="Conv-4 (reinit)", marker='o', color='k', linestyle='--')

    plt.plot(percentages_list_conv24, conv2_hist, label="Conv-2", marker='+', color='b')
    plt.plot(percentages_list_conv24, conv2_hist_reinit, label="Conv-2 (reinit)", marker='+', color='b', linestyle='--')

    plt.legend()
    plt.title("Test accuracy for different ConvNets using early-stop criterion")
    plt.xlabel("Percent of Weights Remaining")
    plt.ylabel("Accuracy at Early-Stop (Test)")

    plt.xlim(left=100.5, right=1.5)
    plt.xscale('log')
    plt.grid()
    plt.xticks([100, 51.4, 26.5, 13.7, 7.1, 3.7, 1.75], [100, 51.4, 26.5, 13.7, 7.1, 3.7, 1.75])
    plt.show()

    # Plots the epoch at which early-stop was occured for all percentages of weights remaining

    plt.plot(percentages_list_conv6, conv6_epochs, label="Conv-6", marker='v', color='g')
    plt.plot(percentages_list_conv6, conv6_epochs_reinit, label="Conv-6 (reinit)", marker='v', color='g', linestyle='--')

    plt.plot(percentages_list_conv24, conv4_epochs, label="Conv-4", marker='o', color='k')
    plt.plot(percentages_list_conv24, conv4_epochs_reinit, label="Conv-4 (reinit)", marker='o', color='k', linestyle='--')

    plt.plot(percentages_list_conv24, conv2_epochs, label="Conv-2", marker='+', color='b')
    plt.plot(percentages_list_conv24, conv2_epochs_reinit, label="Conv-2 (reinit)", marker='+', color='b', linestyle='--')

    plt.legend()
    plt.title("Early-stop epoch for different ConvNets using early-stop criterion")
    plt.xlabel("Percent of Weights Remaining")
    plt.ylabel("Early-Stop Epoch (Val.)")

    plt.xlim(left=100.5, right=1.5)
    plt.xscale('log')
    plt.grid()
    plt.xticks([100, 51.4, 26.5, 13.7, 7.1, 3.7, 1.75], [100, 51.4, 26.5, 13.7, 7.1, 3.7, 1.75])
    plt.show()

plot_dropout()