from rhymeCoordExtractor import analyzeSentence, getPinyin, splitVandC, searchRhymeTable
import openpyxl
import operator

def searchDB(chineseword, dbfile):
    wordres = []  # 存储这个词内部的韵母坐标结果
    for charaindex in range(len(chineseword)):  # 倒序搜索每一个字
        pin = getPinyin(chineseword[-1-charaindex])  # 获取拼音
        spin = splitVandC(pin[0])  # 把拼音分割成声母和韵母
        ind = searchRhymeTable(spin[0], spin[1])  # 获取韵母坐标
        if ind == (100, 100):  # 如果有错误的拼音坐标
            break  # 结束搜索
        wordres.append(ind)  # 否则继续存储
    if len(wordres)==0:
        return None
    elif len(wordres):
        db = openpyxl.load_workbook(dbfile,read_only=True)
        curSheet = db[str(wordres[0])]
        searchRes = {}
        DoubleRhyme = []
		# TODO: 三/四/五押、跳押、首字押等模式
        for row in curSheet:
            curw = row[0].value
            if curw==None:
                continue
            if curw in searchRes:
                searchRes[curw]+=1
            else:
                searchRes[curw]=1
            if len(wordres)>=2 and row[1].value == str(wordres[1]):
                if curw not in DoubleRhyme:
                    DoubleRhyme.append(curw)
    searchRes =sorted(searchRes.items(), key=operator.itemgetter(1), reverse=True)

    return searchRes,DoubleRhyme

	
