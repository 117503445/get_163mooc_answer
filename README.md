# get_163mooc_answer

用于爬取mooc测试答案

因为没有做爬虫部分,需要手动爬取建立题库

## 建立题库

开启小号,进入测试,什么也不要填,开始Chrome抓包,提交,抓取 <https://www.icourse163.org/dwr/call/plaincall/MocQuizBean.getQuizPaperDto.dwr> ,把响应复制到py文件夹下*.txt,自己取名

然后运行 parse.py ,会将这些题目与答案收集到 answer.json

## 搜索题目

开启大号,开始chrome抓包,进入测试,抓取 <https://www.icourse163.org/dwr/call/plaincall/MocQuizBean.getQuizPaperDto.dwr> ,响应复制到q.txt

然后运行 search.py ,输出 test.html 即为答案

## 其他

没有充足考虑兼容性,但是代码非常简单,修改方便
