import os

DIR_NAME = "./img"


def write_in_file(info, url="autoUrl.html",write_type='w'):
    file_name = url_option(url)
    try:
        with open(file_name, write_type,encoding="utf-8") as fp:
            fp.write(info)
            return 1
    except FileNotFoundError:
        mkdir(DIR_NAME)
        write_in_file(info, url, write_type)
        return 0
    except OSError as E:
        print(E)
        return -1

"""def load_from_file():
    try:
        # 文件存在
        fp = open("usr_info", 'r+')
        user = eval(fp.read())
        write_type = 'a'
        # 写入方式以“a”（追加写入）进行
        if user.get("admin") is None:
            user.update({"admin": "admin"})
            write_in_file(user,write_type)
    except OSError:
        # 文件不存在，系统错误
        user.update({"admin": "admin"})
        write_in_file(user)
        return user
    user = eval(fp.read())
    fp.close()
    return user
"""
def url_option(url):
    # 按 /s? 分割
    urllist = url.split('s?wd=')
    url = "wd=" + urllist[-1]
    # 取最后一段字节,生成.html的file_name
    file_name = DIR_NAME + '/' + url + ".html"
    return file_name

    
def mkdir(path): 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        os.makedirs(path) 
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False
 
