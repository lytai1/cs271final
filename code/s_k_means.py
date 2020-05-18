import os
import numpy as np
import math as m
import random

def read_labeled(directory):
    X = []
    Y = []
    X_test = []
    Y_test = []
    i = 0
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            fileName = os.path.join(root + "/", name)
            f = open(fileName)
            no_sample = 0
            for x in f:
                data = x.split(",")
                data = [float(n) for n in data[:-1]]
                if no_sample<800:
                    X.append(np.array(data))
                    Y.append(i)
                else:
                    X_test.append(np.array(data))
                    Y_test.append(i)
                no_sample += 1
            i += 1
    return np.array(X), np.array(Y), np.array(X_test), np.array(Y_test)
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

def s_k_means_super(X, X_test, k, origin_C, iterations):
    #initialization
    n = len(X_test)
    X_norm = [v / np.linalg.norm(v) for v in X]
    X_test_norm = [v / np.linalg.norm(v) for v in X_test]
    indices = [i for i in range(n)]
    random.shuffle(indices)
    slice_length = m.ceil(len(indices)/k)
    C = [indices[i:i+slice_length] for i in range(0, len(indices), slice_length)]
 
    for z in range(iterations):
        c = []
        for j in range(k):
            # calculate for centroid
            cluster = [X_test_norm[i] for i in C[j]] + [X_norm[i] for i in origin_C[j]]
            centroid = cluster[0]
            for point in cluster[1:]:
                centroid += point
            c.append(centroid / np.linalg.norm(centroid))
        C = [[] for _ in range(k)]
        for i in range(n):
            cosines = []
            for l in range(k):
                cosine = np.dot(c[l], X_test_norm[i])/(np.linalg.norm(c[l])*np.linalg.norm(X_test_norm[i]))
                cosines.append(cosine)
            max_index = cosines.index(max(cosines))
            C[max_index].append(i)
        print("length of C = ", len(C))
        print("no. of element in C = ", [len(clus) for clus in C])
    return C

def accuracy(C, Y_test):
    a = 0
    total = len(Y_test)
    for i in range(len(Y_test)):
        if i in C[Y_test[i]]:
            a += 1
    print("no. of accurate = ", a)
    print("total = ", total)
    return a/total

def train(X, Y):
    set_Y = set(Y)
    n = max(set_Y) + 1
    C = [[] for _ in range(n)]
    for i in range(len(X)):
        C[Y[i]].append(i)
    return C


def main():
    directory = "../processed_data/vec"
    X, Y , X_test, Y_test= read_labeled(directory)
    print("length of X = ", len(X))
    print("length of Y = ", len(Y))
    print("length of X test = ", len(X_test))
    print("length of Y test = ", len(Y_test))
    # C = s_k_means(X, 7, 10)
    print("train with w2v")
    train_C = train(X, Y)
    C = s_k_means_super(X, X_test, 7, train_C, 30)
    a = accuracy(C, Y_test)
    print("accuracy = ", a)

    directory = "../processed_data/label"
    X, Y , X_test, Y_test= read_labeled(directory)
    print("length of X = ", len(X))
    print("length of Y = ", len(Y))
    print("length of X test = ", len(X_test))
    print("length of Y test = ", len(Y_test))
    # C = s_k_means(X, 7, 10)
    print("train with byte feature")
    train_C = train(X, Y)
    C = s_k_means_super(X, X_test, 7, train_C, 30)
    a = accuracy(C, Y_test)
    print("accuracy = ", a)

main()
