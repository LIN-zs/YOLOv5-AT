from PIL import Image
import numpy as np
import cv2
# 打开图片
image1 = cv2.imread(r'C:\Users\16609\Desktop\SAM\article figure\mix\P1100013_JPG.rf.198cd5002f67012d46a9b12b4b09f93e.jpg')
image2= cv2.imread(r'C:\Users\16609\Desktop\SAM\article figure\mix\P1100027_JPG.rf.418902fd9435d00f85718e9e74726062.jpg')
r = np.random.beta(32.0, 32.0)  # mixup ratio, alpha=beta=32.0
r=0.35
im = (image1 * r + image2 * (1 - r)).astype(np.uint8)
cv2.imwrite(r'C:\Users\16609\Desktop\SAM\article figure\mix\1.jpg',im)
r=0.45
im = (image1 * r + image2 * (1 - r)).astype(np.uint8)
cv2.imwrite(r'C:\Users\16609\Desktop\SAM\article figure\mix\2.jpg',im)

