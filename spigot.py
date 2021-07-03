import requests
from bs4 import BeautifulSoup
from typing import (AnyStr, List, Dict)
from util import Util
from custom_typing import (JsonDict, RequestResponse)


def get_spigot() -> JsonDict:
    response: RequestResponse = requests.get('https://getbukkit.org/download/spigot')
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')

    downloadResponse: RequestResponse = requests.get(soup.select('#downloadr')[0]['href'])
    downloadSoup: BeautifulSoup = BeautifulSoup(downloadResponse.text, 'html.parser')

    json: JsonDict = {
        'version': Util.oneKey('#download > div > div > div > div:nth-child(1) > div > div:nth-child(1) > h2', soup),
        'size': Util.oneKey('#download > div > div > div > div:nth-child(1) > div > div.col-sm-2 > h3', soup),
        'date': Util.dateFormatter(Util.oneKey('#download > div > div > div > div:nth-child(1) > div > div:nth-child(3) > h3', soup)),
        'download_url': downloadSoup.select('#get-download > div > div > div > div > h2 > a')[0]['href']}
    return json
