import requests
from pytube import YouTube
from pytube import Channel
import json
from csv import writer
import csv
response = requests.get(
    url="https://app.scrapingbee.com/api/v1/store/google",
    params={
        "api_key": "<add scrapy api key>",
        "search": "<add search result>",
        "nb_results": "10000",
    },


)
# print(response.content)

obj = json.loads(response.content)
l1 = obj['organic_results']
urls = []
for i in range(len(l1)):
    t = l1[i].get("url")

    if(t.find('channel') != 0 | t.find('/c') != 0):
        urls.append(t)

        # print(t)
    elif('https://www.youtube.com/watch?v=' in t):
        # print(t)
        vid = t.strip()
        x = YouTube(vid)
        C_url = x.channel_url
        # print(C_url)
        urls.append(C_url)
    elif('https://www.youtube.com/' in t):
        urls.append(t)


writer = open("<foldername/filename.csv>", 'w+')
writer_out = csv.writer(writer, delimiter='\n')
fields = ['channel link']
writer_out.writerow(fields)
writer_out.writerow(urls)
