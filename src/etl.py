import os
import pandas as pd


def get_data(outdir):
    '''
    download and unzip titanic data from Kaggle.
    '''

    return read_train(outdir)


def read_train(datadir):
    '''
    Reads raw training data from disk.
    (Would normally be more complicated!)
    '''
    fp = os.path.join(datadir, 'train.csv')
    return pd.read_csv(fp)


def read_test(datadir):
    '''
    Reads raw test data from disk.
    (Would normally be more complicated!)
    '''

    fp = os.path.join(datadir, 'test.csv')
    return pd.read_csv(fp)