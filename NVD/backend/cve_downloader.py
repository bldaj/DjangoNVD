import os
import gzip
import json
from datetime import datetime

import requests

from NVD.settings import START_YEAR

url = 'https://nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-{0}.json.gz'
archive_name = 'cve-{0}.json'


def create_directory_structure():
    if not os.path.exists('backend/CVEs'):
        os.mkdir('backend/CVEs')

    if not os.path.exists('backend/CVEs/Archives'):
        os.mkdir('backend/CVEs/Archives')

    if not os.path.exists('backend/CVEs/JSONs'):
        os.mkdir('backend/CVEs/JSONs')

    if not os.path.exists('backend/CVEs/CSV'):
        os.mkdir('backend/CVEs/CSV')


def read_archive(file_name: str):
    with gzip.open('backend/CVEs/Archives/{0}.gz'.format(file_name), 'rb') as f:
        print('Reading archive: {0}'.format(file_name + '.gz'))
        return f.read()


def save_archive(file_name: str, content: bytes) -> None:
    with open('backend/CVEs/Archives/{0}.gz'.format(file_name), 'wb') as f:
        print('Saving archive: {0}'.format(file_name + '.gz'))
        f.write(content)


def save_json(file_name: str, content) -> None:
    if isinstance(content, str):
        content = json.loads(content)
    elif isinstance(content, dict):
        pass
    else:
        raise TypeError

    with open('backend/CVEs/JSONs/{0}'.format(file_name), 'w') as f:
        json.dump(content, f)


def create_link_from_year(year: int) -> str:
    return url.format(year)


def create_archive_name_from_year(year: int) -> str:
    return archive_name.format(year)


def download_and_unzip_cve_files_from_nvd():
    current_year = datetime.now().year

    for year in range(START_YEAR, current_year):
        file_name = create_archive_name_from_year(year)

        save_archive(
            file_name=file_name,
            content=requests.get(create_link_from_year(year)).content
        )

        save_json(
            file_name=file_name,
            content=read_archive(file_name=file_name).decode()
        )
