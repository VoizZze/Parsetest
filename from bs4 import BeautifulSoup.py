from bs4 import BeautifulSoup
import requests
import json
import os


for i in range(1,11):
    Url=f'https://quotes.toscrape.com/page/{i}'     
    Page=requests.get(Url)      
    FullHTML=""                
    Quotes=[]
    Soup = BeautifulSoup(Page.text, "html.parser") 
    FullHTML = Soup.findAll('div', class_='quote',itemtype="http://schema.org/CreativeWork")
    for data in FullHTML:                          
        if data.find('span',class_ = 'text') is not None:
            Quotes.append({'Quote':data.find('span',class_='text').get_text().replace("\u201c",'').replace('\u201d',''),
                           'Author':data.find('small',class_='author').get_text(),
                           'Tags':data.find('meta',class_='keywords').get('content')
                           })
    if os.path.exists('data.json') and os.path.getsize('data.json') > 0: 
        with open('data.json','r') as file:
            try:
                d= json.load(file)
            except json.JSONDecodeError:
                d= []
    else:
        d= []
    for element in Quotes:
        d.append(element)
    with open('data.json','w') as file:
        json.dump(d,file,indent= 1)