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

