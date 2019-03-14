"""with open("./img/wd=美女.html",encoding="utf-8") as fp:
    jpg_list = []
    # for line in HTMLText:
    lines = fp.readlines()
    print(type(lines))
    for line in lines:
        if line.find("<img src=")!= -1:
            if line.find(".jpg")!= -1:
                jpg_list.append(line)

    # jpg_list = file_name_jpg(fp.read())
    print(len(jpg_list))
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
    
if __name__ =="__main__":
    file_name_jpg(HTMLText)
