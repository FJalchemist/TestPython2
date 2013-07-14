#!/usr/bin/env python
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    3d plotting experiments, 2d array can be reshaped by methods.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X = np.arange(0, 1, 0.01)
    Y = np.arange(0, 1, 0.01)

    """
    two-dimentionalize
    """
    X = np.array([X,]*len(X))
    X = X.transpose()
    Y = np.array([Y,]*len(Y))

    Z = np.add(X, Y) - 1.5 * np.multiply(X, Y)
#    X, Y, Z = axes3d.get_test_data(0.05)
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    plt.show()
    return
    

if __name__ == "__main__":
    """
    Announce main
    """
    main()
