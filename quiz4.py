import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

f = open('websites.csv','w')
f.write('name,description\n')
ind = 1
while ind <= 5:
    print('page ' + str(ind))
    url = 'https://www.top.ge/category/page/'+str(ind)+'/8'
    r = requests.get(url)

    content = r.text

    soup = BeautifulSoup(content, 'html.parser')


    websites_block = soup.find('table', class_ = "raiting_table")
    websites = websites_block.find_all('tr', class_ = None)
    for each in websites:
        name = each.find('a', class_ = 'stie_title')
        if name is not None:
            print(name.text,end=' - ')
            f.write(name.text + '\n')

        desc = each.find('td', class_ = 'tr_paddings desc_pd hidden-xs ipad_hidden')
        if desc is not None:
            print(desc.text)


    ind += 1
    sleep(randint(15,20))