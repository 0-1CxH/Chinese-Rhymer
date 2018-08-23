# Chinese Rhymer
This project includes two main parts: the Learning System and the Search Module.
The Learning System is responsible for downloading and analyzing the text, which can be lyrics, poetry lines or any text for the Rhyme Database to record. 
After building the Rhyme Database, the Search Module returns the result of matching the rhyme pattern of input keyword with words in the database.

## Learning System
Learning System has several main functions:
### analyzeSentence(chineseSentence)
Get the Rhyme Coordinate of a Chinese sentence. If more than one Chinese character is input, a list of Coordinates are returned.
Rhyme Coordinate is the position of the Chinese YunMu(韵母) in the Mandarin Rhyme Table(普通话押韵表),which is listed below:

>一、佳麻　 a ia ua　　
二、开来　 ai uai　　　　
三、先寒　 an ian uan üan
四、江阳　 ang iang uang　
五、逍遥　 ao iao　　　　　
六、国歌　 e o uo　　　
七、灰微　 ei ui　　　
八、森林　 en in un ün　
九、冬青　 eng ing ong iong
十、希奇（儿）i（er并入）　
十一、诗词　i（整体认读）
十二、别叠　ie (y)e 　
十三、忧愁　ou iu　　　　
十四、读书　u　　　　　
十五、须臾　ü　　　　　　
十六、绝学　üe


i.e.,the Rhyme Coordinate of 'ao' is (4,0).

