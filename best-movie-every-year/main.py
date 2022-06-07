#imports
import urllib3
from bs4 import BeautifulSoup

#inputs
inputYear = input("input the year you want to see the top 10 movies of: ")

# url handling
imdbUrl = "https://www.imdb.com/search/title/?release_date=" + inputYear + "," + inputYear + "&countries=in"
myUrl = urllib3.PoolManager().request('GET', imdbUrl).data
soup = BeautifulSoup(myUrl, "lxml")

print(soup.find('title').text)
print()

counter = 1
movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
if len(movieList) == 0:
    print("No movies returned, maybe the year inputted is wrong.")
else:
    for div_item in movieList:
        if counter>10:
            break
        div = div_item.find('div',attrs={'class':'lister-item-content'})
        header = div.findChildren('h3',attrs={'class':'lister-item-header'})
        name_of_the_movie = str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore'))
        if name_of_the_movie == "":
            print("No movies returned, maybe the year inputted is wrong")
        print(str(counter) + ". " + name_of_the_movie)

        counter += 1

