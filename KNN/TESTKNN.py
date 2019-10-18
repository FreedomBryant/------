import KNN
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data,labels = KNN.creatDataSet()
    print(KNN.classify0([1,2],data,labels,3))
    # print(data)
    # x = data[:,0]
    # y = data[:,1]
    # print(x,y)
    # plt.scatter(x,y,c = 'r',alpha=0.5,marker="x")
    # plt.scatter(1,2,c = 'b',alpha=0.5,marker="o")
    # plt.xlabel("X")
    # plt.ylabel("Y")
    # plt.title("movies")
    # for i in range(len(x)):
    #     plt.annotate(i,(x[i],y[i]))
    # plt.show()