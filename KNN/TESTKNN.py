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

    datingDataMat, datingLabels = KNN.file2matrix("./datingTestSet")
    #设置汉字格式
    font = FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=14)
    #将figure画布分隔成1行1列，不共享x轴和y轴，fig画布的大小为（13，8）
    # 当nrows=2，ncols=2时，代表fig画布被分为4个区域，axs[0][0]代表第一行第一个区域
    fig,axs = plt.subplots(nrows = 2,ncols = 2,sharex = False,sharey = False,figsize = (13,8))
    #获取datingLabels 的行数作为label的个数
    #numberOfLabels = len(datingLabels)
    #label 的颜色配置矩阵
    LabelsColors = []
    for i in datingLabels:
        #didntLike
        if i == 1:
            LabelsColors.append('black')
        #smallDoses
        if i == 2:
            LabelsColors.append('orange')
        # largeDoses
        if i == 3:
            LabelsColors.append('orange')
        # 画出散点图，以datingDataMat矩阵第一列为x，第二列为y，散点大小为15, 透明度为0.5
        axs[0][0].scatter(x=datingDataMat[:, 0], y=datingDataMat[:, 1], color=LabelsColors, s=15, alpha=.5)
        # 设置标题，x轴label， y轴label
        axs0_title_text = axs[0][0].set_title(u'每年获得的飞行常客里程数与玩视频游戏所消耗时间占比', FontProperties=font)
        axs0_xlabel_text = axs[0][0].set_xlabel(u'每年获得的飞行常客里程数', FontProperties=font)
        axs0_ylabel_text = axs[0][0].set_ylabel(u'玩视频游戏所消耗时间占比', FontProperties=font)
        plt.setp(axs0_title_text, size=9, weight='bold', color='red')
        plt.setp(axs0_xlabel_text, size=7, weight='bold', color='black')
        plt.setp(axs0_ylabel_text, size=7, weight='bold', color='black')
        # 画出散点图，以datingDataMat矩阵第一列为x，第三列为y，散点大小为15, 透明度为0.5
        axs[0][1].scatter(x=datingDataMat[:, 0], y=datingDataMat[:, 2], color=LabelsColors, s=15, alpha=.5)
        # 设置标题，x轴label， y轴label
        axs1_title_text = axs[0][1].set_title(u'每年获得的飞行常客里程数与每周消费的冰淇淋公升数', FontProperties=font)
        axs1_xlabel_text = axs[0][1].set_xlabel(u'每年获得的飞行常客里程数', FontProperties=font)
        axs1_ylabel_text = axs[0][1].set_ylabel(u'每周消费的冰淇淋公升数', FontProperties=font)
        plt.setp(axs1_title_text, size=9, weight='bold', color='red')
        plt.setp(axs1_xlabel_text, size=7, weight='bold', color='black')
        plt.setp(axs1_ylabel_text, size=7, weight='bold', color='black')
        # 画出散点图，以datingDataMat矩阵第二列为x，第三列为y，散点大小为15, 透明度为0.5
        axs[1][0].scatter(x=datingDataMat[:, 1], y=datingDataMat[:, 2], color=LabelsColors, s=15, alpha=.5)
        # 设置标题，x轴label， y轴label
        axs2_title_text = axs[1][0].set_title(u'玩视频游戏所消耗时间占比与每周消费的冰淇淋公升数', FontProperties=font)
        axs2_xlabel_text = axs[1][0].set_xlabel(u'玩视频游戏所消耗时间占比', FontProperties=font)
        axs2_ylabel_text = axs[1][0].set_ylabel(u'每周消费的冰淇淋公升数', FontProperties=font)
        plt.setp(axs2_title_text, size=9, weight='bold', color='red')
        plt.setp(axs2_xlabel_text, size=7, weight='bold', color='black')
        plt.setp(axs2_ylabel_text, size=7, weight='bold', color='black')
        # 设置图例
        didntLike = mlines.Line2D([], [], color='black', marker='.', markersize=6, label='didntLike')
        smallDoses = mlines.Line2D([], [], color='orange', marker='.', markersize=6, label='smallDoses')
        largeDoses = mlines.Line2D([], [], color='red', marker='.', markersize=6, label='largeDoses')
        # 添加图例
        axs[0][0].legend(handles=[didntLike, smallDoses, largeDoses])
        axs[0][1].legend(handles=[didntLike, smallDoses, largeDoses])
        axs[1][0].legend(handles=[didntLike, smallDoses, largeDoses])
        # 显示图片
        plt.show()