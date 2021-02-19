from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2
import os
import scipy.io as io
import shutil
import torch


def MaxMinNormalization(x, Max, Min):

    x = (x - Min) / (Max - Min)
    return x


def cal_chi_distance(img_path, gt_path):

    # print(img_path)
    image = cv2.imread(img_path)
    print(img_path)
    mask = cv2.imread(gt_path)
    mask = cv2.resize(mask, (image.shape[1], image.shape[0]))

    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # print('img.shape', image.shape)
    # print('mask.shape', mask.shape)

    reverse_mask = 255 - mask

    fore_hist = cv2.calcHist([image], [0, 1, 2], mask, [8, 8, 8], [0, 255, 0, 255, 0, 255])

    back_hist = cv2.calcHist([image], [0, 1, 2], reverse_mask, [8, 8, 8], [0, 255, 0, 255, 0, 255])

    mask[mask > 0] = 1
    mask_area = mask.sum()

    reverse_mask[reverse_mask > 0] = 1
    reverse_mask_area = reverse_mask.sum()

    fore_hist = (fore_hist/mask_area).flatten()
    back_hist = (back_hist/reverse_mask_area).flatten()

    fore_hist = fore_hist.astype(np.float32)
    back_hist = back_hist.astype(np.float32)


    d = cv2.compareHist(fore_hist, back_hist, method=cv2.HISTCMP_CHISQR)

    return d


def cal_chi_distance_for_depth(depth_path, gt_path):
    depth = cv2.imread(depth_path)
    mask = cv2.imread(gt_path)
    mask = cv2.resize(mask, (depth.shape[1], depth.shape[0]))

    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    reverse_mask = 255 - mask

    fore_hist = cv2.calcHist([depth], [0], mask, [255], [0, 255])
    back_hist = cv2.calcHist([depth], [0], reverse_mask, [255], [0, 255])


    mask[mask > 0] = 1
    mask_area = mask.sum()

    reverse_mask[reverse_mask > 0] = 1
    reverse_mask_area = reverse_mask.sum()

    fore_hist = (fore_hist / mask_area).flatten()
    back_hist = (back_hist / reverse_mask_area).flatten()

    fore_hist = fore_hist.astype(np.float32)
    back_hist = back_hist.astype(np.float32)

    d = cv2.compareHist(fore_hist, back_hist, method=cv2.HISTCMP_CHISQR)

    return d


def load_list(file):

    with open(file) as f:
        lines = f.read().splitlines()

    files = []
    depths = []
    labels = []

    for line in lines:
        files.append(line.split(' ')[0])
        depths.append(line.split(' ')[1])
        labels.append(line.split(' ')[2])

    return files, depths, labels



if __name__ == "__main__":

    lst = '../list/'
    # compute = 'rgbImg_global_contrast'
    compute = 'depthMap_global_contrast'

    save_path = compute + '/ori_txt/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)


    datasets_lists = os.listdir(lst)


    for dataset_list in datasets_lists:
        print('starting analyze {}'.format(dataset_list))
        dataset_name = dataset_list.split('_list.txt')[0]
        imgs, depths, gts = load_list(lst + dataset_list)

        if compute == 'rgbImg_global_contrast':
            imgs = imgs
        else:
            imgs = depths

        ratio = np.zeros(len(imgs))
        for i in range(len(imgs)):
            if compute == 'rgbImg_global_contrast':

                d = cal_chi_distance(imgs[i], gts[i])

            else:
                d = cal_chi_distance_for_depth(depths[i], gts[i])

            ratio[i] = d
