from bs4 import BeautifulSoup

with open(r'\data\html\mobile.html','r') as f:
    content=f.read()

soup=BeautifulSoup(content,'lxml')

print(soup.title.text)

products=soup.find_all('div',class_='sm-product has-tag has-features has-actions')
products



name=[]
price=[]
battery=[]
rating=[]
sim=[]
processor=[]
ram=[]
display=[]
camera=[]
card=[]
os=[]



for product in products:
    name.append(product.h2.text) #name

    price.append(product.span.text) #Price

    try:
        rating.append(product.find('span',class_='sm-rating')['style'].split(': ')[-1]) #rating
    
    except:
        rating.append(None)

    try:
        sim.append(product.find('ul',class_='sm-feat specs').find_all('li')[0].text)
    except:
        sim.append(None)


    try:
        processor.append(product.find('ul',class_='sm-feat specs').find_all('li')[1].text)
    except:
        processor.append(None)

    #ram
    try:
        ram.append(product.find('ul',class_='sm-feat specs').find_all('li')[2].text)

    except:
        ram.append(None)

    #Battery
    try:
        battery.append(product.find('ul',class_='sm-feat specs').find_all('li')[3].text)
    except:
        battery.append(None)

    #display
    try:
        display.append(product.find('ul',class_='sm-feat specs').find_all('li')[4].text)
    except:
        display.append(None)

    #camera
    try:
        camera.append(product.find('ul',class_='sm-feat specs').find_all('li')[5].text)
    except:
        camera.append(None)

    #card

    try:
        card.append(product.find('ul',class_='sm-feat specs').find_all('li')[6].text)
    except:

        card.append(None)

    try:
        os.append(product.find('ul',class_='sm-feat specs').find_all('li')[7].text)
    except:
    
        os.append(None)



data={
'name':name,
'price':price,
'rating' :rating,
'battery':battery,
'sim':sim,
'processor':processor,
'ram':ram,
'display':display,
'camera':camera,
'card':card,
'os':os}

import pandas as pd 
df=pd.DataFrame(data)
df.head()

df.to_csv('/data/raw/raw_data.csv')