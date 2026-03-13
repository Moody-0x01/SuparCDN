#!/bin/python
from os import scandir
import time

from requests import get
from json import loads
from methods import *

total = 5
Avatars = [entry.path for entry in scandir('./img/avatars/')][:total]
backgrounds = [entry.path for entry in scandir('./img/backgrounds/')][:total]
responses = []
success = 0

def test_avatar_store():
    global success, total, responses
    success = 0

    for i, img in enumerate(Avatars):
        with open(img, "rb") as fp:
            uuid = i
            mime = MakeMime(fp)
            print(f"Sending #{i} {img}")
            time.sleep(1)
            response = addAvatar(uuid, mime)
            if response.status_code == 200: success += 1
            else: print(response)
            responses.append(response)

def test_avatar_access():
    global success, total
    success = 0
    for res in responses:
        url = loads(res.content)['data']['url']
        print(url)
        data = get(url)
        print(data.status_code)
        print(data.content)

def test_bg_store():
    global success, total
    success = 0
    for  i, background in enumerate(backgrounds):
            uuid = i
            print(f"Sending #{i} {background}")
            with open(background, "rb") as fp:
                mime = MakeMime(fp)
                # time.sleep(0.2)
                response = addbg(uuid, mime)
                if response.status_code == 200 || : success += 1
                # else: print(response)
                responses.append(response)
def main():
    test_avatar_store ()
    print(f"[STORE AVA ][ {success} / {total} ]")
    test_avatar_access()
    test_bg_store()
    print(f"[STORE BACK][ {success} / {total} ]")

if __name__ == "__main__": main()
