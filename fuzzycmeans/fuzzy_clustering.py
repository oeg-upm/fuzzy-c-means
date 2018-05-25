import numpy as np
import math
import random
import logging


SMALL_VALUE = 0.00001


class FCM:
    """
        This algorithm is from the paper
        "FCM: The fuzzy c-means clustering algorithm" by James Bezdek
        Here we will use the Euclidean distance

        Pseudo code:
        1) Fix c, m, A
        c: n_clusters
        m: 2 by default
        A: we are using Euclidean distance, so we don't need it actually
        2) compute the means (cluster centers)
        3) update the membership matrix
        4) compare the new membership with the old one, is difference is less than a threshold, stop. otherwise
            return to step 2)
    """

    def __init__(self, n_clusters=2, m=2, max_iter=10):
        self.n_clusters = n_clusters
        self.cluster_centers_ = None
        self.u = None  # The membership
        self.m = m  # the fuzziness, m=1 is hard not fuzzy. see the paper for more info
        self.max_iter = max_iter
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.NullHandler())
        # logger.addHandler(logging.StreamHandler())

    def get_logger(self):
        return self.logger

    def set_logger(self, tostdout=False, logfilename=None, level=logging.WARNING):
        if tostdout:
            self.logger.addHandler(logging.StreamHandler())
        if logfilename:
            self.logger.addHandler(logging.FileHandler(logfilename))
        if level:
            self.logger.setLevel(level)

    def init_membership(self, num_of_points):
        self.init_membership_random(num_of_points)

    def init_membership_equal(self, num_of_points):
        """
        :param num_of_points:
        :return: nothing

        # In the below for loop, due to the rounding to 2 decimals, you may think that the membership sum for
        #  a point can be larger than 1. this can happen if number of clusters is larger than 10.
        # mathematical proof that this can happen:
        # (1) --- max_error per point membership to a single cluster is 0.01 (because of the rounding to 2 decimal
        #   points).
        # (2) --- (c-1) * 0.01 >= 1/c
        # (3) --- c^2 - c >= 1
        # solving for c we get c = 10.51 (approx.)
        # so when c >= 11, this error may occur.

        But I added a check below to prevent such a thing from happening
        """
        self.u = np.zeros((num_of_points, self.n_clusters))
        for i in xrange(num_of_points):
            row_sum = 0.0
            for c in xrange(self.n_clusters):
                if c == self.n_clusters-1:  # last iteration
                    self.u[i][c] = 1 - row_sum
                else:
                    rand_num = round(1.0/self.n_clusters, 2)
                    if rand_num + row_sum >= 1.0:  # to prevent membership sum for a point to be larger than 1.0
                        if rand_num + row_sum - 0.01 >= 1.0:
                            self.logger.error('Something is not right in the init_membership')
                            return None
                        else:
                            self.u[i][c] = rand_num - 0.01
                    else:
                        self.u[i][c] = rand_num
                    row_sum += self.u[i][c]

    def init_membership_random(self, num_of_points):
        """
        :param num_of_points:
        :return: nothing

        """
        self.u = np.zeros((num_of_points, self.n_clusters))
        for i in xrange(num_of_points):
            row_sum = 0.0
            for c in xrange(self.n_clusters):
                if c == self.n_clusters-1:  # last iteration
                    self.u[i][c] = 1.0 - row_sum
                else:
                    rand_clus = random.randint(0, self.n_clusters-1)
                    rand_num = random.random()
                    rand_num = round(rand_num, 2)
                    if rand_num + row_sum <= 1.0:  # to prevent membership sum for a point to be larger than 1.0
                        self.u[i][rand_clus] = rand_num
                        row_sum += self.u[i][rand_clus]

    def compute_cluster_centers(self, X, update_func=None):
        """
        :param X:
        :return:

        vi = (sum of membership for cluster i ^ m  * x ) / sum of membership for cluster i ^ m  : for each cluster i

        """
        num_of_points = X.shape[0]
        num_of_features = X.shape[1]
        centers = []
        if update_func is None:
            for c in xrange(self.n_clusters):
                sum1_vec = np.zeros(num_of_features)
                sum2_vec = 0.0
                for i in xrange(num_of_points):
                    interm1 = (self.u[i][c] ** self.m)
                    interm2 = interm1 * X[i]
                    sum1_vec += interm2
                    sum2_vec += interm1
                    if np.any(np.isnan(sum1_vec)):
                        self.logger.debug("compute_cluster_centers> interm1 %s" % str(interm1))
                        self.logger.debug("compute_cluster_centers> interm2 %s" % str(interm2))
                        self.logger.debug("compute_cluster_centers> X[%d] %s" % (i, str(X[i])))
                        self.logger.debug("compute_cluster_centers> loop sum1_vec %s" % str(sum1_vec))
                        self.logger.debug("compute_cluster_centers> loop sum2_vec %s" % str(sum2_vec))
                        self.logger.debug("X: [%d] %s" % (i-1, X[i-1]))
                        self.logger.debug("X: [%d] %s" % (i+1, X[i+1]))
                        self.logger.debug("X: ")
                        self.logger.debug(X)
                        raise Exception("There is a nan in compute_cluster_centers method if")
                if sum2_vec == 0:
                    sum2_vec = 0.000001
                centers.append(sum1_vec/sum2_vec)
        else:
            for c in xrange(self.n_clusters):
                sum1_vec = np.zeros(num_of_features)
                sum2_vec = 0.0
                for i in xrange(num_of_points):
                    interm1 = (self.u[i][c] ** self.m)
                    interm2 = interm1 * X[i]
                    sum1_vec += interm2
                    sum2_vec += interm1
                    if np.any(np.isnan(sum1_vec)):
                        self.logger.debug("compute_cluster_centers> interm1 %s" % str(interm1))
                        self.logger.debug("compute_cluster_centers> interm2 %s" % str(interm2))
                        self.logger.debug("compute_cluster_centers> X[%d] %s" % (i, str(X[i])))
                        self.logger.debug("compute_cluster_centers> loop sum1_vec %s" % str(sum1_vec))
                        self.logger.debug("compute_cluster_centers> loop sum2_vec %s" % str(sum2_vec))
                        self.logger.debug("X: [%d] %s" % (i-1, X[i-1]))
                        self.logger.debug("X: [%d] %s" % (i+1, X[i+1]))
                        self.logger.debug("X: ")
                        self.logger.debug(X)
                        raise Exception("There is a nan in compute_cluster_centers method else")
                if sum2_vec == 0:
                    sum2_vec = 0.000001
                centers.append(sum1_vec/sum2_vec)
                update_func(int(c * 1.0 / self.n_clusters * 100))
            update_func(100)

        self.cluster_centers_ = centers
        return centers

    def distance_squared(self, x, c):
        """
        Compute the Euclidean distance
        :param x: is a single point from the original data X
        :param c: is a single point that represent a center or a cluster
        :return: the distance
        """
        sum_of_sq = 0.0
        for i in xrange(len(x)):
            sum_of_sq += (x[i]-c[i]) ** 2
        return sum_of_sq

    def compute_membership_single(self, X, datapoint_idx, cluster_idx):
        """
        :param datapoint_idx:
        :param cluster_idx:
        :return: return computer membership for the given ids
        """
        clean_X = X
        d1 = self.distance_squared(clean_X[datapoint_idx], self.cluster_centers_[cluster_idx])
        sum1 = 0.0
        for c in self.cluster_centers_:  # this is to compute the sigma
            d2 = self.distance_squared(c, clean_X[datapoint_idx])
            if d2 == 0.0:
                d2 = SMALL_VALUE
            sum1 += (d1/d2) ** (1.0/(self.m-1))
            if np.any(np.isnan(sum1)):
                self.logger.debug("nan is found in compute_membership_single")
                self.logger.debug("d1: %s" % str(d1))
                self.logger.debug("sum1: %s" % str(sum1))
                self.logger.debug("d2: %s" % str(d2))
                self.logger.debug("c: %s" % str(c))
                self.logger.debug("X[%d] %s" % (datapoint_idx, str(clean_X[datapoint_idx])))
                self.logger.debug("centers: %s" % str(self.cluster_centers_))
                raise Exception("nan is found in computer_memberhip_single method in the inner for")
        if sum1 == 0:  # because otherwise it will return inf
            return 1.0 - SMALL_VALUE
        if np.any(np.isnan(sum1 ** -1)):
            self.logger.debug("nan is found in compute_membership_single")
            self.logger.debug("d1: %s" % str(d1))
            self.logger.debug("sum1: %s" % str(sum1))
            self.logger.debug("X[%d] %s" % (datapoint_idx, str(clean_X[datapoint_idx])))
            self.logger.debug("centers: %s" % str(self.cluster_centers_))
            raise Exception("nan is found in computer_memberhip_single method")
        return sum1 ** -1

    def update_membership(self, X):
        """
        update the membership matrix
        :param X: data points
        :return: nothing

        For performance, the distance can be computed once, before the loop instead of computing it every time
        """
        for i in xrange(X.shape[0]):
            for c in xrange(len(self.cluster_centers_)):
                self.u[i][c] = self.compute_membership_single(X, i, c)

    def fit(self, X, y=None, hard=True):
        """
        :param X:
        :param y: list of clusters or a membership, now only support the hard y list which will generate
        the membership
        :param hard: whether y contains a list of clusters or a membership matrix
        :return: self
        """
        X = np.array(X)
        if y is not None:
            y = np.array(y)
            if hard:
                self.set_membership_from_hard_cluster(X, y)
        if self.cluster_centers_ is None:
            do_compute_cluster_centers = True
        else:
            do_compute_cluster_centers = False
        if self.u is None:
            num_of_points = X.shape[0]
            self.init_membership_random(num_of_points)
        #self.init_membership(X.shape[0])
        list_of_centers = []
        membership_history = []
        membership_history.append(self.u.copy())
        for i in xrange(self.max_iter):
            if do_compute_cluster_centers:
                centers = self.compute_cluster_centers(X)
                if i == 0:
                    init_centers = centers
                list_of_centers.append(centers)
            else:
                init_centers = self.cluster_centers_
                list_of_centers = [init_centers]
            self.update_membership(X)
            membership_history.append(self.u.copy())
            self.logger.info("updated membership is: ")
            self.logger.info(self.u)
        return self

    def predict(self, X):
        if self.u is None:
            u = None
        else:
            u = self.u.copy()
        self.u = np.zeros((X.shape[0], self.n_clusters))
        self.update_membership(X)
        predicted_u = self.u.copy()
        if np.any(np.isnan(predicted_u)):
            self.logger.debug("predict> has a nan")
            self.logger.debug("u:")
            self.logger.debug(u)
            raise Exception("There is a nan in predict method")
        self.u = u
        return predicted_u

    def set_membership_from_hard_cluster(self, X, y):
        """
        Computer the membership matrix for each point from the corresponding cluster id in "y"
        :param X: input data points
        :param y: list of clusters, each correspond to the input data X
        :return: None
        """
        u = np.zeros((X.shape[0], len(y)))
        for clus, md in enumerate(y):
            u[md][clus] = 1.0
        self.u = u.T
        self.logger.debug("set_membership_from_hard_cluster > membership: ")
        self.logger.debug(self.u)
        num_of_points = X.shape[0]
        num_of_features = X.shape[1]
        self.logger.debug("num of points: %s" % str(num_of_points))
        self.logger.debug("num of features: %s" % str(num_of_features))
        self.compute_cluster_centers(X, update_func=None)
        self.logger.debug("set_membership_from_hard_cluster > cluster centers: ")
        self.logger.debug(self.cluster_centers_)
