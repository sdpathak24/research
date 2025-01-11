from utils import *

# Note that the SDDN has large model and fits files that can not
# be saved in public repository. Therefore, they must be downloaded first.
download_model()
download_fits()


from astropy.io import fits
import os
import time
import numpy as np
from SDNN import read_data
from SDNN import inverse
from SDNN import save_results

# Import the load_model() function from SDNN module.

from SDNN import load_model
model = load_model()

# You may set up your own data directory.

input_path = 'inputs'  # edit your input path
output_path = 'outputs'  # edit your output path





for file in os.listdir(input_path):
    print('---------- working on', file, '----------')
    fits_file = os.path.join(input_path, file)
    hdu = fits.open(fits_file)
    hdu.verify('fix')
    data = hdu[0].data
    test_data, data_height, data_width = read_data(data)
    start = time.time()
    predict_results = inverse(test_data, model)
    end = time.time()
    print('Inversion Time:', np.round(end - start, 1), 's')
    save_results(predict_results, output_path, file[: file.find('.')], data_height, data_width, save_mag_field_o=False)
