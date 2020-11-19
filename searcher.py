from selenium import webdriver

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
                  "{}+blackpink&atb=v241-6__&iax=images"\
                  "&ia=images".format(t)
            
            driver = webdriver.Firefox()
            driver.get(url)
            images = driver.find_elements_by_class_name("tile--img__img")
            print("Found {} images for {}, first element is {}".format(len(images), t, images[0]))

test = Searcher(['lisa', 'jennie', 'jisoo', 'rose'])
test.get_images(3)
