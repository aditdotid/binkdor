#-*- coding: utf-8 -*-
#recoded by: github.com/aditdotid
import requests
f = open("dork.txt", "r").read().split("\n")
page = 1
# define how many pages to look in
PageDepth = int(input('Halaman ? 1-10 '))
for dork in f:
    if dork == "":
        continue
    for k in range(0, PageDepth):
        bingurl = "https://www.bing.com/search?q=" + dork +"&first=" + str(page) + "&FORM=PERE"
        page += 10
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
        try:
            pageSource = requests.get(bingurl, headers=headers).text
        except requests.exceptions.HTTPError:
            continuecontinue
        except requests.exceptions.ConnectionError:
            continue
        except requests.exceptions.Timeout:
            continue
        da = pageSource.split('<li class="b_algo"><h2><a href="')
        domains = []
        for i in range(0, 10):
            try:
                domains.append(da[i+1].split('"')[0])
            except:
                pass
        for l in domains:
            open('Hasil.txt', 'a+').close()
            l = l.split('/')
            l = l[0] + '//' + l[1] + l[2]
            if l not in open('Hasil.txt', 'r').read():
                open('Hasil.txt', 'a+').write(l + '\n')
                print(l)
print("gunakan dengan bijak ... ")
