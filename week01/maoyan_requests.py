# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
import re
# bs4是第三方库需要使用pip命令安装


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'

cookie ='__mta=188530583.1593047225871.1593185358494.1593225778640.11; uuid_n_v=v1; uuid=2EC17180B68011EAAD7CEBC74F78E0F9DD26B3CEC01F4F87ABC6F58DECAC0426; _lxsdk_cuid=172e9039597c8-069e4aca47e822-4353761-1fa400-172e9039598c8; _lxsdk=2EC17180B68011EAAD7CEBC74F78E0F9DD26B3CEC01F4F87ABC6F58DECAC0426; mojo-uuid=42130ff45299550fcbc6964c316387d7; _csrf=9e18975dcc9dd6fc22535a95d46c15dc67f863c84ac51c418f079403c548c046; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593047226,1593075023; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=188530583.1593047225871.1593178154867.1593178227507.9; mojo-session-id={"id":"e131db068734a8d1cf2a6f40e1e6d7ca","time":1593225778472}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593225779; _lxsdk_s=172f3a7b7cb-2ac-680-042%7C%7C3'

header = {'user-agent':user_agent,'Cookie':cookie}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')
#print(bs_info)

link_list = []
#考虑以字典的形式组装所有的电影形式，电影名称、类型、日期以列表的形式获取
movie_dict = {}
movie_name_list = []
movie_type_list = []
movie_date_list= []
# 获取top10电影的链接
tags_temp = bs_info.find_all('div', attrs={'class': 'movie-item film-channel'})
for tags in tags_temp[0:10]:
    for atag in tags.find_all('a',):
        link_temp = "https://maoyan.com" + atag.get('href')
        
        if link_temp not in link_list:
            link_list.append(link_temp)

#        movie_name_list.append(atag.get('title'))

#        print(atag.get('href'))
        # 获取所有链接
#        print(atag.get('title'))
#        print(atag.find('span',).text)
        # 获取电影名字

#遍历top10的电影链接，取出上映时间和电影类型
for link_temp in link_list:
    response_temp  = requests.get(link_temp,headers=header)
    bs_info_temp = bs(response_temp.text, 'html.parser')
    tags_temp = bs_info_temp.find_all('div', attrs={'class': 'movie-brief-container'})
#    print(tags_temp)
    li_temp = tags_temp[0].find_all('li', attrs={'class': 'ellipsis'})
    
    
    movie_name_temp = tags_temp[0].find_all('h1')
    movie_name_list.append(movie_name_temp[0].text)
    
#    print(li_temp)
    movie_date = li_temp[-1].text
    movie_date = re.search(r'(\S+\d)',movie_date).group()
    movie_date_list.append(movie_date)
    print("上映时间%s" % movie_date)
    movie_type = ""
    for atag_temp in tags_temp[0].find_all('a',):
        movie_type_temp = atag_temp.text.strip()
        if movie_type == "":
            movie_type = movie_type_temp
        else:
            movie_type = movie_type + "," + movie_type_temp
    movie_type_list.append(movie_type)
    print("电影类型%s" % movie_type)

import pandas as pd
#将电影名称、类型、日期列表组装在字典里
movie_dict['name'] = movie_name_list
movie_dict['type'] = movie_type_list
movie_dict['date'] = movie_date_list

print(movie_dict)

movie_maoyan_req = pd.DataFrame(movie_dict,columns=['name','type','date'])
movie_maoyan_req.to_csv('./movie_maoyan_req.csv', encoding='gbk', index=False, header=False)




    





