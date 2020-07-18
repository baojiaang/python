import numpy as np
import matplotlib.pyplot as plt

us_file_path = "../Numpy/youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "../Numpy/youtube_video_data/GB_video_data_numbers.csv"

t_us = np.loadtxt(us_file_path,delimiter=",",dtype=int)

t_us_comments = t_us[:,-1]

print(t_us_comments.max(),t_us_comments.min())
d=500

t_us_comments=t_us_comments[t_us_comments<=5000]
bin_nums =(t_us_comments.max()-t_us_comments.min())//d  # 整除


fig,ax = plt.subplots()
plt.figure(figsize=(20,8))
ax.hist(t_us_comments,bin_nums)
plt.show()
