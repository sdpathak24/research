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
    url ='https://web.njit.edu/~wangj/deepsuncode/SDNN/pretrained_model.h5'
    filename = url.split('/')[-1]
    if os.path.exists(filename):
        print('File:',filename,'already exists, no need to download it')
    else:
        if download_file(filename,url):
            print('Finished dowloading the file.')

def download_fits():
    url ='https://web.njit.edu/~wangj/deepsuncode/SDNN/cals_170713_162012.fts'
    filename = url.split('/')[-1]    
    filename = 'inputs' + os.sep + filename
    if os.path.exists(filename):
        print('File:',filename,'already exists, no need to download it')
    else:
        os.makedirs('inputs',exist_ok=True)
        if download_file(filename,url):
            print('Finished dowloading the file.')

        