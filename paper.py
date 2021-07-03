import requests
from util import Util
from custom_typing import (String, Integer, JsonDict)


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
