# fenci

<p align="center">
    <a href="https://github.com/elegantcoin/fenci"><img src="https://img.shields.io/badge/status-updating-brightgreen.svg"></a>
    <a href="https://github.com/python/cpython"><img src="https://img.shields.io/badge/Python-3.7-FF1493.svg"></a>
    <a href="https://github.com/elegantcoin/fenci"><img src="https://img.shields.io/badge/platform-Windows%7CLinux%7CmacOS-660066.svg"></a>
    <a href="https://opensource.org/licenses/mit-license.php"><img src="https://badges.frapsoft.com/os/mit/mit.svg"></a>
    <a href="https://github.com/elegantcoin/fenci/stargazers"><img src="https://img.shields.io/github/stars/elegantcoin/fenci.svg?logo=github"></a>
    <a href="https://github.com/elegantcoin/fenci/network/members"><img src="https://img.shields.io/github/forks/elegantcoin/fenci.svg?color=blue&logo=github"></a>
    <a href="https://www.python.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" align="right" height="48" width="48" ></a>
</p>
<br />

inspired by [分词打标](http://www.gooseeker.com/res/softdetail_13.html) and [Jieba tutorial](https://blog.csdn.net/jiasudu1234/article/details/70065917), A splitting Chinese words and counting their frequence method is presentated. Since the original system is poorly performed, stopwords are used and English words are delt with correctly.

Results should be:

![](https://github.com/elegantcoin/fenci/blob/master/1111.png)
![](https://github.com/elegantcoin/fenci/blob/master/2222.png)

  ## - 1. input：
  - [All.csv](https://github.com/elegantcoin/fenci/blob/master/All.csv) —— Words need to be split.
  - [stopwords.txt](https://github.com/elegantcoin/fenci/blob/master/stopwords.txt) ——  Stopwords used(both English and Chinese).
  
  ## - 2. main file：
  - [0company.py](https://github.com/elegantcoin/fenci/blob/master/0company.py)  —— Main excution code.
  
  ## - 3. output：
  - [fenci_190807_14_55.csv](https://github.com/elegantcoin/fenci/blob/master/fenci_190807_14_55.csv)  —— Words split.
  - [keyword_190807_14_55.csv](https://github.com/elegantcoin/fenci/blob/master/keyword_190807_14_55.csv)  —— Keywors.

  # - 4. sourcecode：
```python
        # _*_ coding: UTF-8 _*_
        import csv
        import jieba
        import time
        import pandas as pd

        #读取停词表
        stopwords = [line.strip() for line in  open('stopwords.txt',encoding='UTF-8').readlines()]
        #一行行读取csv
        file_object2=open('All.csv').read().split('\n')  

        #建立分词存储列表
        Rs1=[]
        Rs2=[] 
        #统计词频的字典
        dic={}

        for i in range(len(file_object2)):
            result=[]
        #	seg_list = jieba.cut(file_object2[i]) 选择cut的模式
            seg_list = jieba.cut_for_search(file_object2[i])
            #添加源数据列	
            result.append(file_object2[i]) 
            #读取每一行分词	
            for w in seg_list :
                if w not in stopwords:
                    result.append(w)
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
        se=doctime[14:16]

        file=open('fenci_'+yr[-2:]+mon+dy+'_'+hr+'_'+se+'.csv','w')
        writer = csv.writer(file)
        writer.writerows(Rs1)
        file.close() 

        for k,v in enumerate(dic):
            Rs2.append((v,dic[v]))

        #print(Rs2[:10])
        file=open('keyword_'+yr[-2:]+mon+dy+'_'+hr+'_'+se+'.csv','w')
        writer = csv.writer(file)
        writer.writerows(Rs2)
        file.close() 
```
 # - 中国大学：
[中国所有大学分词](https://github.com/elegantcoin/fenci/blob/master/Universities.csv)

  # - 思考：
  - cloudword?
  - 关键信息成组
  - keywors sort()在源代码中对dic排序？还是直接导出结果后再排序，谁的效率高？
  - 停词已经判断则不需要再次判断
  - 舆情分析
  - [Awesome!!!](https://github.com/crownpku/Awesome-Chinese-NLP)
  - 快速将大学的简称也分出来（如北京大学→北大、清华大学→清华、上海交通大学→上交）
