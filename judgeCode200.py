# -*- coding:utf-8 -*-
# Author:ivonne
# Time:2019/1/18
# python 3
import multiprocessing
import urllib.request
import urllib.error
import argparse
import time

#参数
def Args():
    #按照原样输出
    parse = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,add_help=False,description='''
    *===================================*
    |    Please set the parameters!     |
    |    Author:ivonne                  |
    |    Version:1.0                    |
    |    Time:2019/1/18                 |
    *===================================*
    ''')
    parse.add_argument('-f','--file',help='Please set FILE')
    parse.add_argument('-t','--thread',default=4,help='Please set thread number',type=int)
    args = parse.parse_args()
    if args.file is None :
        print (parse.print_help())
        exit()
    else :
        return args


#判断返回值是否为200
def judge(file):
    list2 = []#用来放返回值为200的列表
    with open(file,'r') as f:
        for i in f.readlines():
            i = i.strip()
            list1.append(i)
    for i in range(list1.__len__()):
        urls = 'http://'+list1[i]
        try:
            opurl = urllib.request.urlopen(urls, timeout=3).code
            list2.append(urls)
        except urllib.error.URLError as e:
            e = str(e)
            if 'SSL' in e:
                urls = 'https://'+list1[i]
                list2.append(urls)
        except:
            pass
    return list2   

## 程序入口
if __name__ == "__main__":
    list1 = []#用来放file中的url列表
    args = Args()
    pool = multiprocessing.Pool(args.thread)
    result = pool.map(judge,(args.file,))
    start = time.clock()
    pool.close()
    pool.join()
    with open('res.txt','a') as f:
        for i in result:
            for url in i:
                f.write(str(url)+'\n')
    end = time.clock()
    print ('\nRunning time: %f Seconds'%(end-start))







