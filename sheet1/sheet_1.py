import pandas as pd
import numpy as np

def load_data(path):
    """
    Load data from an external file.
    Args:
        path (str): The file path
    Returns:
        X, y (tuple): A data matrix and a label vector
    """
    df = pd.read_csv(path, header=None)
    y = df.iloc[:, 0].values
    X = df.iloc[:, 1:].values

    return X, y

def entropy(y):

    if len(y) == 0:
        return 0
    _, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)

    return -np.sum(probs * np.log2(probs))

def information_gain(X, y, idx):

    total_entropy = entropy(y)
    values, counts = np.unique(X[:, idx], return_counts=True)

    weighted_entropy = 0
    for v, count in zip(values, counts):
        subset_y = y[X[:, idx] == v]
        weighted_entropy += (count / len(y)) * entropy(subset_y)

    return total_entropy - weighted_entropy

class ID3Tree:

    def __init__(self) -> None:
        self.root = Node()

    def train(self, X, y) -> None:
        # recursively run node train
        all_indices = list(range(X.shape[1]))
        self.root.train(X, y, all_indices)

    def predict(self, X) -> None:
        # recursively run node predict
        return np.array([self.root.predict(x) for x in X])

    def print(self):
        # recursively run node print
        self.root.print()

class Node:

    def __init__(self) -> None:
        self.leaf = False
        self.split_attribute = None
        self.label = None
        self.children = {}

    def train(self, X, y,available_indices) -> None:

        if entropy(y) == 0:
            self.leaf = True
            self.label = y[0]
            return

        if not available_indices:
            self.leaf = True
            self.label = 1 if np.sum(y) >= len(y) / 2 else 0
            return

        self.split_attribute = self.select_best_attribute(X, y, available_indices)

        remaining_indices = [i for i in available_indices if i != self.split_attribute]

        for val in np.unique(X[:, self.split_attribute]):
            mask = X[:, self.split_attribute] == val
            if not np.any(mask):
                continue

            new_node = Node()
            self.children[val] = new_node
            new_node.train(X[mask], y[mask], remaining_indices)

    def predict(self, X) -> None:

        if self.leaf:
            return self.label

        val = X[self.split_attribute]
        if val in self.children:
            return self.children[val].predict(X)
        return self.label


    def print(self):

        if self.leaf:
            print(self.label)
        else:
            print(self.split_attribute)
            for val, child_node in self.children.items():
                print(val)
                child_node.print()

    def select_best_attribute(self, X, y, available_indices):

        gains = {i: information_gain(X, y, i) for i in available_indices}
        return max(gains, key=gains.get)


if __name__ == '__main__':
    # add your code here
    X_train, y_train = load_data('data/SPECT.train')
    X_test, y_test = load_data('data/SPECT.test')

    tree = ID3Tree()
    tree.train(X_train, y_train)
    tree.print()

    preds = tree.predict(X_test)
    accuracy = np.mean(preds == y_test)
    print(f"Test Accuracy: {accuracy * 100:.2f}%")