import requests
#引用requests库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
#下载《三国演义》第一回，我们得到一个对象，它被命名为res
novel=res.text

book = open('三国演义.txt','w',encoding='utf-8')

book.write(novel)

book.close()
