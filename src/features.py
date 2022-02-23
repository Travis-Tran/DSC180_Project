import pandas as pd
import numpy as np
from sklearn.decomposition import PCA


def apply_features(raw_sav_data_list, outfile=None):
    def dimensionality_reduction(raw_sav_data):
        reduced = []
        for i in range(raw_sav_data.shape[0]):
            pca = PCA(n_components=1)
            pca_val = pca.fit_transform(raw_sav_data[i])
            # print(pca.explained_variance_ratio_)
            reduced.append(pca_val.mean())

        table = pd.DataFrame()
        table['numbers'] = reduced

        return [table['numbers'].mean(), table['numbers'].std()]

    dim_red_data = [dimensionality_reduction(x) for x in raw_sav_data_list]
    X = np.array(dim_red_data)

    if outfile:
        np.savetxt(outfile, X, delimiter=',')

    return X
