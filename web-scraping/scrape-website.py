from bs4 import BeautifulSoup
import requests
import csv

# By adding a text to the end, it will get the html of a given website
source = requests.get('http://coreyms.com').text
soup =  BeautifulSoup(source, 'lxml')

csvFile = open('scrapeCMS.csv', 'w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['headline', 'summary', 'link'])


for article in soup.find_all('article'):

    # Getting the first article headline
    headline = article.h2.a.text
    print(headline)

    # Getting the text
    subjectVideo = article.find('div', class_='entry-content').p.text
    print(subjectVideo)

    # Getting the video source, access terms within a tag as a dictionary
    try:
        videoSource = article.find('iframe', class_='youtube-player')['src']
        videoList = videoSource.split('/')
        videoLink = f'{videoList[0] +  videoList[2] + "/" + "watch?v=" + videoList[4].split("?")[0]}'
        print(videoLink)

    except Exception as identifier:

        print(identifier)
     
    csvWriter.writerow([headline, subjectVideo, videoLink])
    print()

csvFile.close()