from random import choice
from string import digits, ascii_lowercase
import requests, fake_headers
from os.path import getsize
from os import remove


BASE_URL = "https://i.imgur.com/"
CHARACTERS = digits + ascii_lowercase
IMAGE_EXTENTIONS = [".webp", ".png", ".jpg"]
IMAGE_COUNTER = 0


def generate_urlId() -> str:
    return "".join([choice(CHARACTERS) for _ in range(6)]) + choice(IMAGE_EXTENTIONS)


def download(urlId: str) -> None:
    filename = "images/" + urlId

    with open(filename, "wb") as f:
        f.write(requests.get(BASE_URL + urlId, headers=fake_headers.make_header()).content)

    if getsize(filename) < 10000:
        return remove(filename)
   
    global IMAGE_COUNTER
    IMAGE_COUNTER += 1
    print(f"[{IMAGE_COUNTER}] {urlId}")


while True:
    download(generate_urlId())

