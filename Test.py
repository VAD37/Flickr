from flickrapi import FlickrAPI
from xml.etree import ElementTree as ET
import pyperclip
class keys:
    apikey = u"6ac162e31528ac235870856eadce38d1"
    apisecret = u"1c01580225bb447c"

print('Dang nhap vao flickr')
flickr = FlickrAPI(keys.apikey, keys.apisecret)

# ------------------------------------------------------------------------------

flickr.authenticate_via_browser(perms='delete')

ID = "151892798@N03"

sets= flickr.photosets_getList(user_id='151892798@N03' , format='etree')

def embed(album_id):
    ALBUM = flickr.photosets.getPhotos(user_id=ID,photoset_id= album_id)

    print('Ma san pham: ',ALBUM[0].get('title'))
    total = int(ALBUM[0].get('total'))

    empty=('')
    for i in range(total):
        D = flickr.photos.getInfo(photo_id = ALBUM[0][i].get('id'))
        ID_SECRET = str( D[0].get('originalsecret'))
        title = ALBUM[0][i].get('title')
        title = title.replace("-"," ")
        title = title.replace("_", " ")
        title = title.replace("copy","")

        try:
          #  print( '<a title="'+ title+ '"><img src="' +
          #         'https://c1.staticflickr.com/' + str(ALBUM[0][i].get('farm')) +
          #        '/' + str(ALBUM[0][i].get('server'))+'/'
           #        + ALBUM[0][i].get('id') + '_' + ID_SECRET + '_o.jpg" alt="' +  title + '"></a>'
           #        )
        
            empty+=('<a title="'+ title+ '"><img src="' +
                   'https://c1.staticflickr.com/' + str(ALBUM[0][i].get('farm')) +
                   '/' + str(ALBUM[0][i].get('server'))+'/'
                   + ALBUM[0][i].get('id') + '_' + ID_SECRET + '_o.jpg" alt="' +  title + '"></a>'+'\n'
                   )

        except IndexError:
            print('error')
    print("Da copy vao trong clipboard")
    pyperclip.copy(empty)
    spam = pyperclip.paste()
def main():
    Input = input("Dua duong link album tren flickr hoac ma so cua album flickr: ")
    while Input!="QUIT":
        #ten =   Input[ (Input.rfind('sets') +4):]
        ten =    (Input.split('/') )
        try:
            t = ten[6]
        except:
            print("Sai duong Link")
        print('\n')
        try:
            embed(t)
        except:
            print("Sai duong link")
        print('\n')
        Input = input("Duong dan Album khac: ")



main()
