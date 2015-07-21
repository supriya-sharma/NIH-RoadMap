import os
import os.path
from robobrowser import RoboBrowser
import shutil
from urllib2 import urlopen


browser = RoboBrowser()

EXP_BASE_URL = 'http://genboree.org/EdaccData/Release-9/experiment-sample/'
SAMPLE_BASE_URL = 'http://genboree.org/EdaccData/Release-9/sample-experiment/'
BASE_URL = ''


def get_gz_urls(base_url):
    browser.open(base_url)
    all_links = []
    for link in browser.select('a'):
        link_href = link['href']
        if link_href.endswith('.gz'):
            all_links.append(link_href)
    return all_links


def filter_by_filetypes(links, valid_filetypes=['bed', 'wig', 'sra']):
    for filetype in valid_filetypes:
        type_links = []
        for link in links:
            if link.endswith(filetype + '.gz'):
                type_links.append(link)
        if type_links:
            return type_links
    return []


def get_subdirectories(url):
    browser.open(url)
    links = []
    for link in browser.select('a'):
        href = link['href']
        if href != '../':
            links.append(href)
    return links


def download_url(source_url, dest_filename):
    # print "in for testing... would download"
    # print source_url
    # print "to"
    # print dest_filename
    # return
    url = urlopen(source_url)
    fout = open(dest_filename, 'wb')
    shutil.copyfileobj(url, fout)
    fout.close()
    url.close()



def download_files(urls, dest_dir='./'):
    abs_dest_dir = os.path.abspath(dest_dir)
    if not os.path.exists(abs_dest_dir):
        os.makedirs(abs_dest_dir)
    for url in urls:
        url_parts = url.split('/')
        filename = url_parts[-1]
        full_name = os.path.join(abs_dest_dir, filename)
        download_url(url, full_name)
            


