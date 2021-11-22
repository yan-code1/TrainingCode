import pylab as plt
import os
import scipy.io as sio
allDict = ['packet_loss','data_latency','power']
def plot_one_mat(dirList):
    for matFile in dirList:
        mat = sio.loadmat(matFile + '/results.mat')
        figNum = 0
        for key in allDict:
            plt.figure(figNum)
            plt.xlabel('Time slot')
            plt.ylabel(key)
            plt.plot(mat[key].mean(axis=0))
            plt.grid(True, linestyle='-.')

            figNum += 1
            plt.title(matFile.split('/')[-1] + key)
            # plt.legend()
    plt.show()
def plot_all_mat(path):
    def getDirList(path):
        dqnList = []
        atpcList = []
        for dir in os.listdir(path):
            if dir.split('_')[0] == 'dqn':
                dqnList.append(os.path.join(path, dir))
            if dir.split('_')[0] == 'atpc':
                atpcList.append(os.path.join(path, dir))
            # dirList.append(os.path.join(path, dir))
        return [dqnList,atpcList]
    dirList=getDirList(path)
    print(dirList)
    for xxList in dirList:
        plot_one_mat(xxList)
plot_all_mat('./res/')
