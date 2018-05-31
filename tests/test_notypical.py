import pytest
import numpy as np

from fuzzycmeans import FCM


def single_known_cluster():
    X = np.array([[1, 1], [1, 2], [2, 2]])
    fcm = FCM(n_clusters=3, max_iter=1)
    fcm.fit(X, [0, 0, 0])

