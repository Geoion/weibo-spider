import requests
import json
import time
from pymongo import MongoClient

URL = 'http://m.weibo.cn/container/getIndex'
COOKIE = '_T_WM=37233bf9db6006a2f6d1d2c4305bed2b; SCF=AqK2Zs1pbHWJxHPun4b8FKuPr5mzDuIuMmEdPPNmZLAELusGwNYQlhvxXZbd6YgnvvFplSt-1nlzrL45oo2sF1w.; SUB=_2A251wEBwDeRxGeBP61cY9i_KzTyIHXVXS2A4rDV6PUJbkdBeLRfDkW2fixjv8YQuL8DQ_grfUdOhLlB63Q..; SUHB=0LcSMGyJGCLyKh; SSOLoginState=1489252384; M_WEIBOCN_PARAMS=luicode%3D20000174%26lfid%3D1005051990309453%26fid%3D1005051990309453%26uicode%3D10000011'
HEADERS = {
        'Cookie': COOKIE,
        'Host': 'm.weibo.cn',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
UID = '1867853927'

def get_db():
    client = MongoClient('localhost', 27017)
    db = client.weibo
    print("连接数据库")
    return db


def get_userinfo(uid):
    userinfo = requests.get("http://m.weibo.cn/container/getIndex?type=uid&value="+uid+"&containerid=100505"+uid,headers=HEADERS)
    info = json.loads(userinfo.content).get("userInfo")
    print(info)

    post= {"_id":uid,
            "screen_name": info["screen_name"],
            "description": info["description"],
            "follow_count": info["follow_count"],
            "followers_count": info["followers_count"],
            "statuses_count": info["statuses_count"]
    }

    collection = db.userInfo
    collection.insert(post)

def get_fans(uid,page):
    userfans = requests.get("http://m.weibo.cn/container/getIndex?containerid=231051_-_fans_-_"+uid+"&luicode=10000011&lfid=100505"+uid+"&featurecode=20000180&page="+str(page), headers=HEADERS)
    fans = json.loads(userfans.content)
    newpage = fans.get('cardlistInfo')['page']
    if newpage is not None:
        print(fans.get('cards'))
        time.sleep(3)
        get_fans(UID, newpage)

def get_followers(uid,page):

    userfollowers = requests.get("http://m.weibo.cn/container/getIndex?containerid=231051_-_followers_-_"+uid+"&luicode=10000011&lfid=100505"+uid+"&featurecode=20000180&page="+str(page), headers=HEADERS)
    followers = json.loads(userfollowers.content)

    newpage = followers.get('cardlistInfo')['page']
    if newpage is not None:
        print(followers.get('cards'))
        time.sleep(3)
        get_followers(UID,newpage)

def get_tweets(uid,page):

    usertweets = requests.get("http://m.weibo.cn/container/getIndex?type=uid&value="+uid+"&containerid=107603"+uid+"&page="+str(page), headers=HEADERS)
    tweets = json.loads(usertweets.content)


    newpage = tweets.get('cardlistInfo')['page']

    if newpage is not None:
        print(tweets.get('cards'))
        time.sleep(3)
        get_tweets(UID,newpage)

def get_comments(tid):
    page = 1
    usercomments = requests.get("http://m.weibo.cn/api/comments/show?id=" + tid + "&page="+ str(page), headers= HEADERS)
    comments = json.loads(usercomments.content)
    print(comments.get('data'))

    maxpage = comments.get('max')

    if page < maxpage:
        get_comments(tid, page+1)

def get_reposttimeline(tid):
    page = 1
    usercomments = requests.get("http://m.weibo.cn/api/statuses/repostTimeline?id=" + tid + "&page=" + str(page), headers=HEADERS)
    comments = json.loads(usercomments.content)
    #print(comments.get('data'))

    maxpage = comments.get('max')

    for pages in range(1,maxpage+1):
        #yield  get_reposttimeline()
        usercomments = requests.get("http://m.weibo.cn/api/statuses/repostTimeline?id=" + tid + "&page=" + str(pages), headers=HEADERS)
        comments = usercomments.json()
        # if hasattr(comments, "data"):
        #     print(comments.get('data'))
        print(comments.get('data'))

db = get_db()

#get_userinfo(UID)
get_tweets(UID,"")
#get_fans(UID,"")
#get_followers(UID,"")
#get_reposttimeline("4084099851139166")

#get_comments("4085333429917678")


