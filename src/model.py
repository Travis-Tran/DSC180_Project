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


