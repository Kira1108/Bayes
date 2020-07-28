import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

plt.style.use('ggplot')
weibo_mean = 208
wechat_mean = 190

wechat_std = 36
weibo_std = 60

xiaoming_weibo = 54
xiaohua_wechat = 63

# standard scaler, converted to standard normal distribution
Z_xiaoming = (xiaoming_weibo - weibo_mean) / weibo_std
Z_xiaohua = (xiaohua_wechat - wechat_mean) / wechat_std

print('Xiaoming: {}, Xiaohua: {}'.format(Z_xiaoming, Z_xiaohua))

plt.hist(stats.norm.rvs(loc = weibo_mean, scale = weibo_std, size = 2000),bins = 50)
plt.axvline(xiaoming_weibo, linestyle = '--')

plt.hist(stats.norm.rvs(loc = wechat_mean, scale = wechat_std, size = 2000),bins = 50, color = 'lightseagreen')
plt.axvline(xiaohua_wechat, linestyle = '--', color = 'lightseagreen')
plt.show()
