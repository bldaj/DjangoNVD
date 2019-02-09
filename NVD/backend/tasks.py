from celery import shared_task

from .cve_downloader import create_directory_structure, download_and_unzip_cve_files_from_nvd


@shared_task
def downloader():
    create_directory_structure()
    download_and_unzip_cve_files_from_nvd()
