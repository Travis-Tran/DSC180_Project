import os

basedir = os.path.dirname(__file__)


def make_datadir():

    data_loc = os.path.join(basedir, '..', 'data')

    for d in ['raw', 'temp', 'out']:
        os.makedirs(os.path.join(data_loc, d), exist_ok=True)

    return
