import numpy as np
import csv
import matplotlib.pyplot as plt

#define the file directory
features_directory = './training_data'
save_Vidi_img_directory = './training_data_vidi'
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
            img_path_vidi = save_Vidi_img_directory+'IMG'+(img_path.split('IMG')[1]).strip()+'('+logs[i][7]+')'
            #img = plt.imread(img_path)
            #img_vidi = plt.imsave(img_path_vidi)
    return

Img_Prepare()