import requests
import pandas
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp2&fm=neo%2Fmerchandising&iid=M_0cb2ea65-c0bf-4d8a-b52d-124b36993e51_5.Q1PDG4YW86MF&ppt=hp&ppn=homepage&ssid=fsp8wq9pow0000001683985899866")
#print(response)
soup=BeautifulSoup(response.content,"html.parser")
# print(soup)
#unstrutered to structured
names=soup.find_all('div',class_="_4rR01T")
name=[]
for i in names[0:10]:
    name.append(i.get_text())
# print(name)
prices=soup.find_all('div',class_="_30jeq3 _1_WHN1")
price=[]
for i in prices[0:10]:
    price.append(i.get_text())
#print(price)
reviews=soup.find_all('div',class_="_3LWZlK")
review=[]
for i in reviews[0:10]:
    review.append(i.get_text())
# print(review)

ratings=soup.find_all('span',class_="_2_R_DZ")
rating=[]
for i in ratings[0:10]:
    rating.append(i.get_text())
# print(rating)

ratings=soup.find_all('span',class_="_2_R_DZ")
rating=[]
for i in ratings[0:10]:
    rating.append(i.get_text())
# print(rating)

images=soup.find_all('img',class_="_396cs4")
image=[]
for i in images[0:10]:
    image.append(i['src'])
# print(image)

links=soup.find_all('a',class_="_1fQZEK")
print(links)
link=[]
for i in links[0:10]:
    d='https://www.flipkart.com'+ i['href']
    link.append(d)
print(link)

data={
    "names":pandas.Series(name),
    'Ratings':pandas.Series(rating),
    'Prices':pandas.Series(price),
    'reviews':pandas.Series(review),
    'images':pandas.Series(image),
    'Links':pandas.Series(link)
}
# print(data)
df=pandas.DataFrame(data)#2 dimensional array row*columns
#print(df)
df.to_csv("mobiles.csv")