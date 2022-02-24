import os
import fastfuels
import pickle


def get_data(outdir, pull=False):
    """
    get data for train or test
    """
    basedir = os.path.dirname(__file__)

    if outdir == 'test':
        # points = points[:3]
        data_loc = os.path.join(basedir, '..', 'test', 'test.pkl')
    if outdir == 'data/raw':
        data_loc = os.path.join(basedir, '..', 'data', 'raw', 'train.pkl')

    if pull:
        fio = fastfuels.open('https://wifire-data.sdsc.edu:9000/fastfuels/index.fio', ftype='s3')
        fio.cache_limit = 1e14

        # query
        def query_fast_fuels(lat, lon):
            roi = fio.query(lon, lat, 15)
            raw_sav_data = roi.data_dict['sav']
            return raw_sav_data

        # data points
        list_coord = []
        for lon in range(-106 * 10, -96 * 10):
            for lat in range(32 * 10, 46 * 10):
                list_coord.append([lat / 10, lon / 10])

        list_coord = [
            [45, -122.0003],
            [32.938576, -116.684257],
            [32.885801, -116.873526],
            [38.989042, -120.579882],
            [35.19249951084869, -119.86643957481108],
            [43.0174, -120.2062],
            [38.48352662411673, -123.14313953065052],
            [42.808417, -119.870967],
            [42.92275, -113.976283],
            [44.5568, -118.8632],
            [43.683533, -122.652183],
            [47.484433, -118.94625]
        ]

        # query data points
        raw_data = []
        for lat, lon in list_coord:
            query = query_fast_fuels(lat, lon)
            raw_data.append(query)

        # write
        output = open(data_loc, 'wb')
        pickle.dump(raw_data, output)
        output.close()

    # read
    pkl_file = open(data_loc, 'rb')
    data1 = pickle.load(pkl_file)
    pkl_file.close()

    return data1
