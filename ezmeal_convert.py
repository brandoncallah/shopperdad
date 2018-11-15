import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import requests
import wget

def emeals_login():

    cj = cookielib.CookieJar()
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_cookiejar(cj)
    br.open("https://emeals.com/account/login.php")

    br.select_form(nr=0)
    br.form['amember_login'] = ''
    br.form['amember_pass'] = ''
    br.submit()

    print br.response().read()

def get_pdf():

    url = "http://emeals.com/account/download.php?id=366&plan=current"
    filename = wget.download(url)

emeals_login()
get_pdf()