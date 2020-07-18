import numpy as np
import matplotlib.pyplot as plt

us_file_path = "../Numpy/youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "../Numpy/youtube_video_data/GB_video_data_numbers.csv"

t_uk = np.loadtxt(uk_file_path,delimiter=",",dtype=int)
t_uk=t_uk[t_uk[:,1]<=500000]
t_uk_comment = t_uk[:,-1]
t_uk_like= t_uk[:,1]



plt.figure(figsize=(20,0))
fig,ax=plt.subplots()
ax.scatter(t_uk_like,t_uk_comment)
plt.show()