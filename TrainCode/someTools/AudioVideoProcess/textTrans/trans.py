import json
import urllib.request
import urllib.parse
from HandleJs import Py4Js


def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    return data


def buildUrl(content, tk, tl):
    baseUrl = 'http://translate.google.cn/translate_a/single'
    baseUrl += '?client=t&'
    baseUrl += 'sl=auto&'
    baseUrl += 'tl=' + str(tl) + '&'
    baseUrl += 'hl=zh-CN&'
    baseUrl += 'dt=at&'
    baseUrl += 'dt=bd&'
    baseUrl += 'dt=ex&'
    baseUrl += 'dt=ld&'
    baseUrl += 'dt=md&'
    baseUrl += 'dt=qca&'
    baseUrl += 'dt=rw&'
    baseUrl += 'dt=rm&'
    baseUrl += 'dt=ss&'
    baseUrl += 'dt=t&'
    baseUrl += 'ie=UTF-8&'
    baseUrl += 'oe=UTF-8&'
    baseUrl += 'clearbtn=1&'
    baseUrl += 'otf=1&'
    baseUrl += 'pc=1&'
    baseUrl += 'srcrom=0&'
    baseUrl += 'ssel=0&'
    baseUrl += 'tsel=0&'
    baseUrl += 'kc=2&'
    baseUrl += 'tk=' + str(tk) + '&'
    baseUrl += 'q=' + content
    return baseUrl


def translate(data, tk, tl):
    # content是要翻译的内容
    content = urllib.parse.quote(data[1])
    url = buildUrl(content, tk, tl)

    result = open_url(url)
    res_json = json.loads(result)
    trans_text = res_json[0][0][0]
    # 去除读取文字中前后的换行符和逗号及单引号或双引号
    original = data[1].strip("\n").strip(",").strip("'").strip('"')
    translate = trans_text.strip(",").strip("'").strip('"')
    print(original + " : " + translate)
    result = data[0] + ": " + trans_text + "\n"
    # 保存翻译后的内容到文件中
    with open('./test.zh.js', 'a', encoding='utf-8') as f:
        f.write(result)


def main():
    js = Py4Js()
    # tl是要翻译的目标语种，值参照ISO 639-1标准，如果翻译成中文"zh/zh-CN简体中文"
    tl = "zh"
    # 读取需要翻译的文件
    with open('text.en.js', encoding="utf-8") as file_obj:
        for line in file_obj:
            data = line.split(":", 1)
            if len(data) == 2:
                tk = js.getTk(data[1])
                translate(data, tk, tl)
            else:
                print("Illegal row data")


if __name__ == "__main__":
    main()