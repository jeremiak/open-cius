from os import listdir, system
from subprocess import call

import requests

download_dest_path = '/data/downloads'
raw_dest_path = '/data/raw'
file_urls = {
    '2006': 'https://www2.fbi.gov/ucr/cius2006/documents/cius2006datatables.zip',
    '2007': 'https://www2.fbi.gov/ucr/cius2007/documents/cius2007datatables.zip',
    '2008': 'https://www2.fbi.gov/ucr/cius2008/documents/cius2008datatables.zip',
    '2009': 'https://www2.fbi.gov/ucr/cius2009/documents/cius2009datatables.zip',
    '2010': 'https://ucr.fbi.gov/crime-in-the-u.s/2010/crime-in-the-u.s.-2010/CIUS2010downloadablefiles.zip',
    '2011': 'https://ucr.fbi.gov/crime-in-the-u.s/2011/crime-in-the-u.s.-2011/CIUS2011datatables.zip',
    '2012': 'https://ucr.fbi.gov/crime-in-the-u.s/2012/crime-in-the-u.s.-2012/resource-pages/cius2012datatables.zip',
    '2013': 'https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/resource-pages/downloads/cius2013datatables.zip',
    '2014': 'https://ucr.fbi.gov/crime-in-the-u.s/2014/crime-in-the-u.s.-2014/resource-pages/downloads/cius2014datatables.zip'
}

def download(url):
    local_filename = '%s/%s' % (download_dest_path, url.split('/')[-1])
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)  # filter out keep-alive new chunks
    return local_filename

print('Downloading years (%s) to %s' % (','.join(file_urls.keys()), download_dest_path))
for url in file_urls.values():
    download(url)

print('Unzipping files to %s' % raw_dest_path)
zip_files = [f for f in listdir(download_dest_path) if '.zip' in f]
for zip_file in zip_files:
    zip_path = '%s/%s' % (download_dest_path, zip_file)
    dest_filname = zip_file.split('.zip')[0]
    dest_filepath = '%s/%s' % (raw_dest_path, dest_filname)
    system('mkdir -p %s' % dest_filepath)
    system('unzip %s -d %s' % (zip_path, dest_filepath))
