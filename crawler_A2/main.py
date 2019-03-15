import framework
import file_op
import img_op


# URL = "http://www.win4000.com/meitu.html"
URL = "https://mdpr.jp/news/detail/1720270"
"""
# URL = "https://www.baidu.com/s?wd="
# params = input("请输入你想要查找的内容:")
URL = URL +params
"""
# kv = {"wd":"python"}

if __name__ == "__main__":
    # if framework.getHTMLText(URL) != "产生异常":
    # print(framework.getHTMLText(URL))
    # file_op.write_in_file(framework.getHTMLText(URL), URL, "w")
    # getHTMLText返回网页的html，解析出图片格式
    # framework.getHTMLText(URL)
    
    #搜索网址
    HTMLText = framework.getHTMLText(URL).text
    file_op.write_in_file(HTMLText, URL, "w", path="./web/")
    #print(HTMLText)
    #识别出图片url链接
    zip_list = img_op.file_name_jpg(HTMLText, URL)
    path = "./img/"+ URL.split("/")[2] +"/"
    #链接提交给get请求
    for img_url,img_name in list(zip_list):
        #try:
        file_op.write_in_file(framework.getHTMLText(img_url).content, img_name, write_type="wb",path=path ,file_class=".jpg")
        #except Error as E:
        #    print(E)
        #    print("文件"+img_url+"写入失败")
        
    #下载图片数据，二进制存入文件

     
