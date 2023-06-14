"""
    Recursive feature elimination (RFE) with logistic regression as estimator
"""

from pydoc import doc
from utils_data_processing import preprocess_imdb
import os
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MaxAbsScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from utils_data_processing import LinearPipeline
from sklearn.feature_selection import RFE
import utils

ngram_range = (1, 2)
min_df = 2
C = 0.5
n_folds = 5
num_jobs = -1
ngram = 2
num_features = 10000
step = 10000


if __name__ == "__main__":
    traindata, _, testdata = preprocess_imdb(num_jobs=num_jobs)

    cache_name = "imdb_wrapper.pkz"
    try:
        X_train, y_train, X_test, y_test, vocabulary = utils.load_cache(
            cache_name, ["X_train", "y_train", "X_test", "y_test", "vocabulary"]
        )
    except RuntimeError as err:
        traindata, _, testdata = preprocess_imdb(num_jobs=num_jobs)


    """
    Add lines here
    """