import requests #used the requests library
from bs4 import BeautifulSoup as bs #used the bs4/BeautifulSoup library 

github_user=input('Input Github User: ') #added a variable called github_user and will obtain the username of the github profile being looked for
url = 'https://github.com/' +github_user #adds the username to the end of the github url 
r = requests.get(url) #sent a request to the newly created url
soup = bs(r.content, 'html.parser') #used beautiful soup to get the particular html source code
# used f12 to find the direct source 'src' code of the image url  
profile_image = soup.find('img', {'alt' : 'Avatar'})['src'] #used soup.find to find the source of the image code through it's container tags
print(profile_image) #print the profile image url to the user