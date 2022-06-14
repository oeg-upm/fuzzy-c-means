import numpy as np
import logging

import sys
sys.path.append('..')


from fuzzycmeans import FCM
from fuzzycmeans.visualization import draw_model_2d


def example():
    X = np.array([[1, 1], [1, 2], [2, 2], [9, 10], [10, 10], [10, 9], [9, 9], [20,20]])
    fcm = FCM(n_clusters=3)
    fcm.fit(X, [0, 0, 0, 1, 1, 1, 1, 2])
    # fcm.fit(X)
    testing_data = np.array([[0, 1.9], [5, 3], [4, 4], [8, 9], [9.5, 6.5], [5, 5], [15,15], [12,12], [14,14], [19,10]])
    predicted_membership = fcm.predict(testing_data)
    print("\n\ntesting data")
    print(testing_data)
    print("predicted membership")
    print(predicted_membership)
    print("\n\n")
    draw_model_2d(fcm, data=testing_data, membership=predicted_membership)
    # draw_model_2d(fcm, data=X, membership=fcm.u)


def example_single_known_zero_filled():
    X = np.array([[1, 1], [1, 2], [2, 2], [0, 0], [0, 0]])
    fcm = FCM(n_clusters=3, max_iter=1)
    fcm.fit(X, [0, 0, 0, 1, 2])
    draw_model_2d(fcm, data=X, membership=fcm.u)


def example_single_known():
    X = np.array([[1, 1], [1, 2], [2, 2], [0, 0], [0, 0]])
    fcm = FCM(n_clusters=3, max_iter=1)
    fcm.fit(X, [0, 0, 0, 1, 2])
    draw_model_2d(fcm, data=X, membership=fcm.u)
    print(fcm.u)


# example()
example_single_known()
