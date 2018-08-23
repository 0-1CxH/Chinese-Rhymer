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
>>>([[(5, 0), (5, 0)], [(3, 1), (13, 0)], [(5, 0), (9, 0)], [(2, 1), (11, 0)]], ['这个', '项 目', '设计', '编写'])



As shown in the example, all Non-Chinese characters are ignored, and words whose length less than minLen=2 or more than maxLen=6 are also ignored.<br>

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


### downloadLyricsOfAPlayList(playlistid,filename)
With playlist and filename input, the crawler download ALL lyrics from the assigned NetEase playlist.<br>
This function is mainly based on getPlaylistInfoByHibaiAPI(id), which provides the information of all songs in a playlist. <br>
As you may notice, "TransCode=020111" is defined by the API, meaning the playlist is from NetEase Music.<br>
The Hibai also has API of web-crawling other music websites, please contact the Hibai for more information. <br>
And my src code includes the API provided by NetEase itself, please contact the NetEase for more information.<br>





