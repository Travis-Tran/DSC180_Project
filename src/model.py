import fastfuels

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from sklearn.cluster import KMeans, Birch


import joblib


def models():
    mdls = {
        "KMeans": KMeans,
        "Birch": Birch
    }

    return mdls


def model_build(
        features,
        predictions_fp,
        mdl_fp,
        modeltype,
        test_size,
        **params):
    X_train, X_test = train_test_split(features, test_size=test_size)

    mdl = models()[modeltype]  # get model from dict
    mdl = mdl(**params)  # instantiate model w/given params

    pl = Pipeline([
        ('mdl', mdl)
    ])

    pl.fit(X_train)
    predictions = pl.predict(X_test)
    out = pd.DataFrame({'predictions': predictions})

    out.to_csv(predictions_fp, index=False)
    joblib.dump(pl, mdl_fp, compress=1)

    return out


def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    return [json.loads(gdf.to_json())['features'][0]['geometry']]


def geo_dataframe(long, lat):
    output = []

    minx, miny = lat, long
    maxx, maxy = lat + 0.0003, long + 0.0003

    bbox = geometry.box(minx, miny, maxx, maxy)

    geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=crs.from_epsg(4326))  # Word Geodetic System 1984
    geo_utm = geo.to_crs(crs=src.crs.data)
    coords = getFeatures(geo_utm)
    out_img, out_transform = rasterio.mask.mask(src, shapes=coords, crop=True)

    output.append(np.unique(out_img)[0])
    #    fig,ax=plt.subplots(1,2)

    #    h=ax[0].imshow(out_img[0,:,:], origin="upper", vmin=91., vmax=189.)
    fig.colorbar(h, shrink=0.5)

    roi = fio.query(lat, long, 15)
    #    print(roi.view('sav'))
    raw_sav_data = roi.data_dict['sav']

    pixels = []
    for x in range(len(raw_sav_data)):
        for y in raw_sav_data[x]:
            avg = sum(y)
            pixels.append(avg)

    df = pd.DataFrame()
    df['Pix'] = pixels
    print(df['Pix'].hist())

    output.append([sum(pixels) / len(pixels)])  # (df[df['Pix'] < 20].shape[0] / df.shape[0] * 100)

    print('The label for this region is ' + str(output[0]))
    print('The sum of non-flat surface in this region is ' + str(output[1]))
    return output
