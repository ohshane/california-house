import os
import tarfile
from urllib import request
from pathlib import Path

url = "https://drive.google.com/uc?export=download&id=1Fy1B4OElYBh3h7eAHIKKGP1TDBKcWCy3"
dataset_dir = Path(__file__).parent / 'dataset'
data_dir = dataset_dir / 'housing.tgz'

def make_csv():
    request.urlretrieve(url, data_dir)
    file = tarfile.open(data_dir)
    file.extractall(dataset_dir)
    file.close()