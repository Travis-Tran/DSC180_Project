import os
import fastfuels
import pickle


def get_data(outdir, pull=False):
    """
    get data for train or test
    """
    basedir = os.path.dirname(__file__)

    if outdir == 'test':
        points = points[:3]
        data_loc = os.path.join(basedir, '..', 'test', 'test.pkl')
    if outdir == 'data/raw':
        data_loc = os.path.join(basedir, '..', 'data', 'raw', 'train.pkl')

    if pull:
        fio = fastfuels.open('https://wifire-data.sdsc.edu:9000/fastfuels/index.fio', ftype='s3')
        fio.cache_limit = 1e14

        raw_data = []

        def query_fast_fuels(lat, lon):
            roi = fio.query(lon, lat, 15)
            raw_sav_data = roi.data_dict['sav']
            return raw_sav_data

        # NEW
        list_coord = []
        for lon in range(-106 * 10, -96 * 10):
            for lat in range(32 * 10, 46 * 10):
                list_coord.append([lat / 10, lon / 10])
        list_coord = list_coord[:int(14000 / 400)]

        for lat, lon in list_coord:
            raw_data.append((query_fast_fuels(lat, lon)))

        # write
        output = open(data_loc, 'wb')
        pickle.dump(raw_data, output)
        output.close()

    # read
    pkl_file = open(data_loc, 'rb')
    data1 = pickle.load(pkl_file)
    pkl_file.close()

    return data1
