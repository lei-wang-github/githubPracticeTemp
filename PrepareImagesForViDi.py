import numpy as np
import csv
import matplotlib.pyplot as plt
import os

#define the file directory
features_directory = './training_data/'
save_Vidi_img_directory = './training_data_vidi/'
labels_file = './training_data/driving_log.csv'

def Img_Prepare():
    logs = []
    features = []
    labels = []
    with open(labels_file, 'rt') as f:
        reader = csv.reader(f)
        for line in reader:
            logs.append(line)
        log_labels = logs.pop(0)
        
    for i in range(len(logs)):
        for j in range(3):
            img_path = logs[i][j]
            img_path = features_directory+'IMG'+(img_path.split('IMG')[1]).strip()
            img_path_vidi = save_Vidi_img_directory+'IMG'+(img_path.split('IMG')[1]).strip()
            filename, file_extension = os.path.splitext(img_path_vidi)
            if j == 0: #Center
                img_path_vidi = filename +'-'+logs[i][8]+'-'+'.PNG'
                img = plt.imread(img_path)
                img_vidi = plt.imsave(img_path_vidi, img)
            elif j == 1: #Left
                img_path_vidi = filename +'-'+logs[i][9]+'-'+'.PNG'
                img = plt.imread(img_path)
                img_vidi = plt.imsave(img_path_vidi, img)
            else: #Right
                img_path_vidi = filename +'-'+logs[i][10]+'-'+'.PNG'
                img = plt.imread(img_path)
                img_vidi = plt.imsave(img_path_vidi, img)
                
    return

Img_Prepare()