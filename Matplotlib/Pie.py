import matplotlib.pyplot as plt

data = [ i for i in range(5)]
label = [ c for c in "abcde"]

print(data)
print(label)

fig,ax = plt.subplots()
ax.pie(data,labels=label)
plt.show()