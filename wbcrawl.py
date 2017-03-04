import requests
import json

url = 'http://m.weibo.cn/container/getIndex?uid=1002861732&luicode=20000174&type=uid&value=1002861732&containerid=1076031002861732'
cookie = '_T_WM=ca68525b08d761cdd867311856eb8265; SUB=_2A251vs_2DeRxGeBP61cY9i_OzziIHXVXQNG-rDV6PUJbkdBeLWn3kW0XN-bfAMTjYLdlkD7_Bz81YkdWyQ..; SUHB=0YhhA-OgV30Ig3; SCF=As5lSygKY9mP0i5xHEK7yUN-moCtlwfnpDvtaxnBbyxos-RTOiO2FXq3Cf9q0bWF8GBHpzb1kob7rFEy_cKW-TM.; SSOLoginState=1488633767; H5_INDEX=0_all; H5_INDEX_TITLE=%E5%87%8C%E6%99%B4%E6%B7%8C%E5%A4%A9%E8%8F%B1; M_WEIBOCN_PARAMS=luicode%3D20000174%26lfid%3D1005051002861732%26fid%3D1005051002861732%26uicode%3D10000011'

headers = {
    'Cookie':cookie,
    'Host':'m.weibo.cn',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

data = requests.get(url,headers = headers)
ans = json.loads(data.text)
print(ans)