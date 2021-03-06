# Split-words

<p align="center">
    <a href="https://github.com/elegantcoin/Split-words"><img src="https://img.shields.io/badge/status-updating-brightgreen.svg"></a>
    <a href="https://github.com/python/cpython"><img src="https://img.shields.io/badge/Python-3.7-FF1493.svg"></a>
    <a href="https://github.com/elegantcoin/Split-words"><img src="https://img.shields.io/badge/platform-Windows%7CLinux%7CmacOS-660066.svg"></a>
    <a href="https://opensource.org/licenses/mit-license.php"><img src="https://badges.frapsoft.com/os/mit/mit.svg"></a>
    <a href="https://github.com/elegantcoin/Split-words/stargazers"><img src="https://img.shields.io/github/stars/elegantcoin/Split-words.svg?logo=github"></a>
    <a href="https://github.com/elegantcoin/Split-words/network/members"><img src="https://img.shields.io/github/forks/elegantcoin/Split-words.svg?color=blue&logo=github"></a>
    <a href="https://www.python.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" align="right" height="48" width="48" ></a>
</p>
<br />

inspired by [分词打标](http://www.gooseeker.com/res/softdetail_13.html) and [Jieba tutorial](https://blog.csdn.net/jiasudu1234/article/details/70065917), A splitting Chinese words and counting their frequence method is presentated. Since the original system is poorly performed, stopwords are used and English words are delt with correctly.

- ps::joy::joy::joy:[Leetcode 192. Word Frequency](https://leetcode-cn.com/problems/word-frequency/solution/shelltong-ji-ci-pin-by-laotoutou/)  Only counting words, see this one line simple solution!
    ```shell
    cat words.txt | xargs -n 1|sort |uniq -c|sort -nr| awk '{print $2" "$1}'
    ```

Results should be:

![](https://github.com/elegantcoin/fenci/blob/master/1111.png)
![](https://github.com/elegantcoin/fenci/blob/master/2222.png)

  ## - :fire: 1. input：
  - [All.csv](https://github.com/elegantcoin/fenci/blob/master/All.csv) —— Words need to be split.
  - [stopwords.txt](https://github.com/elegantcoin/fenci/blob/master/stopwords.txt) ——  Stopwords used(both English and Chinese).
  
  ## - :fire: 2. main file：
  - [Split_words.py](https://github.com/elegantcoin/Split-words/blob/master/Split_words.py)  —— Main excution code.
  
  ## - :fire: 3. output：
  - [fenci_190807_14_55.csv](https://github.com/elegantcoin/fenci/blob/master/fenci_190807_14_55.csv)  —— Words split.
  - [keyword_190807_14_55.csv](https://github.com/elegantcoin/fenci/blob/master/keyword_190807_14_55.csv)  —— Keywords.

  # - :fire: 4. sourcecode：
```python
# _*_ coding: UTF-8 _*_
import csv
import jieba
import jieba.posseg as psg
import copy
import time
import argparse


ap=argparse.ArgumentParser()
ap.add_argument("-f","--file-name",required=True,
    help="Input file name")
args=vars(ap.parse_args())

#读取停词表
stopwords = [line.strip() for line in  open('stopwords.txt',encoding='UTF-8-sig').readlines()]
stopflags=["m","o","q","w","x","y"]
#一行行读取csv
file_object2=open(args["file_name"],'r',encoding ='UTF-8-sig').read().split('\n')

#建立分词存储列表
Rs1=[]
Rs2=[] 
#统计词频的字典
dic={}
dic2= {"Ag":"形语素","a":"形容词","ad":"副形词","an":"名形词","b":"区别词","c":"连词","dg":"副语素","d":"副词","e":"叹词","f":"方位词","g":"语素",\
    "h":"前接成分","i":"成语","j":"简称略语","k":"后接成分","l":"习用语","m":"数词","Ng":"名语素","n":"名词","nr":"人名","ns":"地名","nt":"机构团体",\
    "nz":"其他专名","o":"拟声词","p":"介词","q":"量词","r":"代词","s":"处所词","tg":"时语素","t":"时间词","u":"助词","vg":"动语素","v":"动词",\
    "vd":"副动词","vn":"名动词","w":"标点符号","x":"非语素字","y":"语气词","z":"状态词","un":"未知词",}

for i in range(len(file_object2)):
  result=[]
  # 选择cut的模式
  # seg_list = jieba.cut(file_object2[i])
  seg_list = psg.cut(file_object2[i])
  # seg_list = jieba.cut_for_search(file_object2[i])
  #添加源数据列	
  # result.append(file_object2[i])
  #读取每一行分词	
  for w in seg_list :
    if w.word not in stopwords and w.flag not in stopflags:
      result.append(w.word)
      dic[w]=dic.get(w,0)+1
      continue
  #把分词写入源列表后面	
  Rs1.append(result)

#写入CSV,并用时间命名文件 避免重名
# 08 05 2019 09:49:02 时间格式
doctime=str(time.strftime("%m %d %Y %H:%M:%S", time.localtime()))
mon=doctime[0:2]
dy=doctime[3:5]
yr=doctime[6:10]
hr=doctime[11:13]
mi=doctime[14:16]
se=doctime[17:19]

file=open('0fenci_'+yr[-2:]+mon+dy+'_'+hr+'_'+mi+se+'.csv','w',newline='',encoding='utf-8-sig')
writer = csv.writer(file)
writer.writerows(Rs1)
file.close() 

# dic排序
dic1=copy.deepcopy(dic)
dic = sorted(dic1.items(), key=lambda d:d[1], reverse = True)
for k,v in enumerate(dic):
  Rs2.append((v[0].word,v[0].flag,dic2.get(v[0].flag),v[1]))

# for k,v in enumerate(dic):
# 	Rs2.append((v,dic[v]))

#print(Rs2[:10])
file=open('1keyword_'+yr[-2:]+mon+dy+'_'+hr+'_'+mi+se+'.csv','w',newline='',encoding='utf-8-sig')
writer = csv.writer(file)
writer.writerows(Rs2)
file.close() 
```
 # :fire: - 中国大学： [中国所有大学分词](https://github.com/elegantcoin/fenci/blob/master/Universities.csv)
    
![](https://github.com/elegantcoin/fenci/blob/master/Colleges_in_China.png)

  # - 思考：
  - cloudword?
  - Shell 可以一行解决词频问题，但是原文的分词结果展示以及中文实现是困难的。
  - 关键信息成组
  - keywors sort()在源代码中对dic排序？还是直接导出结果后再排序，谁的效率高？
  - 停词已经判断则不需要再次判断
  - 舆情分析
  - [Awesome!!!](https://github.com/crownpku/Awesome-Chinese-NLP)
  - [中文知识图谱 openkg.cn](http://openkg.cn/home)
  - 快速将大学的简称也分出来（如北京大学→北大、清华大学→清华、上海交通大学→上交）
  - 利用[百度echarts](https://echarts.apache.org/examples/zh/index.html#chart-type-parallel) 和[这个思路@zhouwei713](https://github.com/zhouwei713/data_analysis/tree/master/honglou)渲染图谱
  - 高频词提取后进行词之间的连接，形成图谱。如下所示:
    
    ![](https://github.com/elegantcoin/fenci/blob/master/ifind.png)
  - 利用[`Ucinet6`](http://www.cabit.com.cn/products/dec/ucinet/) 和 [`NetDraw`](http://www.jeb.com.fr/en/netdraw.shtml) 可以绘制简单版本的，但是可视化效果不好，如下图所示:
    ![](https://github.com/elegantcoin/fenci/blob/master/NetDraw.jpg)