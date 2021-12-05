import os
import pandas as pd


def get_data(outdir):
    """
    download and unzip titanic data from Kaggle.
    """

    if outdir == 'test':
        return read_test(outdir)

    if outdir == 'data/raw':
        return read_train(outdir)


def read_train(datadir):
    """
    Reads raw training data from disk.
    (Would normally be more complicated!)
    """
    print('raw ')
    fp = os.path.join(datadir, 'train.csv')
    return pd.read_csv(fp)


def read_test(datadir):
    """
    Reads raw test data from disk.
    (Would normally be more complicated!)
    """
    print('test')
    fp = os.path.join(datadir, 'test.csv')
    return pd.read_csv(fp)