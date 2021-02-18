from urllib.request import urlopen
from bs4 import BeautifulSoup
from pathlib import Path
import requests
import json
import os


def read(url, savepath):
    r = requests.get(url)
    Path(os.path.dirname(savepath)).mkdir(parents=True, exist_ok=True)
    write_file(savepath, r.text)


def write_file(name, data):
    out = open(name, 'w')
    out.write(data)
    out.close()


def resolve(url):
    html = urlopen(url)
    return BeautifulSoup(html, 'html.parser')


def toJson(data, noindent=False):
    if noindent:
        return json.dumps(data, ensure_ascii=False)
    else:
        return json.dumps(data, ensure_ascii=False, indent=2)


def readDate(dateString):
    return parser.parse(dateString).strftime('%Y%m%d')


def toSnake(string):
    string = string.replace(' ', '_')
    string = string.replace('-', '_')
    string = string.replace('\'', '_')
    string = string.replace('&', '_')
    return string


def codefix(name):
    if name == "hunwoo":
        return "hyunwoo"
    if name == "sniper":
        return "sniper_rifle"
    if name == "twin_sword":
        return "dual_sword"
    if name == "throw":
        return "throwing"
    if name == "lidailin":
        return "li_dailin"
    if name == "dáinsleif":
        return "dainsleif"
    if name == "thuận_thiên_":
        return "thuan_thien"
    if name == "twin_swords":
        return "twin_sword"
    if name == "nirvana_gauntlet":
        return "gauntlet"
    if name == "walther_ppk":
        return "walter_ppk"
    if name == "bloodwing_knuckles":
        return "bloodwing_knuckle"
    if name == "wing_knuckles":
        return "wing_knuckle"
    if name == "iron_knuckles":
        return "iron_knuckle"
    if name == "glass_knuckles":
        return "glass_knuckle"
    if name == "single_coil_pickup":
        return "single_pickup"
    if name == "vintage_cards":
        return "vintage_card"
    return name
