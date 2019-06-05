from celery import shared_task

from .cve_downloader import create_directory_structure, download_and_unzip_cve_files_from_nvd
from .cve_parser import main as cve_parser_task
from .most_vulnerable_vendors import main as vendors_analyser_task
from .cvss import main as cvss_analyzer_task


@shared_task
def downloader():
    print('Downloader started')
    create_directory_structure()
    download_and_unzip_cve_files_from_nvd()
    print('Downloader finished')


@shared_task
def parser():
    print('Parser started')
    cve_parser_task()
    print('Parser finished')


@shared_task
def vendors_analyser():
    print('Vendors analyser started')
    vendors_analyser_task()
    print('Vendors analyser finished')


@shared_task
def cvss_analyzer():
    print('CVSS analyzer started')
    cvss_analyzer_task()
    print('CVSS analyzer finished')
