import requests
import json
import time
import pymongo

URL = 'http://m.weibo.cn/container/getIndex'
COOKIE = '_T_WM=ca68525b08d761cdd867311856eb8265; SUB=_2A251vs_2DeRxGeBP61cY9i_OzziIHXVXQNG-rDV6PUJbkdBeLWn3kW0XN-bfAMTjYLdlkD7_Bz81YkdWyQ..; SUHB=0YhhA-OgV30Ig3; SCF=As5lSygKY9mP0i5xHEK7yUN-moCtlwfnpDvtaxnBbyxos-RTOiO2FXq3Cf9q0bWF8GBHpzb1kob7rFEy_cKW-TM.; SSOLoginState=1488633767; H5_INDEX=0_all; H5_INDEX_TITLE=%E5%87%8C%E6%99%B4%E6%B7%8C%E5%A4%A9%E8%8F%B1; M_WEIBOCN_PARAMS=luicode%3D20000174%26lfid%3D1005051002861732%26fid%3D1005051002861732%26uicode%3D10000011'
HEADERS = {
        'Cookie': COOKIE,
        'Host': 'm.weibo.cn',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
UID = '5907193262'

def get_userinfo(uid):
    containerid = '100505' + uid
    payload = {
        'type':'uid',
        'value':uid,
        'containerid' :containerid
    }

    userinfo = requests.get(URL,params=payload,headers=HEADERS)
    info = json.loads(userinfo.content)
    print(info.get("userInfo"))

def get_fans(uid,page):
    containerid = '231051_-_fans_-_' +uid
    lfid = '100505'+uid
    payload = {
        'containerid': containerid,
        'luicode': '10000011',
        'lfid': lfid,
        'page':page
    }
    userfans = requests.get(URL, params=payload, headers=HEADERS)
    fans = json.loads(userfans.content)
    newpage = fans.get('cardlistInfo')['page']
    if newpage is not None:
        print(fans.get('cards'))
        time.sleep(3)
        get_fans(UID, newpage)

def get_followers(uid,page):
    containerid = '231051_-_followers_-_' +uid
    lfid = '100505'+uid
    payload = {
        'containerid': containerid,
        'luicode': '10000011',
        'lfid': lfid,
        'page':page
    }
    userfollowers = requests.get(URL, params=payload, headers=HEADERS)
    followers = json.loads(userfollowers.content)

    newpage = followers.get('cardlistInfo')['page']
    if newpage is not None:
        print(followers.get('cards'))
        time.sleep(3)
        get_followers(UID,newpage)


def get_tweets(uid,page):
    containerid = '107603' + uid
    payload = {
        'type': 'uid',
        'value': uid,
        'containerid': containerid,
        'page':page
    }

    usertweets = requests.get(URL, params=payload, headers=HEADERS)
    tweets = json.loads(usertweets.content)


    newpage = tweets.get('cardlistInfo')['page']

    if newpage is not None:
        print(tweets.get('cards'))
        time.sleep(3)
        get_tweets(UID,newpage)

get_userinfo(UID)
get_tweets(UID,"")
get_fans(UID,"")
get_followers(UID,"")
