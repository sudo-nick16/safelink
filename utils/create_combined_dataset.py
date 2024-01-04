import pandas as pd 
from urllib.parse import urlparse
from re import findall
from extract import * 

df1 = pd.read_csv("ai/dataset/malicious_phish.csv")
df2 = pd.read_csv("ai/dataset/data.csv")

df1_uniques = df1.type.unique()

df1 = df1.replace({'type':{'phishing':'bad','defacement':'bad','malware':'bad','benign':'good'}})

df1.rename(columns={'type':'label'},inplace=True)

df = pd.concat([df1,df2],axis=0)

df = df.drop_duplicates()

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

df.to_csv("ai/dataset/url-combined-dataset.csv", index = False)
