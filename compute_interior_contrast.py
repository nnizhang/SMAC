# calculate the entropy of masked image

from skimage import data
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage import io
from skimage.measure.entropy import shannon_entropy
import numpy as np
from skimage.color import rgb2gray
import os
from skimage.transform import rescale, resize
import scipy.io
import cv2
import math


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



def entro(*c):
    esp = 0.000001
    result = -1
    if(len(c)>0):
        result = 0

    for i in range(len(c[0])):
       
        result += (-c[0][i])*math.log(c[0][i]+esp, 2)

  
    return result


def cal_entropy(img_path, gt_path):
    
    image = cv2.imread(img_path)
    print(img_path)
    mask = cv2.imread(gt_path)
    mask = cv2.resize(mask, (image.shape[1], image.shape[0]))

    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # print('img.shape', image.shape)
    # print('mask.shape', mask.shape)

    fore_hist = cv2.calcHist([image], [0, 1, 2], mask, [8, 8, 8], [0, 255, 0, 255, 0, 255])

    mask[mask > 0] = 1
    mask_area = mask.sum()

    fore_hist = (fore_hist / mask_area).flatten()
    fore_hist = fore_hist.astype(np.float32)

    ent = entro(fore_hist)

    return ent


def cal_entropy_for_depth(depth_path, gt_path):
    depth_path  ='/data/zhangni/Data/RGB-D_Saliency/RGBdDataset_processed/ReDWeb_S/trainset/depth/7441943888_d0371f42f0.png'
    gt_path  ='/data/zhangni/Data/RGB-D_Saliency/RGBdDataset_processed/ReDWeb_S/trainset/GT/7441943888_d0371f42f0.png'
    depth = cv2.imread(depth_path)

    mask = cv2.imread(gt_path)
    mask = cv2.resize(mask, (depth.shape[1], depth.shape[0]))
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    
    fore_hist = cv2.calcHist([depth], [0], mask, [8], [0, 255])

    mask[mask > 0] = 1
    mask_area = mask.sum()


    fore_hist = (fore_hist / mask_area).flatten()

    fore_hist = fore_hist.astype(np.float32)

    ent = entro(fore_hist)
    if ent < 0:
        print(depth_path)
    
    return ent


if __name__ == "__main__":

    lst = '../list/'
    # compute = 'rgbImg_object_interior'
    compute = 'depthMap_object_interior'

    save_path = compute + '/ori_txt/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    save_path2 = compute + '/txt/'
    if not os.path.exists(save_path2):
        os.makedirs(save_path2)

    save_path_mat = compute + '/mat/'
    if not os.path.exists(save_path_mat):
        os.makedirs(save_path_mat)

    datasets_lists = os.listdir(lst)


    for dataset_list in datasets_lists:
        print('starting analyze {}'.format(dataset_list))

        imgs, depths, gts = load_list(lst + dataset_list)
        ratio = np.zeros(len(imgs))
        for i in range(len(imgs)):
            # print('{}/{}'.format(i, len(imgs)))
            # print(imgs[i])

            if compute == 'rgbImg_object_interior':

                d = cal_entropy(imgs[i], gts[i])

            else:
                d = cal_entropy_for_depth(depths[i], gts[i])

            ratio[i] = d
        
