import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

import PIL.Image
import cv2
import numpy as np
import pandas
import torch
from tqdm import tqdm

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from models.common import DetectMultiBackend
from utils.callbacks import Callbacks
from utils.dataloaders import create_dataloader
from utils.general import (LOGGER, TQDM_BAR_FORMAT, Profile, check_dataset, check_img_size, check_requirements,
                           check_yaml, coco80_to_coco91_class, colorstr, increment_path, non_max_suppression,
                           print_args, scale_boxes, xywh2xyxy, xyxy2xywh)
from utils.metrics import ConfusionMatrix, ap_per_class, box_iou
from utils.plots import output_to_target, plot_images, plot_val_study
from utils.torch_utils import select_device, smart_inference_mode

weights =r'C:\Users\16609\Desktop\有ca\weights\best.pt'
device=torch.device('cuda')
data=r'C:/Users/16609/Desktop/greenorange.v15i.yolov5pytorch/data.yaml'

im=cv2.imread(r'C:\Users\16609\Desktop\greenorange.v15i.yolov5pytorch\valid\images\P1100016_JPG.rf.911ee9bdb2ac1a30de5deac9c8c2d3e7.jpg')
targets=pandas.read_csv(r'C:\Users\16609\Desktop\greenorange.v15i.yolov5pytorch\valid\labels\P1100016_JPG.rf.911ee9bdb2ac1a30de5deac9c8c2d3e7.txt',header=None).values

model = DetectMultiBackend(weights, device=device, dnn=True, data=data, fp16=False)
model.eval()
im=PIL.Image.fromarray(im)
#im = im.to(device, non_blocking=True)
nb, _, height, width = im.shape
targets = targets.to(device)
preds, train_out = model(im)
targets[:, 2:] *= torch.tensor((width, height, width, height), device=device)# to pixels
lb = [targets[targets[:, 0] == i, 1:] for i in range(nb)] if False else []  # for autolabelling
preds = non_max_suppression(preds,0.0001,0.6,labels=lb,multi_label=True,agnostic=True,max_det=150)

plot_images(im, targets, im, './f a0.jpg', {0: 'orange'})  # labels
plot_images(im, output_to_target(preds), im, './ f a.jpg', {0: 'orange'})  # pred