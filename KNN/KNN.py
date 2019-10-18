import numpy as np
def creatDataSet():
    group = np.array([[1,1.1],[1,1],[0,0],[0,0.1]])
    labels = ['爱情片','爱情片','动作片','动作片']
    return group,labels

def classify0(inX,dataSet,labels,k):
    #距离计算
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    print(sqDiffMat)
    sqDistances = sqDiffMat.sum(axis = 1)
    print(sqDistances)
    distances = sqDistances**0.5
    print(distances)
    #返回排序索引值
    sortedDistIndicies = distances.argsort()
    print(sortedDistIndicies)
    # 定义一个记录类别次数的字典
    classCount = {}
    # 选择距离最小的k个点
    for i in range(k):
        # 取出前k个元素的类别
        voteIlabel = labels[sortedDistIndicies[i]]
        # 字典的get()方法，返回指定键的值，如果值不在字典中返回0
        # 计算类别次数
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    print(classCount)
    # python3中用items()替换python2中的iteritems()
    # key = operator.itemgetter(1)根据字典的值进行排序
    # key = operator.itemgetter(0)根据字典的键进行排序
    # reverse降序排序字典
    sortedClassCount = sorted(classCount.items(),
                              key=lambda x : x[1], reverse=True)
    # 返回次数最多的类别，即所要分类的类别
    print(sortedClassCount)
    return sortedClassCount[0][0]

