"""
Annotation: this file split train and val samples from instance_npz into instance_dataset.
Anthor: Lin, PRML Lab
Data: 20, July, 2022
"""

import os
import shutil
from tqdm import tqdm

train_txt_name_full = '../datasets/kitti/train.txt'
val_txt_name_full = '../datasets/kitti/val.txt'

images_train = '../datasets/kitti/train/images'
images_val = '../datasets/kitti/val/images'

labels_train = '../datasets/kitti/train/labels'
labels_val = '../datasets/kitti/val/labels'

images = '../datasets/kitti/images'
labels = '../datasets/kitti/labels'


def get_id_list(txt_name_full):
    id_list = []
    with open(txt_name_full) as f:
        rds = f.readlines()
        for rd in rds:
            image_id = rd.strip()[:-4]
            # print(image_id)
            id_list.append(image_id)
    return id_list


train_id_list = get_id_list(train_txt_name_full)
val_id_list = get_id_list(val_txt_name_full)

if not os.path.exists(images_train):
    # shutil.rmtree(images_train)
    os.makedirs(images_train)

if not os.path.exists(images_val):
    # shutil.rmtree(images_val)
    os.makedirs(images_val)

if not os.path.exists(labels_train):
    # shutil.rmtree(images_train)
    os.makedirs(labels_train)

if not os.path.exists(labels_val):
    # shutil.rmtree(images_train)
    os.makedirs(labels_val)


for image_id in tqdm(train_id_list):
    im_name_full = os.path.join(images, image_id+'.png')
    shutil.copy(im_name_full, images_train)

    lab_name_full = os.path.join(labels, image_id+'.txt')
    shutil.copy(lab_name_full, labels_train)

for image_id in tqdm(val_id_list):
    im_name_full = os.path.join(images, image_id+'.png')
    shutil.copy(im_name_full, images_val)

    lab_name_full = os.path.join(labels, image_id + '.txt')
    shutil.copy(lab_name_full, labels_val)
