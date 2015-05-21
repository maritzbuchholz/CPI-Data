import urllib2
from BeautifulSoup import BeautifulSoup, SoupStrainer
import re

site = urllib2.urlopen("http://download.bls.gov/pub/time.series/cu/").read()


soupstrainerBeautifulSoup(site)

#site = BeautifulSoup(site)

#linksToBob = SoupStrainer(site, href=re.compile('/pub/time.series/cu/cu.data'))

#print linksToBob
