import pytest
import numpy as np

from fuzzycmeans import FCM


def test_2d():
    X = np.array([[1, 1], [1, 2], [2, 2], [9, 10], [10, 10], [10, 9], [9, 9]])
    fcm = FCM()
    fcm.fit(X, [0, 0, 0, 1, 1, 1, 1])
    assert len(fcm.cluster_centers_) == 2
    assert fcm.cluster_centers_[0][0] == pytest.approx(1.33333333, 0.1)
    assert fcm.cluster_centers_[0][1] == pytest.approx(1.66666667, 0.1)
    testing_data = np.array([[0, 1.9], [3, 3], [4, 4], [8, 9], [9.5, 6.5]])
    predicted_membership = fcm.predict(testing_data)
    actual_membership = np.array([[0.98777232, 0.01222768],
                                  [0.94884591, 0.05115409],
                                  [0.82813688, 0.17186312],
                                  [0.02482074, 0.97517926],
                                  [0.0908581, 0.9091419]])
    assert predicted_membership == pytest.approx(actual_membership, 0.01)


def test_logger():
    fcm = FCM()
    fcm.get_logger()
    fcm.set_logger(tostdout=True,logfilename="output.html")