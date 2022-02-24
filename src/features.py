import pandas as pd
import numpy as np
from sklearn.decomposition import PCA


def apply_features(raw_sav_data_list, outfile=None):
    np.seterr(invalid='ignore')

    def dimensionality_reduction(raw_sav_data):
        # new
        columns = []
        for x in raw_sav_data:
            for cols in x:
                columns.append(cols)

        pca = PCA(n_components=1)
        pca_val = pca.fit_transform(columns)

        # mean
        for i, cols in enumerate(columns):
            cols[cols == 0] = np.nan
            z = np.nanmean(cols)
            np.append(pca_val[i], z)

        return pca_val

    dim_red_data = [datum for x in raw_sav_data_list for datum in dimensionality_reduction(x)]
    X = np.array(dim_red_data)

    if outfile:
        np.savetxt(outfile, X, delimiter=',')

    return X
