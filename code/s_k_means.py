import os
import numpy as np
import math as m
import random

def read_labeled(directory):
    X = []
    Y = []
    i = 0
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            fileName = os.path.join(root + "/", name)
            f = open(fileName)
            for x in f:
                data = x.split(",")
                data = [float(n) for n in data[:-1]]
                X.append(np.array(data))
                Y.append(i)
            i += 1
    return np.array(X), np.array(Y)
def s_k_means(X, k, iterations):
    #initialization
    n = len(X)
    x = [v / np.linalg.norm(v) for v in X]
    indices = [i for i in range(n)]
    random.shuffle(indices)
    slice_length = m.ceil(len(indices)/k)
    C = [indices[i:i+slice_length] for i in range(0, len(indices), slice_length)]

    for z in range(iterations):
        c = []
        for j in range(k):
            index = C[j]
            cluster = [x[i] for i in index]
            centroid = cluster[0]
            for point in cluster[1:]:
                centroid += point
            c.append(centroid / np.linalg.norm(centroid))
        C = [[] for _ in range(k)]
        for i in range(n):
            cosines = []
            for l in range(k):
                cosine = np.dot(c[l], x[i])/(np.linalg.norm(c[l])*np.linalg.norm(x[i]))
                cosines.append(cosine)
            max_index = cosines.index(max(cosines))
            C[max_index].append(i)
        print("length of C = ", len(C))
        print("no. of element in C = ", [len(clus) for clus in C])
    return C


def main():
    directory = "../processed_data/label/vec"
    X, Y = read_labeled(directory)
    # print(X)
    # print(Y)
    s_k_means(X, 7, 100)
main()
