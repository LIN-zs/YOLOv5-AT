import pywt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
from matplotlib.ticker import MultipleLocator
from scipy.interpolate import make_interp_spline
x=pd.read_csv(r'C:\Users\16609\Desktop\asd.csv').columns.values
noisy_signal=pd.read_csv(r'C:\Users\16609\Desktop\asd.csv').values[0,:]

# 对信号进行小波变换
# coeffs = pywt.wavedec(noisy_signal, wavelet, level=level)
#
# # 通过阈值处理细节系数
# threshold = np.sqrt(2 * np.log(len(noisy_signal)))
# coeffs_thresh = pywt.threshold(coeffs, threshold, mode='soft')63760
#
# # 通过逆小波变换重构信号
# denoised_signal = pywt.waverec(coeffs_thresh, wavelet)
# plt.plot(x, denoised_signal, 'b', label='原始信号')

# 生成噪声
x_major_locator=MultipleLocator(10)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
y_smooth1=noisy_signal[0:7]
y_smooth2 = scipy.signal.savgol_filter(noisy_signal[7:37],11,3)
y_smooth3 = scipy.signal.savgol_filter(noisy_signal[38:60],11,3)
y_smooth4 = scipy.signal.savgol_filter(noisy_signal[61:],11,3)
y_smooth=np.concatenate([y_smooth1,y_smooth2,noisy_signal[37:38,],y_smooth3,noisy_signal[60:61],y_smooth4])
# y_smooth[6]=noisy_signal[6]
# y_smooth[60]=noisy_signal[60]
# y_smooth[37]=noisy_signal[37]
plt.plot(x,noisy_signal,label='yuanshi')
plt.plot(x, y_smooth, 'b', label='quzao',color='r')
plt.xlim()
plt.legend()
plt.show()