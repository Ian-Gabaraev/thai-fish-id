import ast
import threading
import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

urls_str = os.getenv('URLS')
urls = ast.literal_eval(urls_str)
root_folder = 'media'


def create_folder(dir_name):

    dir_path = os.path.join(root_folder, dir_name)
    dir_path = os.path.join('..', dir_path)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    return dir_path


def download_image(image_url, filepath):
    response = requests.get(image_url)
    with open(filepath, 'wb') as f:
        f.write(response.content)


def extract_fish_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    fish_info = []
    divs = soup.find_all('div', {'class': 'et_pb_gallery_item'})

    fish_name = image_link = None

    for div in divs:
        h3 = div.find('h3')
        if h3:
            fish_name = h3.text

        image_div = div.find('div', {'class': 'et_pb_gallery_image'})
        if image_div and image_div.a and image_div.a.has_attr('href'):
            image_link = image_div.a['href']

        if fish_name and image_link:
            fish_info.append((fish_name, image_link))

    return fish_info


def download_fish_images(url):
    url_parts = url.strip('/').split('/')
    fish_type = url_parts[-1]
    dir_name = create_folder(fish_type)

    response = requests.get(url)
    if not response.ok:
        print(f"Failed to download page: {url}")
        return

    fish_info = extract_fish_info(response.content)
    threads = []

    for fish_name, image_link in fish_info:
        filename = f'{fish_name}.jpg'
        filepath = os.path.join(dir_name, filename)

        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            print(f"\tSaving fish: {fish_name}")
        else:
            continue

        t = threading.Thread(target=download_image,
                             args=(image_link, filepath))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    threads = []

    for url in urls:
        t = threading.Thread(target=download_fish_images, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
