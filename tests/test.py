#!/bin/python
from os import scandir
import time

from requests import get
from json import loads
from methods import *

Avatars = [entry.path for entry in scandir('./img/avatars/')][:5]
responses = []
success = 0
total = len(Avatars)

def test_avatar_store():
    global success, total, responses
    success = 0
    total = len(Avatars)

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
    total = len(Avatars)
    for res in responses:
        url = loads(res.content)['data']['url']
        print(url)
        input("Press to continue :)")
        data = get(url)
        print(data.status_code)
        print(data.content)
def main():
    test_avatar_store ()
    print(f"[STORE ][ {success} / {total} ]")
    test_avatar_access()
    # print(f"[ACCESS][ {success} / {total} ]")

if __name__ == "__main__": main()
