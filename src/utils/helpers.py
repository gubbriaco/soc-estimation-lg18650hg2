import os
import pandas as pd


def get_dataframe(dir_path, listdir, delimiter=',', axis=0, ignore_index=True):
    df = pd.DataFrame()
    for name in listdir:
        path = os.path.join(dir_path, name)
        df = pd.concat(
            [df, pd.read_csv(path, delimiter=delimiter)],
            axis=axis,
            ignore_index=ignore_index
        )
    return df
