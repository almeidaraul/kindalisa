from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from skimage.io import imread

class Searcher():
    def __init__(self, terms):
        """terms: list of strings to be searched"""
        self.terms = terms
        self.images = { t: [] for t in self.terms }

    def get_images(self, quantity):
        """
        for each search term, get the first (quantity) images from duckduckgo
        """
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        for t in self.terms:
            imgs = []
            url = "https://duckduckgo.com/?t=canonical&q="\
                  "{}+blackpink&atb=v241-6__&iax=images"\
                  "&ia=images".format(t)
            
            driver.get(url)
            image_elements = []
            while not len(image_elements):
                image_elements = driver.find_elements_by_class_name("tile--img__img")

            images = []
            for i in image_elements[:quantity]:
                images.append(imread(i.get_attribute('src')))
            self.images[t] = images
        driver.quit()
            

# test = Searcher(['lisa', 'jennie', 'jisoo', 'rose'])
# test.get_images(10)
# print(test.images)
