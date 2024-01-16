import os
num=0
for i in os.listdir(r'C:\Users\16609\Desktop\leave'):
    os.rename(r'C:\Users\16609\Desktop\leave'+'\\'+str(i),r'C:\Users\16609\Desktop\leave'+'\\'+'c'+str(num)+'.jpg')
    num+=1

# from PIL import Image
# import random
#
# # 打开原始图像和要粘贴的图像
# background_image = Image.open(r'C:\Users\16609\Desktop\input\P1100503.JPG')
# overlay_image = Image.open(r'C:\Users\16609\Desktop\output\P1100500\1.png')
#
# # 获取原始图像和要粘贴图像的宽度和高度
# bg_width, bg_height = background_image.size
# overlay_width, overlay_height = overlay_image.size
#
# # 随机确定粘贴位置的左上角坐标
# x = random.randint(0, bg_width - overlay_width)
# y = random.randint(0, bg_height - overlay_height)
# for i in range(overlay_width):
#     for j in range(overlay_height):
#         pixel_value = overlay_image.getpixel((i, j))
#         if pixel_value == (0, 0, 0):
#             pass
#         else:
#             background_image.putpixel((x+i,y+j),pixel_value)
#
# # 创建新的图像对象作为粘贴结果
# result_image = background_image.copy()
#
# # 在指定位置粘贴图像
#
#
# # 显示或保存粘贴后的图像
# result_image.show()
# # result_image.save('result_image.jpg')
import os
import random
from PIL import Image

# 指定图像文件夹路径
# folder_path = r'C:\Users\16609\Desktop\output\P1100500'
# # 获取文件夹内所有图片文件的路径
# image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.jpg') or file.endswith('.png')]
#
# # 从图片文件列表中随机选择10张图片
# selected_images = random.sample(image_files, 50)
# # 读取选中的图片并保存在列表中
# image_list = []
# for image_file in selected_images:
#     image = Image.open(image_file)
#     image_list.append(image)
# background_image = Image.open(r'C:\Users\16609\Desktop\input\P1100503.JPG')
# bg_width, bg_height = background_image.size
# for overlay_image in image_list:
#     overlay_width, overlay_height = overlay_image.size
#     # 随机确定粘贴位置的左上角坐标
#     x = random.randint(0, bg_width - overlay_width)
#     y = random.randint(0, bg_height - overlay_height)
#     for i in range(overlay_width):
#         for j in range(overlay_height):
#             pixel_value = overlay_image.getpixel((i, j))
#             if pixel_value == (0, 0, 0):
#                 pass
#             else:
#                 background_image.putpixel((x+i,y+j),pixel_value)
#     # 创建新的图像对象作为粘贴结果
# result_image = background_image.copy()


