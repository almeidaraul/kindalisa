import requests
import urllib.request
import time
from bs4 import BeautifulSoup

class Searcher():
    def __init__(self, terms):
        """terms: list of strings to be searched"""
        self.terms = terms
        self.images = { t: [] for t in self.terms }

    def get_images(self, quantity):
        """
        for each search term, get (quantity) images from duckduckgo
        """
        for t in self.terms:
            imgs = []
            url = "https://duckduckgo.com/?t=canonical&q="\
                  "{}&atb=v241-6__&iax=images"\
                  "&ia=images".format(t)
            response = requests.get(url)

            soup = BeautifulSoup(response.text, "html.parser")

test = Searcher(['lisa+blackpink', 'jennie+blackpink', 'jisoo+blackpink', 'rose+blackpink'])
