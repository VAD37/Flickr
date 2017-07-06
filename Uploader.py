#!/usr/bin/env python

from xml.etree import ElementTree as ET
import logging
import webbrowser
from os import walk
#logging.basicConfig(level=logging.INFO)
import string

from flickrapi import FlickrAPI

class keys:
    apikey = u"6ac162e31528ac235870856eadce38d1"
    apisecret = u"1c01580225bb447c"
    apikey2="68fcfa3118c47edee89c57f231137112"
    apisecret2="a7f01e5e43b0004e"
def read_file(direction):
    file = (direction)
    file=file.replace('\\' , '//')
    d=walk(file)
    album_title=''
    album_id=''
    tong=0
    for (x,y,z) in d:
        for i in z:
            I=i.replace('-',' ')
            I=I.replace('_', ' ')
            I=I.replace('.jpg','')
            I=I.replace('copy','')
            
            t=I.split(' ')
            for x in t:
                for a in x:
                    if a.isdigit() == True:
                        match = t.index(x)
                        break
                if a.isdigit()==True:
                    break
            if i!="Thumbs.db":
                ma_sp = t[match].translate(str.maketrans('','',string.ascii_lowercase))
            else:
                ma_sp=' '
            print("San Pham: ",ma_sp)
            f= file + '//' + i
            #print('dia chi: ',f)
            print('Ten anh: ',I)
            print('Dang anh moi')
            try:
                    
                anh = flickr.upload(filename = f , title = I.replace('copy',''),tags = ma_sp ,is_public=1, is_friend=1, is_family=1)
                tong+=1
                p_id = anh.findtext('photoid')
                #print('photo id ', p_id)
                if album_title != ma_sp:
                    album_title= ma_sp
                    #Tao album moi
                    A = flickr.photosets.create(title =album_title,primary_photo_id = p_id)
                    
                    album_id = A[0].get('id')
                    print('Tao album moi cho ',album_title)
                    #print('Album id: ',album_id)
                else:
                    flickr.photosets.addPhoto(photoset_id = album_id , photo_id = p_id)
                    print('Them anh vao album:',ma_sp)
                print("TONG SO ANH DA DANG:",tong)
                print('\n')
            except:
                print("Khong phai la file anh. Chuyen sang file tiep theo\n")
def album():
    
    return
def remove(d):
    return

print('Dang nhap vap flickr')
flickr = FlickrAPI(keys.apikey2,keys.apisecret2)
flickr.authenticate_via_browser(perms='delete')



#photo_id = photo.findtext('photoid')
#print(photo_id)
#flickr.photosets.create(title = 'test',primary_photo_id = photo_id)
def main():
 #   photo = flickr.upload(filename = 'test.jpg',title = 'test2', is_public=1, is_friend=1, is_family=1)
    #file="E:\experiment\WEB"
    print("Bo cac file khong la anh de dang anh len nhanh hon.")
    print("Tat ca anh trong folder deu phai co ma so trong ten.")
    print("Neu ko ten va ma so anh khi dang len se sai.")
    print("Vi du file anh: xxx - TK0390.jpg , xxx _ TK3902.jpg deu se nhan dang dc.")
    while True:
        INPUT= input("Folder anh tren PC: ")
        read_file(INPUT)

main()



