    microwave
    ---------

    microwave is a simple tool to hit a lot of URLs on your site
    at once provided you have a sitemap.xml. The intention of this
    is that it will enable you to have a "warmed" cache so that when
    real traffic is encountered, very little of the requests
    do any real work.

    It also displays status codes for handy 404 detection.

   
    Installation
    ------------

    Clone, make a python 2 (because gevent) virtualenv, and then
    pip install -r requirements.txt


    Usage:
        microwave [--ssl] <domain>
        microwave -h | --help
        microwave --version

    Options:
        -h --help                   Show this screen.
        --version                   Show version.
        --ssl                       Use HTTPS.
