import os 
allDict = ['packet_loss']
def plot_all_mat(path):
    def getDirList(path):
        dirList = []
        for dir in os.listdir(path):
            dirList.append(os.path.join(path, dir))
        return dirList
    import scipy.io as sio
    dirList=getDirList(path)
    for matFile in dirList:
        mat = sio.loadmat(matFile+'/result.mat')
        figNum = 0
        for key in allDict:
            plt.figure(figNum)
            plt.xlabel('Time slot')
            plt.ylabel(key)
            plt.plot(mat[key].mean(axis=0))
            plt.grid(True, linestyle='-.')
            figNum+=1
            plt.title(matFile.split('/')[-1]+key)
            plt.show()
