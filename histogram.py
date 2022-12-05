import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("info.csv", encoding='gbk')
length = len(df)
region = {}
unit_price = []
total_price = []
for i in range(length):
    if i != 38:
        if str(df['region'][i]) not in region.keys():
            region[str(df['region'][i])] = [1]
            region[str(df['region'][i])].append(int(df['unit_price'][i]))
            region[str(df['region'][i])].append(int(df['total_price'][i]))            
        else:
            region[str(df['region'][i])][0] += 1
            region[str(df['region'][i])][1] += int(df['unit_price'][i])
            region[str(df['region'][i])][1] += int(df['total_price'][i])

for key in region.keys():
    region[key][1] = int(region[key][1] / region[key][0])
    region[key][2] = int(region[key][2] / region[key][0])

num = [region[key][0] for key in region.keys()]
color = ['red', 'green', 'blue', 'yellow', 'black', 'pink', 'purple', 'gold', 'gray', 'orange']
label = [key for key in region.keys()]
unit_price = [region[key][1] for key in region.keys()]
total_price = [region[key][2] for key in region.keys()]

fig1 = plt.figure(10)
for i in range(1, 11):
    rect =plt.bar(x = i,height = unit_price[i-1],color=(color[i-1]),label=(label[i-1]),width = 0.7)
    plt.text(i, unit_price[i-1], unit_price[i-1], ha='center', va='bottom',)
plt.legend()
plt.xticks(range(1, 11), num)
plt.title('平均单价直方图(/元)')
plt.show()

fig1 = plt.figure(10)
for i in range(1, 11):
    rect =plt.bar(x = i,height = total_price[i-1],color=(color[i-1]),label=(label[i-1]),width = 0.7)
    plt.text(i, total_price[i-1], total_price[i-1], ha='center', va='bottom',)
plt.legend()
plt.xticks(range(1, 11), num)
plt.title('平均总价直方图(/万元)')
plt.show()