import pytest
import numpy as np
from fuzzycmeans import FCM


def single_known_cluster():
    X = np.array([[1, 1], [1, 2], [2, 2]])
    fcm = FCM(n_clusters=3, max_iter=1)
    fcm.fit(X, [0, 0, 0])


def fit_from_centroids():
    data_test = [178.75, 5.97390157]
    data_height = [170., 186., 182., 177.]
    data_size = [40, 42, 45, 47, 50]
    data_injuries = [3, 4, 1, 0]
    centers = [[175., 4.08],
               [44.8, 3.54],
               [2., 1.58]]
    fcm = FCM(n_clusters=3, max_iter=1)
    fcm.cluster_centers_ = np.array(centers)
    fcm.fit(fcm.cluster_centers_, [0, 1, 2])
    membership_height = fcm.predict(np.array([data_test]))
    membership_height = fcm.predict(np.array([[np.average(data_height), np.std(data_height)]]))
    membership_size = fcm.predict(np.array([[np.average(data_size), np.std(data_size)]]))
    membership_injuries = fcm.predict(np.array([[np.average(data_injuries), np.std(data_injuries)]]))