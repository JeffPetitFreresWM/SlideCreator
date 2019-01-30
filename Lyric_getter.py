from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import urllib.parse
def lyric_getter(url):
    
    page = urlopen(url)
    soup = bs(page,'html.parser')
    a = soup.find_all('div')
    a = list(a)
    dict_numbers = {}
    for div in a:
        dict_numbers[div]=(len(div))
        dict_numbers
        b = max(dict_numbers, key=dict_numbers.get)
    lyrics = b.get_text()
    lines = lyrics.split('\n')
    clean_lyrics=[]
    for line in lines:
        if len(line) >3:
            clean_lyrics.append(line)




    word=''
    j=1
    for lin in clean_lyrics:
        if j>=4 and j%4==0:
            word+=lin
            word+='\n\n'
            #slidetext.append(clean_lyrics[j])
            j+=1
        else:
            word+=lin
            word+='\n'
            j+=1
    word_list=word.split('\n\n')
    

    return word_list

    

    



