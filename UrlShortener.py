# Shortener the Longer URL using build in Library Files
# pyshorteners 
# pyperclip 

import pyshorteners

def shortenerurl(url): 
    shorturl= pyshorteners.Shortener()
    print(shorturl.tinyurl.short(url)) 


url=input("Enter the URL to shortening: ") 
shortenerurl(url)