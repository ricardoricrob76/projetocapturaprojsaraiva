#import libraries
import urllib
import urllib.request
from bs4 import BeautifulSoup
 
#specify the url
quote_page = 'https://www.bloomberg.com/quote/SPX:IND'
 
#query the website and return the html to the variable 'page'
page = urllib.request.urlopen(quote_page)
 
#parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parse')
 
#Take out the <div> of name and get its value
name_box = soup.find('h1', attr={'class': 'name'})
 
name = name_box.text.strip() # strip() is used to remove starting & trailing
print(name)