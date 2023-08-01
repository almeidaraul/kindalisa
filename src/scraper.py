import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from skimage.io import imread, imsave


def scrape_duckduckgo_images(search_term, quantity, driver=None):
    """Get first `quantity` images from DDG query of each search term"""
    if driver is None:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        home_dir = os.path.expanduser("~")
        webdriver_service = webdriver.chrome.service.Service(
            f"{home_dir}/chromedriver/stable/chromedriver")
        driver = webdriver.Chrome(service=webdriver_service, options=options)
    url = "https://duckduckgo.com/?t=canonical&q="\
          f"{search_term}&atb=v241-6__&iax=images"\
          "&ia=images"

    driver.get(url)
    class_name = "tile--img__img"
    image_elements = []
    while image_elements == []:
        image_elements = driver.find_elements(By.CLASS_NAME, class_name)

    def get_image(el): return imread(el.get_attribute('src'))
    images = list(map(get_image, image_elements[:quantity]))
    driver.quit()
    return images


if __name__ == "__main__":
    names = ["lisa", "jennie", "jisoo", "rose"]
    search_terms = [f"{name}+blackpink" for name in names]
    for i0, t in enumerate(search_terms):
        imgs = scrape_duckduckgo_images(t, 10)
        home_dir = os.path.expanduser("~")
        for i, img in enumerate(imgs):
            imsave(f"/home/raul/kindalisa/src/{i0}_{i}.png", img)
