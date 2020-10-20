from bs4 import BeautifulSoup
import requests

with open('enter html link here .html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')  # The lxml is a particular parser, but it can be any parser!

print(soup.prettify())  # This prints the whole html and indents it to make it more readable

match = soup.title.text  # In this example, soup has many variables which are
# accessible to the user because they're just common html tags! So here, we're grabbing the text
# from the first "title" tag located in the .html file

match2 = soup.find('div',
                   class_='footer')  # In this example, we are finding the div tag that specifically has the class
# 'footer' in it. class_ is used since "class" is a keyword in python compilers

# Remember to use the "inspect" thing in your browser to figure out what you want to grab from the websites
