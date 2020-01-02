'''
helpers.py

Description: Helper Functions for Plaut Model
  - get_accuracy: to calculate the accuracy of a set of given word types in a dataset
  - make_plot: makes a line plot with multiple lines
  - make_folder: makes a new folder to store simulation results

Date Created: November 27, 2019

Revisions:
  - Jan 01, 2020: multiple revisions, see below:
      > migrate code to make new folder for simulation from plaut_model.ipynb
  - Nov 28, 2019: modify get_accuracy to have option to analyze vowels only
  - Nov 27, 2019: multiple changes, see below:
      > create file, copy get_accuracy from plaut_model.ipynb file
      > modify get_accuracy to take a list of word types at once
      > write make_plot function

'''

import pandas as pd
import torch
from matplotlib import pyplot as plt
import os
import datetime
from pathlib import Path

# function to get the accuracy of a particular category
def get_accuracy(model, data_loader, cat=['All'], vowels_only=False):
    correct = [0.0 for i in cat]
    total = [0.0 for i in cat]
    accuracy = [0.0 for i in cat]
    for i, data in enumerate(data_loader):  # get batch from dataloader
        # extract inputs, labels, type from batch
        inputs = data["graphemes"].float()
        labels = data["phonemes"].float()
        types = pd.DataFrame(data["type"])
        
        outputs = model(inputs).round()  # find prediction using model, then round to 0 or 1
       
        # The following section compares the outputs with the labels, torch.eq performs an element-wise
        # comparison between the two input vectors, and .sum sums up the amount of indentical (i.e. correct)
        # elements in each word -> compare is dim [# of samples]
        if vowels_only == True:
            compare = torch.eq(outputs[:, 23:37], labels[:, 23:37]).sum(dim=1) # compare vowel section only with labels
            compare_len = 14 # length to compare is only # of vowels
        else:
            compare = torch.eq(outputs, labels).sum(dim=1)  # compare with labels
            compare_len = 61 # length to compare is entire phonology vector

        for j in range(len(cat)): # for each desired type
            if cat[j] == 'All':
                correct[j] += torch.eq(compare, compare_len).sum().item() # count as correct if all desired elements match label
                total[j] += len(compare) # accumulate number of samples
            else:
                curr_type = types.apply(lambda x: x == cat[j])  # check for desired type
                temp_compare = pd.DataFrame(compare) # create dataframe using compare to faciliate next line (vector comparison)
                correct[j] += ((curr_type == True) & (temp_compare == compare_len)).sum()[0] # correct if desired type AND all desired elements match label
                total[j] += (curr_type == True).sum()[0] # count all of the desired type
                
    for i in range(len(accuracy)):
        accuracy[i] = correct[i]/total[i] # calculate accuracy: divide correct samples by total samples
    
    return accuracy

def make_plot(x_data, y_data, labels, x_label, y_label, title, save=False, filepath=None):
    plt.figure()  # initialize figure

    # for multiple lines on same graph, plot one at a time
    for data, label in zip(y_data, labels):
        plt.plot(x_data, data, label=label)
    
    #axis labels, title, legend
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend(loc='best')
    
    # save plot at filepath if needed
    if save == True:
        plt.savefig(filepath, dpi=200)

    plt.show() # show plot in Jupyter Notebook cell output
    return None

def make_folder():
    # create a new folder for every run
    path = Path(os.getcwd()).parent #get parent (Plaut_Model) directory filepath
    now = datetime.datetime.now()
    date = now.strftime("%b").lower()+now.strftime("%d")
    i = 1

    while True:
        try:
            rootdir = str(path)+"/results/"+date+"_test"+'{:02d}'.format(i)
            os.mkdir(rootdir)
            break
        except:
            i += 1

    return rootdir
