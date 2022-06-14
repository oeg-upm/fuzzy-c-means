# fuzzy-c-means
Fuzzy c-means Clustering


## Description
This implementation is based on the paper
**FCM: The fuzzy c-means clustering algorithm**  by: *James C.Bezdek, Robert Ehrlich, and  William Full*

## To run the tests
`sh run_tests.sh`

## To run the coverage
`sh run_coverage.sh`

## Install via pip
```pip install fuzzycmeans```


## How to use it
1. Fit the model. This is to cluster any given data *X*.
```Python
X = np.array([[1, 1], [1, 2], [2, 2], [0, 0], [0, 0]])
fcm = FCM(n_clusters=3, max_iter=1)
fcm.fit(X, [0, 0, 0, 1, 2])
```
2. (Optional.) Use the model to assign new data points to existing clusters. Note that the predict function would return the membership as this a fuzzy clustering. 
```Python
Y = np.array([[1, 2], [2, 2], [3, 1], [2, 1], [6, 8]])
membership = fcm.predict(Y)
```


