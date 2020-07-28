from bs4 import BeautifulSoup
import requests
from collections import Counter

#url = 'https://www.rev.com/blog/transcripts/donald-trump-chris-wallace-interview-transcript-july-19'
url = 'https://www.rev.com/blog/transcripts/joe-biden-child-and-elder-care-plan-speech-transcript-july-21'
req = requests.get(url)

soup = BeautifulSoup(req.text,"lxml")
paragraphs = soup.find_all('p')
transcript = ''

for paragraph in paragraphs:
    transcript = transcript + ' ' + paragraph.text
   
transcript = transcript.lower()
words = transcript.split()
Counter = Counter(words)

if(Counter['health']+ Counter['cases'] + Counter['healthcare'] + Counter['virus'] > 10):
    print('health')
if(Counter['police'] + Counter['enforcement'] + Counter['brutality'] + Counter['protests'] > 10):
    print('police')
if(Counter['economy'] + Counter['economic'] + Counter['unemployment'] + Counter['recession'] + Counter['jobs'] > 10):
    print('economy')
