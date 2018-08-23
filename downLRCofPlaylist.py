import requests
import json
import os


def getPlaylistInfoByHibaiAPI(id):
    id = str(id)
    #header = {'user-agent':'Mozilla/5.0'}
    data1 = {"TransCode": "020111", "OpenId": "Test", "Body": {"SongListId": id}}
    url = 'https://api.hibai.cn/api/index/index'
    req = requests.post(url,json=data1)
    #print(req.url)
    return req.json()

def getLyricsByNetEaseAPI(songid):
    songid = str(songid)
    url = "http://music.163.com/api/song/lyric?os=pc&id="+songid+"&lv=-1&kv=-1&tv=-1"
    req = requests.get(url)
    return req.json()

def getLyricByHabaiAPI(songid):
    songid = str(songid)
    url = "https://api.hibai.cn/music/Music/Music?id="+songid+"&type=lrc"
    req = requests.get(url)
    return req.json()

def writeToFile(s, filename):
    i = 0
    if not os.path.exists(filename):
        g = open(filename,"a",encoding='utf-8')
        g.close()
    # filesize = os.path.getsize(filename)
    # while filesize > tmax:
    #     i = i+1
    #     filename = filenameList[i]
    #     filesize = os.path.getsize(filename)
    f = open(filename,"a",encoding='utf-8')
    f.write(s)
    f.close()
    return

def downloadLyricsOfAPlayList(playlistid,filename):
    raw = getPlaylistInfoByHibaiAPI(playlistid)
    raw = raw['Body']['songs']
    print(raw)
    lrcURL = []
    count = 0
    for item in raw:
        Aurl = item['lrc']
        #lrcURL.append(Aurl)
        print(Aurl)
        req = requests.get(Aurl)
        s = req.text
        writeToFile(s,filename)
        count+=1
        print("Processing Song %d" %count)
    return


