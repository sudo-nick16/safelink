import pandas as pd 
from urllib.parse import urlparse
from re import findall
from extract import * 

df = pd.read_csv("ai/dataset/data.csv")

# df['hasSuspiciousSymbol'] = [hasSuspiciousSymbol(url) for url in df['url']]
df['numberDots'] = [url.count('.') for url in df['url']]
df['numberHyphen'] = [url.count('-') for url in df['url']]
df['numberDigits'] = [len(findall(r'/\d/', url)) for url in df['url']]
df['urlLen'] = [len(url) for url in df['url']]
df['hostNameLen'] = [len(getHostname(url)) for url in df['url']]
df['pathLen'] = [len(str(urlparse(url).path)) for url in df['url']]
df['numberBackSlash'] = [url.count('/') for url in df['url']]
df['hasHttps'] = [1 if 'https' in url else 0 for url in df['url']]
# df['portN'] = [getPortN(url) for url in df['url']]

df = df.replace({'label':{'bad':0,'good':1}})

df.to_csv("ai/dataset/smol-data.csv", index = False)
