import numpy as np

from fuzzycmeans import FCM


def test_2d():
    X = np.array([[1, 1], [1, 2], [2, 2], [9, 10], [10, 10], [10, 9], [9, 9]])
    fcm = FCM()
    fcm.fit(X, [0,0,0,1,1,1,1])
