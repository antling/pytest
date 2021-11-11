import zipfile
with zipfile.ZipFile(r'D:\work\appserver_zip', 'r') as zip_ref:
    zip_ref.extractall('c:/wuda')
