from urllib.request import urlopen
from bs4 import BeautifulSoup# Specify url of the web page
from .model import query
output = []
def getPara(url : str):
    summary = ""
    source = urlopen(url).read()# Make a soup 
    soup = BeautifulSoup(source,'html.parser')

    # text = 
    i = 0
    limit = 5
    text = ""
    for paragraph in soup.find_all('p'):
        if i < limit:
            text += paragraph.text
            text += "~"
            i+=1
    para = text.split('~')

    for i in para:
        output = query({"inputs" : i})
        summary += output[0]['summary_text']
    return {soup.title.string : summary}