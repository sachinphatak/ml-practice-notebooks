from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    markers = ['s', 'x', '^', '*', 'v']
    colors = ['red', 'blue', 'lightgreen', 'cyan', 'gray']
    cmap = ListedColormap(colors[:len(np.unique(y))])
    x1_min, x1_max = np.min(X[:, 0]), np.max(X[:, 0])
    x2_min, x2_max = np.min(X[:, 1]), np.max(X[:, 1])
    xx1, xx2 = np.meshgrid(np.arange(x1_min-1, x1_max+1, resolution), np.arange(x2_min-1, x2_max+1, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(X[y == cl, 0], X[y == cl, 1], marker=markers[idx], color=cmap(idx), alpha=0.8, label=cl)
        
    if test_idx:
        X_test, y_test = X[test_idx,:], y[test_idx]
        plt.scatter(X_test[:,0], X_test[:,1], facecolors='none', edgecolors='black', alpha=1.0, linewidth=1, marker='o', s=55, label='test set')