import framework
import file_op
import img_op


URL = "https://www.baidu.com/s?wd="
# kv = {"wd":"python"}
params = input("请输入你想要查找的内容:")
URL = URL +params

if __name__ == "__main__":
    # if framework.getHTMLText(URL) != "产生异常":
    # print(framework.getHTMLText(URL))
    # file_op.write_in_file(framework.getHTMLText(URL), URL, "w")
    # getHTMLText返回网页的html，解析出图片格式
    # framework.getHTMLText(URL)
    
    #搜索网址
    HTMLText = framework.getHTMLText(URL)
    print(HTMLText)
    #识别出图片url链接
    img_op.file_name_jpg(HTMLText)
    #链接提交给get请求
    
    #下载图片数据，二进制存入文件
