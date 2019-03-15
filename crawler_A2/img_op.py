"""
    传入html文本，查找全部图片文件，并返回列表
"""
"""
def file_name_jpg(HTMLText):
    jpg_list = []
    # lines = fp.readlines()
    for line in HTMLText:
        if line.find("<img src=")!= -1:
            if line.find(".jpg")!= -1:
                jpg_list.append(line)
    for i in jpg_list:
        # print(type(i))
        url = i.strip()
        urllist = url.split("<img src=")
        url = urllist[1]
        # print(url)
        urllist= url.split(".jpg")
        url = urllist[0]
        url = "https://" + url +".jpg"
        jpg_list.append(url)
        print(jpg_list)

    return jpg_list
"""
from bs4 import BeautifulSoup as bf
import lxml
import framework


def file_name_jpg(HTMLText, url):
    soup = bf(HTMLText, 'lxml')
    """ 
    imglist = soup.find_all('img')
    for i in imglist:
        print(i)
    """
    img_url_list = []
    #imglist = soup.find_all(attrs={"class":"pic"})
    imglist = soup.find_all(name="img")
    for i in imglist:
        # print(i.get("src"))
        img_url_list.append(i.get("src"))
    # 转集合去重
    img_url_list = list(set(img_url_list))
    # 反反爬：以故意缺失http和网站主名的形式反爬，对这部分进行补充
    for i in img_url_list:
        if i.find("http") == -1:
            # 假设i="/i/24101/70/resize/d24101-70-320114-0.jpg"
            # 转换成img_url="https://prtimes.jp/i/24101/70/resize/d24101-70-320114-0.jpg"
            # url = "https://prtimes.jp/main/html/rd/p/000000070.000024101.html"
            # img_url = url.split("/")[0] + "/" + url.split("/")[1] + "/" + url.split("/")[2] + "/" + i
            # img_url_list[img_url_list.index(i)] = img_url

            img_url = '/'.join(url.split("/")[:3]) + i
            img_url_list[img_url_list.index(i)] = img_url
        
    # 过滤器
    print("过滤前的项数：",len(img_url_list))
    re_list = img_url_list[:]
    # 过滤尾部无"."
    for i in img_url_list:
        if '.' not in i.split("/")[-1]:
            re_list.remove(i)
    img_url_list = re_list[:]
    # 过滤.jpg后无用信息
    for i in img_url_list:
        if ".jpg" in i.split("/")[-1]:
            new_i = "/".join(i.split("/")[:-1]) + "/" + i.split("/")[-1].split("?")[0]
            re_list[re_list.index(i)] = new_i
    img_url_list = re_list[:]
    print("过滤后的项数：",len(re_list))
    for i in re_list:
        print(i)
    # 过滤后的图片url列表img_url_list
    img_url_list = re_list[:]
    # 重名另指定
    lenth = len(re_list)
    for i in range(lenth-1):
        j = i+1
        while j<lenth:
            if re_list[j].split("/")[-1] in re_list[i]:
                re_list[j] = rename(re_list[j])
                print(re_list[i],"重名指定后：",re_list[j])
            j=j+1
    
    zip_list = zip(img_url_list, re_list)
    return zip_list

def rename(name):
    new_name = ''.join(name.split(".")[:-1]) + str(-1) + "." + name.split(".")[-1]
    return new_name

   
if __name__ =="__main__":
    url = "https://prtimes.jp/main/html/rd/p/000000070.000024101.html"
    with open("./web/000000070.000024101.html","r",encoding='utf-8') as fp:
        HTMLText = fp.read()
    zip_list = file_name_jpg(HTMLText, url)
    print("----------------")
    for i,j in list(zip_list):
        print(i,j)
    print("---*********----")
    for i,j in list(zip_list):
        print(j)
    print("================")
    print(list(zip_list))
        
