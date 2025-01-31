# -*- coding: utf-8 -*-
"""segmentation testing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/120MPE43GRgVUijbm4Dwstzg5lX3X70d5
"""

import torch
from torchvision import transforms
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path


model = torch.hub.load('ultralytics/yolov5:v5.0', 'yolov5s', pretrained=True)


image_path = 'uploads/briyani.jpg'
img = Image.open(image_path)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((640, 640)),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
img_tensor = transform(img).unsqueeze(0)


with torch.no_grad():
    results = model(img_tensor)

masks = results.xyxy[0][:, -1].cpu().numpy()

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(np.array(img))
ax[0].set_title("Original Image")

ax[1].imshow(masks, cmap='tab20b', interpolation='none')
ax[1].set_title("Segmentation Mask")

plt.show()