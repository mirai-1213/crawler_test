import os

DIR_NAME = "./"


def write_in_file(info, url="autoUrl.html",write_type='w', path=DIR_NAME, file_class=".txt"):
    count = 0
    if url == "autoUrl.html":
        file_name = "autoUrl.html"
    else:
        file_name = url_option(url, path)
    print(type(info))
    try:
        if 'b' not in write_type:
            fp = open(file_name, write_type,encoding="utf-8")
        else:
            fp = open(file_name, write_type)
        fp.write(info)
        print("succeed")
        fp.close()
        return 1
    except FileNotFoundError as E:
        print(E)
        mkdir(path)
        write_in_file(info, url, write_type)
        return 0
    except OSError as E:
        print(file_name+"OSError")
        print(E)
        return -1
    except:
        print("other error!")
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
def url_option(url,path):

    file_name = path + url.split('/')[-1]
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
 
