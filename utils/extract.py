from urllib.parse import urlparse
from re import findall
import numpy as np

def getHostname(url):
    try:
        parsedUrl = urlparse(url)
        if (parsedUrl.scheme == ''):
            return str(urlparse('http://'+url).hostname)
        return str(parsedUrl.hostname)
    except:
        return url

# parameters start here:
def hasSuspiciousSymbol(url):
    checkSymbol = ['=','?','%','+','$','!','*',',','@'] 
    for symbol in checkSymbol:
        if symbol in url:
            return True
    return False

def numberDots(url):
    return url.count('.')

def numberHyphen(url):
    return url.count('-')

def numberDigits(url):
    return len(findall(r'/\d/', url))

def urlLen(url):
    return len(url)

def hostNameLen(url):
    return len(getHostname(url))

def pathLen(url):
    return len(str(urlparse(url).path))

def numberBackSlash(url):
    return url.count('/')

def hasHttps(url):
    return 1 if 'https' in url else 0

def getPortN(url):
    try:
        parsedUrl = urlparse(url)
        if (parsedUrl.scheme == ''):
            port = urlparse('http://'+url).port
        else:
            port = parsedUrl.port
        if port is None:
            return 80
        else:
            return port
    except:
        return 80


def extract_features_as_df(url):
    features = []
    # features.append(hasSuspiciousSymbol(url))
    features.append(numberDots(url))
    features.append(numberHyphen(url))
    features.append(numberDigits(url))
    features.append(urlLen(url))
    features.append(hostNameLen(url))
    features.append(pathLen(url))
    features.append(numberBackSlash(url))
    features.append(hasHttps(url))
    # features.append(getPortN(url))

    df = np.array([ features ], dtype=object)

    return df
