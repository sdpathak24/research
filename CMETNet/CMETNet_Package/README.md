## Predicting CME arrival time through data integration and ensemble learning<br>
This README explains the requirements and getting started to run the CME transit time prediction using the Deep Learning network CMETNet.

## Authors
Khalid A. Alobaid, Yasser Abduallah, Jason T. L. Wang, and Haimin Wang

## Abstract

The Sun constantly releases radiation and plasma into the heliosphere. 
Sporadically, the Sun launches solar eruptions such as flares and coronal mass ejections (CMEs). 
CMEs carry away a huge amount of mass and magnetic flux with them. An Earth-directed CME can cause serious consequences to the human system. 
It can destroy power grids/pipelines, satellites, and communications. 
Therefore, accurately monitoring and predicting CMEs is important to minimize damages to the human system. 
In this study we propose an ensemble learning approach, named CMETNet, 
for predicting the arrival time of CMEs from the Sun to the Earth. 
We collect and integrate eruptive events from two solar cycles, #23 and #24, from 1996 to 2021 with a total of 363 geoeffective CMEs. 
The data used for making predictions include CME features, 
solar wind parameters and CME images obtained from the SOHO/LASCO C2 coronagraph. 
Our ensemble learning framework comprises regression algorithms for numerical data analysis and a convolutional neural network for image processing. 
Experimental results show that CMETNet performs better than existing machine learning methods reported in the literature, 
with a Pearson product-moment correlation coefficient of 0.83 and a mean absolute error of 9.75 h.

For the latest updates of the tool refer to https://github.com/deepsuncode/CMETNet

## Prerequisites
The specified version of Python and its packages are required to run on a local CPU.
| Library | Version | Description  |
|---|---|---|
| python| 3.9.13 | Programming language|
| astropy | 5.1| Astronomy in Python for image processing and more|
|numpy| 1.21.6| Array manipulation|
|scikit-learn| 1.2.1| Machine learning|
|scikit-image| 0.19.2 | Image processing|
| pandas|1.4.4| Data loading and manipulation|
| tensorflow| 2.11.0| Deep learning tool|
| xgboost| 1.5.0 | Optimized distributed gradient boosting library |
| matplotlib|3.5.2| Visualization tool|



Other versions are not tested, but they should work if you have the environment set properly to run deep learning jobs.


## Installation on local machine
To install the required packages, you may use Python package manager "pip" as follow:
1.	Copy the above packages into a text file,  ie "requirements.txt"
2.	Execute the command: 

Type:

	pip install -r requirements.txt

Note: There is a requirements file already created for you to use that includes all packages with their versions. The files are located in the root directory of the CMETNet.
Note: Python packages and libraries are sensitive to versions. Please make sure you are using the correct packages and libraries versions as specified above.


## Package Structure
After downloading the zip files from github repository: https://github.com/deepsuncode/CMETNet the CMETNet package includes the following folders and files:

| File | Description  |
|---|---|
| README.md | this  file | 
|  requirements.txt  | includes Python required packages for Python version 3.9.13| 
|  data   | includes data that can be used for training and prediction| 
|  results | will include the prediction result file(s)| 
|  CMETNet_CNN_train.py | Python program to train/predict the CMETNet CNN model| 
|  CMETNet_COMB_train.py  | Python program to train/predict CMETNet COMB models| 
|  results_ensemble.py | Python program to ensemble the 5 models and produce CMETNet results| 
 
 
 
## Running a Train/Prediction Task:
To run a train task, you should type: 

	python CMETNet_CNN_train.py
	
and

	python CMETNet_COMB_train.py
	
Without any option will this will train all the models using data samples, and save the prediction results in the results folder.

## Running a Testing Task:
To show the results of CMETNet, you should type:

	python results_ensemble.py
	
This will ensemble the results made by the models and show the PCCMM/MAE, save the CMETNet results in the results folder.

