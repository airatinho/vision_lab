import os
import requests

PATH = "" # all files in this path(directory) - are images
URL = "" + "/images" #server URL addres

def send_images(path_img:str=PATH,url:str=URL)->None:
    """Send images from folder to server"""
    for i in os.listdir(path_img):
        with open(path_img+f'/{i}','rb') as img:
            params = {'img':img}
        responce=requests.post(url,params=params)
        if responce.status_code!=200:
            print(f"Some error with post request, response {responce.status_code}")
        print(f'Image {i} sended!')

if __name__ == "__main__":
    send_images() #call function