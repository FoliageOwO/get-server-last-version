from bs4.element import ResultSet
from typing import (List, Dict)
from custom_typing import (JsonDict, String)
from bs4 import BeautifulSoup


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
