from random import choice
from string import digits, ascii_lowercase
import requests, fake_headers
from os.path import getsize
from os import remove
import threading


BASE_URL = "https://i.imgur.com/"
CHARACTERS = digits + ascii_lowercase
IMAGE_EXTENTIONS = [".webp", ".png", ".jpg"]
IMAGE_COUNTER = 0
THREADS = 12


def generate_urlId() -> str:
    return "".join([choice(CHARACTERS) for _ in range(6)]) + choice(IMAGE_EXTENTIONS)


def download() -> None:
    print("Starting download!")
    urlId = generate_urlId()
    url = BASE_URL + urlId
    filename = "images/" + urlId

    with open(filename, "wb") as f:
        f.write(requests.get(url, headers=fake_headers.make_header()).content)

    if getsize(filename) < 10000:
        print(f"Download failed for {urlId}")
        return remove(filename)
   
    global IMAGE_COUNTER
    IMAGE_COUNTER += 1
    print(f"[{IMAGE_COUNTER}] {urlId}")


while True:
    threads = [threading.Thread(target=download) for _ in range(THREADS)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    



