#!/bin/python

''' download any books from 8novels.net in .txt format by aksl337 '''
import io
import sys
from bs4 import BeautifulSoup
import requests
from time import sleep


headerss = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0", "Accept-Language": "en-US, en;q=0.5"}

# check for link of book on 8novel site,change accordingly
url_string = "http://www.8novels.net/billion/b6747"
# change range for last page for eg. if book last page is 131 then range(2,132)
url_list = [url_string + "_" + str(i) for i in range(2, 132)]
url_list.insert(0, url_string)
# This site require sessions
s = requests.Session()
for indexed, link in enumerate(url_list):
    try:

        response = s.get(link + '.html', headers=headerss, timeout=10)
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.find(class_="text").get_text()
        if not content:
            print " no output form web"
        else:
            # download content of book in one .txt file later we can easily convert it to pdf
            # you can download each page to seperate .txt with litte change here
            with io.open('unvailed.txt', mode='at', encoding='utf-8') as out_file:
                out_file.write(unicode(content))
            print '{}{} success'.format('unvailed.txt', str(indexed))
    except requests.exceptions.HTTPError as e:
        print ('connection refused by server,make sure site is up and working...')
        print ('lemme try again...')
        sleep(5)
        continue
    except requests.Timeout as e:
        print(str(e))
        print 'timed out'
        print('lemme try again')
        sleep(5)
        continue
    except AttributeError:
        print 'error in content'
    except requests.ConnectionError:
        print 'network problem, are you sure ,you are online? either its you or site itself'
        sys.exit()

    sleep(0.4)
