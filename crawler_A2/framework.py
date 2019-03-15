import requests
import file_op

def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()  #如果状态码不是200，触发HTTPError异常
        r.encoding = r.apparent_encoding
        return r
    except:
        return "产生异常"


if __name__ == "__main__":
    url = "http://www.win4000.com/meitu.html"
    print(getHTMLText(url))
    HTMLText = getHTMLText(url)
    file_op.write_in_file(HTMLText)

