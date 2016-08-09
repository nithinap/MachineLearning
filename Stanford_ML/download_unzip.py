import numpy as np
import pandas as pd
import zipfile
from six.moves.urllib.request import urlretrieve 

base_url = "https://s3.amazonaws.com/spark-public/ml/exercises/on-demand/"
filename = "machine-learning-ex3.zip"
"""
train_data, _ = urlretrieve(base_url, filename)
print("Download completed!")
"""
# Now unzip the file
with zipfile.ZipFile(filename,"r") as zf:
    zf.extractall()
    