from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from skimage.io import imread


def scrape_duckduckgo_images(search_term, quantity, driver=None):
    """Get first `quantity` images from DDG query of each search term"""
    if driver is None:
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
    url = "https://duckduckgo.com/?t=canonical&q="\
          f"{search_term}&atb=v241-6__&iax=images"\
          "&ia=images"

    driver.get(url)
    class_name = "tile--img__img"
    image_elements = []
    while not len(image_elements):
        image_elements = driver.find_elements_by_class_name(class_name)

    def get_image(el): return imread(el.get_attribute('src'))
    images = list(map(get_image, image_elements[:quantity]))
    driver.quit()
    return images


if __name__ == "__main__":
    names = ["lisa", "jennie", "jisoo", "rose"]
    search_terms = [f"{name}+blackpink" for name in names]
    for t in search_terms:
        scrape_duckduckgo_images(t, 10)
