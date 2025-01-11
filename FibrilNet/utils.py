import requests
import shutil
import os 

def download_file(local_filename, url):
    result = True
    print('Downloading the file:',local_filename,', please waint until it finishes.')
    try:
        with requests.get(url, stream=True) as r:
            with open(local_filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
    except Exception as e:
        print('Unable to download the SDNN model file. You must download the file manually from the url:', url)
        print('Error from the download process is:', e)
        result = False
    return result

def download_model():
    url ='https://web.njit.edu/~wangj/deepsuncode/FibrilNet/model.hdf5'
    filename = 'model' + os.sep +url.split('/')[-1]
    if os.path.exists(filename):
        print('File:',filename,'already exists, no need to download it')
    else:
        os.makedirs('model',exist_ok=True)
        if download_file(filename,url):
            print('Finished dowloading the file.')


        