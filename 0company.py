# 原文：https://blog.csdn.net/jiasudu1234/article/details/70065917 
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
