from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

class CVSplitter:

    def __init__(self, k):
        self.k = k

    def split(self,N):
        indices = np.arange(N)
        np.random.shuffle(indices)

        fold_sizes = np.full(self.k, N // self.k, dtype=int)
        fold_sizes[:N % self.k] += 1

        current = 0

        for fold_size in fold_sizes:
            start, stop = current, current + fold_size
            test_idx = indices[start:stop]
            train_idx = np.concatenate([indices[:start], indices[stop:]])
            yield train_idx, test_idx

            current = stop


if __name__ == '__main__':
    X, y = load_digits(return_X_y=True)
    ks = [2,3,5,10,20]

    for k in ks:
        splitter = CVSplitter(k=k)
        accuracies = []

        for train_idx, test_idx in splitter.split(len(X)):
            X_train, y_train = X[train_idx], y[train_idx]
            X_test, y_test = X[test_idx], y[test_idx]

            clf = DecisionTreeClassifier()
            clf.fit(X_train, y_train)

            preds = clf.predict(X_test)
            accuracies.append(accuracy_score(y_test, preds))

        mean_accuracy = np.mean(accuracies)
        std_accuracy = np.std(accuracies)
        print('k:',k)
        print('mean accuracy:',mean_accuracy)
