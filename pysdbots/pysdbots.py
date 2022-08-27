import requests


headers={'Content-Type': 'application/json'}


def anime_logo(name):
    API = f"https://api.sdbots.tk/anime-logo?name={name}"
    req = requests.get(API).url
    return(req)

def tiktok(url):
    API = f"https://api.sdbots.tk/tiktok?url={url}"
    req = requests.get(API).json()
    return(req)

def apod():
    API = "https://api.sdbots.tk/apod"
    req = requests.get(API).json()
    return(req)

def detect_lang(text):
    req = requests.get(f"https://api.sdbots.tk/detect?text={text}").json()
    return(req)

def write(text):
    body = {
        "text": f"{text}"
    }
    url = "https://api.sdbots.tk/write"
    req = requests.post(url=url, headers=headers, json=body).url
    return(req)

def chk(cc):
    API = f"https://api.sdbots.tk/chk?cc={cc}"
    req = requests.get(API).json()
    return(req)

def sk_checker(key):
    req = requests.get(f"https://api.sdbots.tk/sk?key={key}").json()
    return(req)

def lyrics(song):
    req = requests.get(f"https://api.sdbots.tk/lyrics?song={song}").json()
    return(req)

def ipinfo(ip):
    req = requests.get(f"https://api.sdbots.tk/ipinfo?ip={ip}").json()
    return(req)

def hirunews():
    req = requests.get("https://api.sdbots.tk/hirunews").json()
    return(req)

def logohq(text):
    req = requests.get(f"https://api.sdbots.tk/logohq?text={text}").url
    return(req)

def fakeinfo():
    req = requests.get("https://api.sdbots.tk/fakeinfo").json()
    return(req)


a = anime_logo("DamanthaJa")
print(a)