import requests
import pandas
from bs4 import BeautifulSoup
response=requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
print(response)
soup=BeautifulSoup(response.content,"html.parser")
# print(soup)
#unstrutered to structured
names=soup.find_all('td','a',class_="titleColumn")
name=[]
for i in names[0:30]:
    name.append(i.get_text())
# print(name)

images=soup.find_all('img')
image=[]
for i in images[0:30]:
    image.append(i['src'])
# print(image)



ratings=soup.find_all('td',class_="ratingColumn imdbRating")
rating=[]
for i in ratings[0:30]:
    rating.append(i.get_text())
# print(rating)

data={
    "names":pandas.Series(name),
    'images':pandas.Series(image),
    'Ratings':pandas.Series(rating),
}
print(data)
df=pandas.DataFrame(data)#2 dimensional array row*columns
print(df)
df.to_csv("movies.csv")