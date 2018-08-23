rhymeTable = [['a','ia','ua'],['ai','uai'],['an','ian', 'uan'],['ang', 'iang', 'uang'],
              ['ao', 'iao'],['e', 'o', 'uo'],['ei', 'ui'],['en', 'in', 'un'],['eng', 'ing', 'ong', 'iong'],
              ['i'],['i'],['ie','e'],['ou','iu'],['u'],['u'],['ue']]
allVowel = ['b','p','m','f','d','t','n','l','z','c','s','zh','ch','sh','r','s','t','g','k','h','j','q','x','y','w',' ']
from xpinyin import Pinyin
import jieba

# vowel 声母
# consonant 韵母
def searchRhymeTable(vowel, consonant, table = rhymeTable):
    if vowel==' ': #零韵母的情况
        if consonant not in ['a','o','e']:
            return (100,100)
    if vowel not in  allVowel: #去除英文或者其他错误的情况
        return (100,100)
    flag  = 0
    for i in range(len(rhymeTable)):
        for j in range(len(rhymeTable[i])):
            if rhymeTable[i][j]==consonant:
                flag =1
    if flag==0:
        return (100,100)

    if consonant=='i': #区分希奇、诗词韵
        if vowel in ['z','c','s','zh','ch','sh']:
            return (10,0)
        else :
            return (9,0)
    elif consonant=='e': #区别国歌、别叠韵
        if vowel=='y':
            return (11,1)
        else :
            return (5,0)
    elif consonant=='u': #区分读书、须臾韵
        if vowel in ['j','q','x','y']:
            return (14,0)
        else :
            return (13,0)
    elif consonant=='v': #考虑ü
        return (14,0)

    for i in range(len(table)):
        if consonant in table[i]:
            j = table[i].index(consonant)
            break
    return (i,j)

def splitVandC(pinyin):
    if len(pinyin)<1 or len(pinyin)>6:
        return ('a','b')
    if len(pinyin)==1:
        return (' ',pinyin[0])
    if pinyin[0] not in allVowel:
        return ('a','b')
    if pinyin[0] in ['z','c','s']:
        if pinyin[1]=='h':
            vowel = pinyin[0:2]
            consonant = pinyin[2:]
        else:
            vowel= pinyin[0]
            consonant = pinyin[1:]
    else:
        vowel = pinyin[0]
        consonant = pinyin[1:]
    return (vowel,consonant)

def getPinyin(chineseSentence):
    p = Pinyin()
    s = p.get_pinyin(chineseSentence, ',')
    plist = []
    lastComma = -1
    for i in range(len(s)):
        if s[i]== ',':
            plist.append(s[lastComma+1:i])
            lastComma = i
    plist.append(s[lastComma+1:])
    return plist

def splitASentence(chineseSentence, allMode = True):
    seg_list = jieba.cut(chineseSentence, cut_all=allMode)
    s = "/".join(seg_list)
    wlist = []
    lastSlash = -1
    for i in range(len(s)):
        if s[i]== "/" :
            wlist.append(s[lastSlash+1:i])
            lastSlash = i
    wlist.append(s[lastSlash+1:])
    return wlist


def analyzeSentence(chineseSentence, minLen=2, maxLen=6, allMode=True):
    wlist = splitASentence(chineseSentence,allMode) #首先对句子进行分词
    sentenres = [] #存储最后的韵母坐标
    orires = [] #存储韵母坐标对应的中文词
    for aword in wlist: #对于分词后的每一个词语
        if len(aword)<minLen or len(aword)>maxLen: #如果词语的长度大于最大或者小于最小
            continue #跳过这个词
        wordres = [] #存储这个词内部的韵母坐标结果
        wordlen  = len(aword)
        for chara in aword: #对于这个词中的每一个字
            pin = getPinyin(chara) #获取拼音
            #print(pin)
            spin = splitVandC(pin[0]) #把拼音分割成声母和韵母
            #print(spin)
            ind = searchRhymeTable(spin[0],spin[1]) #获取韵母坐标
            if ind==(100,100): #如果有错误的拼音坐标
                break #跳过这个词
            wordres.append(ind) #否则继续存储
        if wordlen==len(wordres): #只有当词中没有出现错误坐标的时候
            sentenres.append(wordres) #才存入最终结果里
            orires.append(aword) #以及对应中文
    assert len(sentenres)==len(orires)
    return sentenres,orires #返回（韵母坐标，对应词语）的元组

