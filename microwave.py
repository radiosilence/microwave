#!/usr/bin/env python
import requests
import gevent
from gevent import monkey
monkey.patch_socket()
monkey.patch_ssl()

from docopt import docopt
from bs4 import BeautifulSoup


NAME = 'microwave'
VERSION = '0.1'
AUTHOR = 'James Cleveland'
SHORT_DESC = 'cache warmer'

__doc__ = """{2}

Usage:
    {0} [--ssl] <domain>
    {0} -h | --help
    {0} --version

Options:
    -h --help                   Show this screen.
    --version                   Show version.
    --ssl                       Use HTTPS.
""".format(
    NAME,
    VERSION,
    SHORT_DESC
)

def touch(url):
    r = requests.get(url)
    print('[{1}] {0}'.format(url, r.status_code))

def microwave(domain, ssl=False):
    if ssl:
        protocol = 'https://'
    else:
        protocol = 'http://'
    r = requests.get('{protocol}{domain}/sitemap.xml'.format(
        protocol=protocol,
        domain=domain
    ))
    soup = BeautifulSoup(r.content)
    gevent.joinall([
        gevent.spawn(touch, url.get_text()) for url in soup.find_all('loc')
    ])
    
    print u'\nDING!\n'


def main():
    args = docopt(__doc__, version='{} {}'.format(
        NAME,
        VERSION))
    microwave(args['<domain>'], ssl=args['--ssl'])

if __name__ == '__main__':
    main()
