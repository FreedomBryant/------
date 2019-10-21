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

def file2matrix(filename):
    # 打开文件
    fr = open("./datingTestSet.txt")
    # 读取文件的所有内容
    arrayOLines = fr.readlines()
    print(arrayOLines)
    # 得到文件行数
    numberOfLines = len(arrayOLines)
    # 返回的Numpy矩阵numberOfLines行，3列
    returnMat = np.zeros((numberOfLines, 3))
    # 创建分类标签向量
    classLabelVector = []
    # 行的索引值
    index = 0
    # 读取每一行
    for line in arrayOLines:
        # 去掉每一行首尾的空白符，例如'\n','\r','\t',' '
        line = line.strip()
        # 将每一行内容根据'\t' 符进行切片，本例中一共有4列
        listFromLine = line.split('\t')
        # 将数据的前3列进行提取保存在returnMat矩阵中，也就是特征矩阵
        returnMat[index, :] = listFromLine[0:3]
        # 根据文本内容进行分类1：不喜欢 2：一般 3：喜欢
        if listFromLine[-1] == 'didntLike':
            classLabelVector.append(1)
        elif listFromLine[-1] == 'smallDoses':
            classLabelVector.append(2)
        elif listFromLine[-1] == 'largeDoses':
            classLabelVector.append(3)
        index += 1
    # 返回标签列向量以及特征矩阵
    return returnMat,classLabelVector
