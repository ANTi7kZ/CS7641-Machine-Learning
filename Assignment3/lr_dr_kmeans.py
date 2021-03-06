import pandas as pd

from clustertesters import lr_KMeansTestCluster as kmtc


def encode_target(df, target_column):
    """Add column to df with integers for the target.

    Args
    ----
    df -- pandas DataFrame.
    target_column -- column to map to int, producing
                     new Target column.

    Returns
    -------
    df_mod -- modified DataFrame.
    targets -- list of target names.
    """
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod[target_column].replace(map_to_int, inplace=True)
    return (df_mod, map_to_int)

if __name__ == "__main__":
    letter_recognition = pd.read_csv("letter_ig_reduced.csv")
    dft, mapping = encode_target(letter_recognition, "class")
    #dft.to_csv('letternew.cvs')
    #print dft
    #dft2 = pd.read_csv("phishing.csv")
    X = (dft.ix[:,:-1])
    y = dft.ix[:, -1]
    #print X
    #print y
    tester = kmtc.KMeansTestCluster(X, y, clusters=range(1,31), plot=True, targetcluster=2, stats=True)
    tester.run()





