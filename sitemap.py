from urlparse import urlparse as parser
import urlparse
import urllib2
from urllib2 import HTTPError
from cgi import escape
from BeautifulSoup import BeautifulSoup as Bs
import sys


def domain_name(url):
    """
    This function will take a url and filter out the domain name from it
    :param url: Takes a URL in the form of http://www.redhat.com
    :return: It will return the domain name redhat.com
    """
    dom = parser(url).netloc
    domain = dom.split('.')
    if 'www' in domain:
        return domain[0]+'.'+domain[1]+'.'+domain[2]
    else:
        return domain[0]+'.'+domain[1]


def web_crawler(url):
    """
    This Function will crawl the website and return the list of links on the same
    :param url: Takes a URL in the form of http://www.redhat.com
    :return: It will return list of all links in the URL
    """
    url_list = []
    req = urllib2.Request(url)
    handle = urllib2.build_opener()
    domain = domain_name(url)
    if handle:
        content = handle.open(req).read()
        soup = Bs(content)
        tags = soup('a')
        for tag in tags:
            href = tag.get('href')
            if href is not None:
                url = urlparse.urljoin(url, escape(href))
                if domain in url:
                    url_list.append(url)
    return url_list


if __name__ == '__main__':
    try:
        url = str(sys.argv[1])
        links_list = set(web_crawler(url))
        print '\n'.join(links_list)
        for links in links_list:
            print "\n The links inside " + links
            try:
                print '\n'.join(set(web_crawler(links)))
                if HTTPError:
                    print "Getting 404 Response from this URL"
                    continue
            except Exception:
                print "Link may be Invalid or getting redirected to some other URL"
    except Exception:
        print "Invalid address given. Please try again with valid web address"
