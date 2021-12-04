import pandas as pd

def apply_features(df, feats, outfile=None):

    features = pd.DataFrame()

    for feat in feats:
        f = fmap.get(feat)
        if f is not None:
            # custom feature found
            features[feat] = f(df)
        else:
            # feature is existing column
            features[feat] = df[feat]

    if outfile:
        features.to_csv(outfile, index=False)

    # temp
    features = df
    return features