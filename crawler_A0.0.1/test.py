# URL = "https://www.baidu.com/s?wd="
# 存储文件名为wdxxxx.html

def url_option(url):
    # 按 /s? 分割
    urllist = url.split('s?wd=')
    url = "wd=" + urllist[-1]
    # 取最后一段字节,生成.html的file_name
    file_name = "./web/"+url+".html"
    return file_name

