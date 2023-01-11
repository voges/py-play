"""Demo of scikit-learn's DecisionTreeClassifier."""


import matplotlib.pyplot as plt
import sklearn.datasets
import sklearn.tree


def main():
    """Train a decision tree on the iris dataset."""
    # This dataset consists of the petal and sepal lengths of three species of
    # Iris (setosa, virginica, and versicolor) stored in a 150x4 numpy.ndarray.
    iris = sklearn.datasets.load_iris()

    # We train a decision tree using the entropy as splitting criterion.
    clf = sklearn.tree.DecisionTreeClassifier(criterion="entropy", random_state=0)
    clf = clf.fit(X=iris.data, y=iris.target)  # pylint: disable=no-member

    # Visualize the tree.
    print(sklearn.tree.export_text(clf, feature_names=iris["feature_names"]))
    sklearn.tree.plot_tree(clf)
    plt.show()


if __name__ == "__main__":
    main()
