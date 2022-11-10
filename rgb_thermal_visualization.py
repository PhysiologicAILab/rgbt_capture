import numpy as np
import cv2
import os
# import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


# import time
# from datetime import datetime

# root_path = r'D:\Temp\data'
root_path = r'D:\TCC_04Nov\TCC\P3_D1\2022-11-04_14-20-28'

save_path = os.path.join(root_path, 'plots')
if not os.path.exists(save_path):
    os.makedirs(save_path)

list_files = os.listdir(root_path)
ext_list = ['.npy', '.jpg', '.png']

therm_images = []
rgb_images = []
therm_time_stamp_list = []
rgb_time_stamp_list = []

for i in range(len(list_files)):
    fn = list_files[i]
    if os.path.isfile(os.path.join(root_path, fn)):
        fname, fn_ext = os.path.splitext(fn)
        if fn_ext in ext_list:
            ts = fname.split('_')[1:]
            ts = float(ts[0] + '.' + ts[1])
            # ts = datetime.fromtimestamp(ts)
            # print(ts)

            if fn_ext == '.npy':
                therm_images.append(fn)
                therm_time_stamp_list.append(ts)
            else:
                rgb_images.append(fn)
                rgb_time_stamp_list.append(ts)

therm_time_stamp_list = np.asarray(therm_time_stamp_list)
rgb_time_stamp_list = np.asarray(rgb_time_stamp_list)

for i in range(len(therm_images)):

    th_ts = therm_time_stamp_list[i]
    diff_ts = np.abs(th_ts + 0.4 - rgb_time_stamp_list)
    rgb_indx = int(np.argmin(diff_ts))
    print(i, '--', rgb_indx, ':', min(diff_ts))
    
    fn, _ = os.path.splitext(therm_images[i])
    th_img = np.load(os.path.join(root_path, therm_images[i]))
    rgb_img = cv2.imread(os.path.join(root_path, rgb_images[rgb_indx]))
    rgb_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
    save_fn = fn.split('_')[1:]
    save_fn = '_'.join(save_fn)
    # fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    # ax[0].imshow(th_img, cmap='magma')
    # ax[0].axis('off')
    # ax[1].imshow(rgb_img)
    # ax[1].axis('off')
    # plt.tight_layout()
    # plt.savefig(os.path.join(save_path, fn + '.jpg'))
    # plt.close()

    fig = Figure()
    ax = fig.subplots(1, 2)
    fig.tight_layout()
    fig.set_figwidth(10)
    fig.set_figheight(4)
    canvas = FigureCanvas(fig)
    ax[0].imshow(th_img, cmap='magma')
    ax[0].set_axis_off()
    ax[1].imshow(rgb_img)
    ax[1].set_axis_off()
    canvas.draw()
    canvas.print_jpg(os.path.join(save_path, save_fn + '.jpg'))
    fig.clf()

    # if i > 100:
    #     break
