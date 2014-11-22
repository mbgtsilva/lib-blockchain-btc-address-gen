'libbcbtcag - A library for generating Bitcoin Public and Private keys in unison using Blockchain.info 's wallet generator.'
'GNU GPL v3.0 or above - <http://gnu.org/licenses/gpl.txt>'

import urllib

def generate(use_https):
    if use_https == True:
        protocol = "https://"
    else protocol = "http://"
    return urllib.request.urlopen(protocol + "blockchain.info/q/newkey")

def get_version():
    return "1.0"
