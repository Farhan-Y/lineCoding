import matplotlib.pylab as plt
from digital_data_to_signal import dataToSignal
import numpy as np


class gui:
    def __init__(self, mybin = dataToSignal('101000110')):
        self.mybin = mybin 


    def plot_NRZ(self):
        signal = [1] + self.mybin.NRZ() # 1 is added just for meaningfull graphical representation

        fig , ax = plt.subplots(figsize=(8,5))
        ax.set_title("NRZ")
        ax.step(np.arange(0 , len(signal) , 1) , signal )
        ax.set_xticks(range(0,len(signal)))
        plt.show()


    def plot_NRZL(self):

        signal = [1] +  self.mybin.NRZL() # 1 is added just for meaningfull graphical representation
        fig , ax = plt.subplots(figsize=(8,5))
        ax.set_title("NRZL")
        ax.step(np.arange(0 , len(signal) , 1) , signal )
        ax.set_xticks(range(0,len(signal)))
        plt.show()


    def plot_NRZI(self):
      
        signal = self.mybin.NRZI(start= '1')  # no need to add anything in the beginning.
        fig , ax = plt.subplots(figsize=(8,5))
        ax.set_title("NRZI")
        ax.step(np.arange(0 , len(signal) , 1) , signal )
        ax.set_xticks(range(0,len(signal)))
        plt.show()

    def plot_Manchester(self , ieee802dot3 = False ):
        signal = [1] + self.mybin.toManchester(ieee802dot3 = ieee802dot3)  
        fig , ax = plt.subplots(figsize=(8,5))
        ax.set_title("Manchester")
        ax.step(np.arange(0 , len(signal)/2 , 0.5) , signal )
        ax.set_xticks(range(0,len(signal)//2))
        plt.show()


    def plot_DifferentailManchester(self):
        signal = [1] + self.mybin.toDifferentailManchester() 
        fig , ax = plt.subplots(figsize=(8,5))
        ax.set_title("Differential Manchester")
        ax.step(np.arange(0 , len(signal)/2 , 0.5) , signal )
        ax.set_xticks(range(0,len(signal)//2))
        plt.show()

