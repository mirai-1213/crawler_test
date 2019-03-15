img_url_list=["https://graph.facebook.com/1593325340766739/picture?width=43&height=43","https://graph.facebook.com/10218577738420885/picture?width=43&height=43"]


print("过滤前的项数：",len(img_url_list))
re_liet = img_url_list[:]
for i in img_url_list:
    if '.' not in i.split("/")[-1]:
        re_liet.remove(i)
print("过滤后的项数：",len(re_liet))
for i in re_liet:
    print(i)


