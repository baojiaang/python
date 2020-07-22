import matplotlib.pyplot as plt

x_label = ['2015','2016','2017','2018']
num_list1=[20,30,15,35] # 纵轴坐标值1
num_list2=[15,30,40,20] #纵轴坐标值2
x = range(len(num_list1))

fig, ax =plt.subplots()

bar1 = ax.bar(x,height=num_list1,color='red',width=0.4)
bar2 = ax.bar([i+0.4 for i in x],height=num_list2,width=0.4,color='yellow')

plt.ylim(0,50)
plt.xticks([i for i in x],x_label)

# 上面的文本

for bar in bar1:
    height=bar.get_height()
    ax.text(bar.get_x()+bar.get_width()/2,height+1,str(height),ha="center",va='bottom')
for bar in bar2:
    height=bar.get_height()
    ax.text(bar.get_x()+bar.get_width()/2,height+1,str(height),ha="center",va='bottom')

plt.show()