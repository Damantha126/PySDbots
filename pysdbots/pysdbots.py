import requests


headers={'Content-Type': 'application/json'}


def anime_logo(name):
    API = f"https://api.sdbots.tech/anime-logo?name={name}"
    req = requests.get(API).url
    return(req)

def tiktok(url):
    API = f"https://api.sdbots.tech/tiktok?url={url}"
    req = requests.get(API).json()
    return(req)

def apod():
    API = "https://api.sdbots.tech/apod"
    req = requests.get(API).json()
    return(req)

def detect_lang(text):
    req = requests.get(f"https://api.sdbots.tech/detect?text={text}").json()
    return(req)

def write(text):
    body = {
        "text": f"{text}"
    }
    url = "https://api.sdbots.tech/write"
    req = requests.post(url=url, headers=headers, json=body).url
    return(req)

def chk(cc):
    API = f"https://api.sdbots.tech/chk?cc={cc}"
    req = requests.get(API).json()
    return(req)

def sk_checker(key):
    req = requests.get(f"https://api.sdbots.tech/sk?key={key}").json()
    return(req)

def lyrics(song):
    req = requests.get(f"https://api.sdbots.tech/lyrics?song={song}").json()
    return(req)

def ipinfo(ip):
    req = requests.get(f"https://api.sdbots.tech/ipinfo?ip={ip}").json()
    return(req)

def hirunews():
    req = requests.get("https://api.sdbots.tech/hirunews").json()
    return(req)

def logohq(text):
    req = requests.get(f"https://api.sdbots.tech/logohq?text={text}").url
    return(req)

def fakeinfo():
    req = requests.get("https://api.sdbots.tech/fakeinfo").json()
    return(req)


print("SD Bots API -> https://docs.sdbots.tech")