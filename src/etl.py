import os
import fastfuels
import pickle
import pprint


def get_data(outdir, points, pull=False):
    """
    get data for train or test
    """
    basedir = os.path.dirname(__file__)

    if outdir == 'test':
        points = points[:1]
        data_loc = os.path.join(basedir, '..', 'data', 'raw', 'train.pkl')
    if outdir == 'data/raw':
        data_loc = os.path.join(basedir, '..', 'test', 'test.pkl')

    if pull:
        fio = fastfuels.open('https://wifire-data.sdsc.edu:9000/fastfuels/index.fio', ftype='s3')
        fio.cache_limit = 1e14

        raw_data = []

        def query_fast_fuels(lat, lon):
            roi = fio.query(lon, lat, 15)
            raw_sav_data = roi.data_dict['sav']
            return raw_sav_data

        for lat, lon in points:
            raw_data.append((query_fast_fuels(lat, lon)))

        # write
        output = open(data_loc, 'wb')
        pickle.dump(raw_data, output)
        output.close()

    # read
    pkl_file = open(data_loc, 'rb')
    data1 = pickle.load(pkl_file)
    # pprint.pprint(data1)
    pkl_file.close()

    return data1
