import requests
from typing import (AnyStr, Dict, Any)
from bs4 import BeautifulSoup
from bs4.element import ResultSet

String = AnyStr
JsonDict = Dict[String, Any]
Integer = int
RequestResponse = requests.Response

class Util(object):
    @staticmethod
    def toText(resultSet: ResultSet) -> String:
        return str(list(resultSet)[0])

    @staticmethod
    def removeTag(string: String) -> String:
        return string.replace('<h2>', '').replace('</h2>', '') \
            .replace('<h3>', '').replace('</h3>', '') \
            .replace('<h4>', '').replace('</h4>', '')

    @staticmethod
    def oneKey(selectString: String, soup: BeautifulSoup) -> String:
        return Util.removeTag(Util.toText(soup.select(selectString)))

    @staticmethod
    def UTCFormatter(dateString: String) -> String:
        dateList: List[String] = dateString.split('T')
        time: String = dateList[1].replace('Z', '')
        return f'{dateList[0]} {time}'

    @staticmethod
    def dateFormatter(dateString: String) -> String:
        dateList: List[String] = dateString.split(' ')
        dateList.remove(dateList[0])
        monthMapping: List[String] = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December']
        monthIndex = str(monthMapping.index(dateList[0]) + 1)
        month = ('0' + monthIndex) if len(monthIndex) == 1 else monthIndex
        return f'{dateList[2]}-{month}-{dateList[1]}'

def get_paper() -> JsonDict:
    projectsLastVersion: String = requests.get('https://papermc.io/api/v2/projects/paper/').json()['versions'][-1]
    buildLast: Integer = requests.get(f'https://papermc.io/api/v2/projects/paper/versions/{projectsLastVersion}').json()['builds'][-1]
    lastJson: JsonDict = requests.get(
        f'https://papermc.io/api/v2/projects/paper/versions/{projectsLastVersion}/builds/{buildLast}').json()
    downloadName: String = lastJson['downloads']['application']['name']

    json: JsonDict = {
        'version': projectsLastVersion,
        'build': buildLast,
        'date': Util.UTCFormatter(lastJson['time']),
        'download_url': f'https://papermc.io/api/v2/projects/paper/versions/{projectsLastVersion}/builds/{buildLast}/downloads/{downloadName}'}
    return json

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

def get_vanilla() -> JsonDict:
    response: RequestResponse = requests.get('https://getbukkit.org/download/vanilla')
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')

    downloadResponse: RequestResponse = requests.get(soup.select('#downloadr')[0]['href'])
    downloadSoup: BeautifulSoup = BeautifulSoup(downloadResponse.text, 'html.parser')
    downloadUrl: String = downloadSoup.select('#get-download > div > div > div > div > h2 > a')[0]['href']

    json: JsonDict = {
        'version': Util.oneKey('#download > div > div > div > div:nth-child(1) > div > div:nth-child(1) > h2', soup),
        'size': Util.oneKey('#download > div > div > div > div:nth-child(1) > div > div.col-sm-2 > h3', soup),
        'date': Util.dateFormatter(Util.oneKey('#download > div > div > div > div:nth-child(1) > div > div:nth-child(3) > h3', soup)),
        'download_url': downloadUrl,
        'boost_download_url': downloadUrl.replace('https://launcher.mojang.com', 'https://download.mcbbs.net')}
    return json
