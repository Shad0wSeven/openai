import urllib.request 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
urllib.request.urlretrieve("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4", 'test.mp4') 