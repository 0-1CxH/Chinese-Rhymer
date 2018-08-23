# Chinese Rhymer
This project includes two main parts: the Learning System and the Search Module.
The Learning System is responsible for downloading and analyzing the text, which can be lyrics, poetry lines or any text for the Rhyme Database to record. 
After building the Rhyme Database, the Search Module returns the result of matching the rhyme pattern of input keyword with words in the database.


## Learning System
Learning System has several main functions:
### analyzeSentence(chineseSentence)
Get the Rhyme Coordinate of a Chinese sentence. If more than one Chinese character is input, a list of Coordinates are returned.<br>
With the API provided by Jieba and xpinyin, splitting sentences and get the original Pinyin is much easiler.<br>

Here is one example:

>>>analyzeSentence("这个项目由0-1CxH设计和编写", minLen=2, maxLen=6, allMode=True)  


Result:
>>>([[(5, 0), (5, 0)], [(3, 1), (13, 0)], [(5, 0), (9, 0)], [(2, 1), (11, 0)]], ['这个', '项目', '设计', '编写'])



As shown in the example, all Non-Chinese characters are ignored, and words whose length less than minLen=2 or more than maxLen=6 are also ignored.<br>




### downloadLyricsOfAPlayList(playlistid,filename)
With playlist and filename input, the crawler download ALL lyrics from the assigned NetEase playlist.<br>
This function is mainly based on getPlaylistInfoByHibaiAPI(id), which provides the information of all songs in a playlist. <br>
As you may notice, "TransCode=020111" is defined by the API, meaning the playlist is from NetEase Music.<br>
The Hibai also has API of web-crawling other music websites, please contact the Hibai for more information. <br>
And my src code includes the API provided by NetEase itself, please contact the NetEase for more information.<br>

Here is an example:

>>> downloadLyricsOfAPlayList("313835828","0001.txt")


### analyzeAFile(filename,database)
After initiated an empty database (using Excel for convienence) with "initEmptyDB(dbname)", the xls/xlsx file is ready for storing analyse results. <br>
"analyzeAFile()" uses lyrics text file and databse file as input, by analyzing LRC line by line using "analyzeSentence()" and record the result returned in specific workbook sheets.<br>
This process consume so much time (Average: 30min/150songs).


Here is an example:

>>> analyzeAFile("0001.txt","db.xlsx")

## Search Module
Search Module includes:
### searchDB(chineseword, dbfile)
This function mainly serves the query purpose :"Match words in Database<dbfile> whose Rhyme Coordinate(s) is/are same as the given Word<chineseword>."<br>
Returned result is arranged like (searchRes,DoubleRhyme), "searchRes" contains all words that has same ending rhyme with the word, "DoubleRhyme" contains all words has at least two same ending rhymes with the word. <br>
The search module is crude without much design, so the future versions would improve on more complex rhyme patterns.

Here is an example:

>>> searchDB("未来", "db.xlsx")


Result:

>>> ([('现在', 41), ('离开', 29), ('不再', 27), ('下来', 27), ('应该', 26), ('未来', 22), ('明白', 20), ('期待', 17), ('静下来', 15), ('醒来', 14), ('后来', 13), ('等待', 12), ('回来', 12), ('不在', 12), ('人海', 12), ('大海', 10), ('存在', 10), ('不该', 9), ('留在', 9), ('从来', 9), ('坐在', 9), ('没来', 8), ('苍白', 8),
<br>...此处省略其他结果...<br>], ['没来', '未来', '北海'])

i.e. ('现在', 41) means '现在' and "未来" has same rhyme, and was recorded for 41 times from what learnt so far.
i.e. ['没来', '未来', '北海'] are at least double rhyme of "未来".


### searchInterface.py
This file is the GUI of the Search Module.


## Appendix

**Rhyme Coordinate** is the position of the Chinese YunMu(韵母) in the Mandarin Rhyme Table(普通话押韵表),which is listed below:

>一、佳麻　 a ia ua　　<br>
二、开来　 ai uai　　　　<br>
三、先寒　 an ian uan üan <br>
四、江阳　 ang iang uang　<br>
五、逍遥　 ao iao　<br>
六、国歌　 e o uo　　　<br>
七、灰微　 ei ui　　　<br>
八、森林　 en in un ün　<br>
九、冬青　 eng ing ong iong   <br>
十、希奇（儿）i（er并入）　<br>
十一、诗词　i（整体认读）<br>
十二、别叠　ie (y)e 　<br>
十三、忧愁　ou iu　　　<br>
十四、读书　u　　<br>
十五、须臾　ü　　　<br>
十六、绝学　üe     <br>


i.e.,the Rhyme Coordinate of 'ao' is (4,0).