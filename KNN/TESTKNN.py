import time
import KNN
def main():
    # 获取程序运行时间
    start = time.clock()
    # 打开文件的名称
    filename = "./datingTestSet.txt"
    # 打开并处理数据
    datingDataMat, datingLabels = KNN.file2matrix(filename)
    # 训练集归一化
    normDataset, ranges, minVals = KNN.autoNorm(datingDataMat)
    KNN.datingClassTest()
    # print(normDataset)
    # print(ranges)
    # print(minVals)
    # showdatas(datingDataMat, datingLabels)
    KNN.classifyPerson()
    # print(datingDataMat)
    # print(datingLabels)
    # 创建数据集
    # group, labels = createDataSet()
    # 测试集
    # test = [100,100]
    # kNN分类
    # test_class = classify0(test, group, labels, 3)
    # 打印分类结果
    # print(test_class)
    end = time.clock()
    # 打印程序运行时间
    print('Running time: %f Seconds' % (end - start))


if __name__ == '__main__':
    main()