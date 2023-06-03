import requests
import os
import urllib.error
import urllib.request

def mkdir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def elapsed_time_str(seconds):
    seconds=int(seconds + 0.5)
    h=seconds//3600
    m=(seconds-h*3600)//60
    s=seconds-h*3600-m*60 
    return f"{m:02}-{s:02}"

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as error:
        print(error)

def download_img(img):
    url = 'https://api.trace.moe/search?url='+img
    r = requests.get(url)
    data = r.json()
    eposode="episode-"+str(data['result'][0]['episode'])
    from_t="_from-"+str(elapsed_time_str(round(data['result'][0]['from'])))
    to_t="_to-"+str(elapsed_time_str(round(data['result'][0]['to'])))
    name=eposode+from_t+to_t
    download_file(img, "img_out/"+name+".jpg")

if __name__ == "__main__":
    mkdir("img_out")
    with open('url.txt', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\r\n')
            download_img(line)