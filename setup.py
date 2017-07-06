from distutils.core import setup
import py2exe


setup(
    console=['Test.py'],
    options = {
        'py2exe':{
            'packages':['flickrapi'],
            'packages':['xml.etree'],
            'packages':['pyperclip']}})

