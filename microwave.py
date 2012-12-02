#!/usr/bin/env python
import requests
import gevent
from docopt import docopt
from bs4 import BeautifulSoup


NAME = 'microwave'
VERSION = '0.1'
AUTHOR = 'James Cleveland'
SHORT_DESC = 'cache warmer'

__doc__ = """{2}

Usage:
    {0} <domain>
    {0} -h | --help
    {0} --version

Options:
    -h --help                   Show this screen.
    --version                   Show version.
""".format(
    NAME,
    VERSION,
    SHORT_DESC
)

def touch(url):
    r = requests.get(url)
    print('[{1}] {0}'.format(url, r.status_code))

def microwave(domain):
    r = requests.get('http://{}/sitemap.xml'.format(domain))
    soup = BeautifulSoup(r.content)
    gevent.joinall([
        gevent.spawn(touch, url.get_text()) for url in soup.find_all('loc')
    ])


def main():
    args = docopt(__doc__, version='{} {}'.format(
        NAME,
        VERSION))
    microwave(args['<domain>'])

if __name__ == '__main__':
    main()
