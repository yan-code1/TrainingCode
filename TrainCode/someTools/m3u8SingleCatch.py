import datetime
import threading

import requests
import os
import time

# Python的urllib3软件包的证书认证及警告的禁用
import urllib3
urllib3.disable_warnings()

# 增加重试连接次数
requests.DEFAULT_RETRIES = 5

kwargs = {
    # m3u8是本地的文件路径
    'm3u8_path' : "./media_3.m3u8",
    # request请求头，若无可能被禁止访问
    'header'    : {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"},
    # 文件后缀名'.m4s' or '.ts'
    'fileEnd'       : ".m4s",
    # 下载链接的前序
    'base_url'  :'https://01.cdn.yoda.slideslive.com/O3J6ABPLSrav/',
    # 分片保存路径
    'download_path':'./download_path/',
    'combine_path' :'./combine_path/',
    'out_name' :'out',

}
class m3u8Download():
    def __init__(self,**kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.urls = []
    # 从m3u8文件中取出并生成ts文件的下载链接
    def get_urls(self,tag = 'video' ):
        NO_INIT = True
        with open(self.m3u8_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                # get initial file, for example: #EXT-X-MAP:URI="init_0_2500000.m4s"
                if NO_INIT and 'init' in line :
                    self.urls.append(self.base_url + line.split('"')[-2])
                if line.endswith(self.fileEnd+"\n"):
                    self.urls.append(self.base_url + line.strip("\n"))
        return self.urls

    def downloadThread(self,i):
        url = self.urls[i]
        print(url)
        file_name = url.split("/")[-1]
        video_path = self.download_path + "/{}".format(i) + self.fileEnd
        if not os.path.exists(video_path):
            # print("url", url)
            print("开始下载 %s" % file_name)
            time.sleep(0.1)  # 防止爬虫间隔时间过短被禁止请求
            start = datetime.datetime.now().replace(microsecond=0)
            try:
                response = requests.get(headers=self.header, url=url, stream=True, verify=False)
                # 关闭多余的连接
                response.keep_alive = False
            except Exception as e:
                print("异常请求：%s" % e)
                return

            with open(video_path, "wb+") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)

            end = datetime.datetime.now().replace(microsecond=0)
            # print("耗时：%s" % (end - start))
        else:
            print("{} 已经存在，开始下载下一个分片".format(file_name))
    def mutiDownload(self):
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)
        Threads = []
        for i in range(len(self.urls)):
            t = threading.Thread(target=self.downloadThread,args=(i,))
            time.sleep(0.1)
            Threads.append(t)
            t.start()

        # waiting
        for t in Threads:
            t.join()
        print('所有分片下载完毕')
    # 取出下载链接并下载
    def download(self):
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)
        for i in range(len(self.urls)):

            url = self.urls[i]
            file_name = url.split("/")[-1]
            video_path = self.download_path +"/{}".format(i) + self.fileEnd
            if not os.path.exists(video_path):
                print("url", url)
                print("开始下载 %s" % file_name)
                time.sleep(0.1)  # 防止爬虫间隔时间过短被禁止请求
                start = datetime.datetime.now().replace(microsecond=0)
                try:
                    response = requests.get(headers=self.header, url=url, stream=True, verify=False)
                except Exception as e:
                    print("异常请求：%s" % e.args)
                    return

                with open(video_path, "wb+") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)

                end = datetime.datetime.now().replace(microsecond=0)
                print("耗时：%s" % (end - start))
            else:
                print("{} 已经存在，开始下载下一个ts".format(file_name))
                continue


    # 将已经下载的文件的路径进行排序
    def file_walker(self):
        file_list = []
        for root, dirs, files in os.walk(self.download_path):  # 生成器
            for fn in files:
                p = str(root + '/' + fn)
                file_list.append(p)
        file_list.sort(key=lambda x: int(x.split('/')[-1].split('.')[0].split('_')[-1]))
        print(file_list)
        return file_list

    def toMp4(self,video_name):
        # print(video_path)
        os.system("ffmpeg -i " + video_name+" -codec copy " + self.combine_path + "out.mp4")
        print("视频 {}.mp4 转换成功".format(video_name))
    # 将所有下载好的分片文件组合成一个文件
    # video_path: 下载好的一堆分片文件的文件夹
    # combine_path: 组合好的文件的存放位置
    # file_name: 组合好的视频文件的文件名

    def combine(self):
        if not os.path.exists(self.combine_path):
            os.makedirs(self.combine_path)
        file_list = self.file_walker()
        # print(file_list)
        file_path = self.combine_path +self.out_name+ self.fileEnd
        with open(file_path, 'wb+') as fw:
            for i in range(len(file_list)):
                fw.write(open(file_list[i], 'rb').read())
        self.toMp4(self.combine_path +self.out_name)
        return file_path


if __name__ == '__main__':
    m3u8 = m3u8Download(**kwargs)

    m3u8.get_urls()
    m3u8.mutiDownload()
    m3u8.file_walker()
    m3u8.combine()
    m3u8.toMp4()
