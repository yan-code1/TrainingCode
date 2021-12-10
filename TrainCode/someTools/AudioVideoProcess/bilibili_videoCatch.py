# encoding: utf-8
# create cookie.txt into which you need to put the link including BV number.
# single catch version
# usage: change the BV nubmer and header in this code and run, you can choose the quality of download video.
from lxml import etree
import requests
import os
# 获取视频名称
def name(bv,headers):
    url = 'https://www.bilibili.com/video/'+bv
    text = requests.get(url,headers = headers).text
    tree = etree.HTML(text)
    name = tree.xpath('//*[@id="viewbox_report"]/h1/span/text()')[0]
    return name
# 获取cid
def cid(bv,headers):
    url = 'https://api.bilibili.com/x/player/pagelist'
    param = {
        'bvid':'%s'%bv,
        'jsonp':'jsonp'
    }
    text = requests.get(url,params = param,headers = headers).json()
    cid = text['data'][0]['cid']
    return cid
# 获取视频url
def flv(cid,bv,headers,quality):
    url = 'https://api.bilibili.com/x/player/playurl'
    param = {
        'cid':'%s'%cid,
        'bvid':'%s'%bv,
        'qn':'%s'%quality,
    }
    text = requests.get(url,params = param,headers = headers).json()
    return text
# 请求视频并保存
def get_flv(name,flv_url,headers):
    print("\n等待响应数据（需要的时间较长）...")
    response = requests.get(flv_url,headers = headers)
    code = response.status_code
    print('\n响应码：',code)
    text = response.content
    if code == 200:
        with open("./%s.flv"%name,'wb') as fp1:
            fp1.write(text)
        with open("./list.txt",'a') as fp2:
            fp2.write(name+"\n"+bv+"\n\n")
        print("视频获取成功\n(若视频清晰度不符，请及时更新cookie值)")
    else:
        print("视频获取失败")
# main
bv = 'BV1TA411A7V6'#input("输入BV号：")
# 获取本地txt保存的cookie
cookie = ""
if os.path.exists("./cookie.txt"):
    with open('./cookie.txt') as fp:
        cookie = fp.read()
    cookie = cookie.split('\n')[0]
print('\ncookie:',cookie)
headers = {
    'Referer':'https://www.bilibili.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'cookie':"%s"%cookie,
}
cid = cid(bv,headers)
print('\n可获取cookie值的链接(需先在浏览器正常登录)\nhttps://api.bilibili.com/x/player/playurl?cid=%s&bvid=%s'%(cid,bv))
name = name(bv,headers)
print('\n标题：',name)
print('\ncid:',cid)
quality = ''
text =flv(cid,bv,headers,quality)
qn = text['data']['support_formats']
print("\n可选择的清晰度(部分清晰度可能获取失败)：")
for qu in qn:
    print(('清晰度：%s'%qu['new_description']).ljust(15)+('视频质量参数:%d'%qu['quality']).ljust(15)+('格式参数:%s'%qu['format']).ljust(15))
quality = input("输入清晰度对应的视频质量参数（默认1080p）：")
if quality == '':
    quality = '80'
text = flv(cid,bv,headers,quality)
flv_url = text['data']['durl'][0]['url']
print('\nflv_url:',flv_url)
get_flv(name,flv_url,headers)
