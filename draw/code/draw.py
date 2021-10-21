import pandas as pd

file = '../data/revenue12.xls'

p = pd.read_excel(file)
p = p[['y', 'y_pred']].copy()
p.index = range(1994, 2016)
import matplotlib.pyplot as plt

# 使用pandas的画图函数作图
p.plot(style=['b-o', 'r-*'], xticks=p.index, figsize=(15, 5))
plt.xlabel("Year")
plt.savefig('c:/wuda/sinc.pdf')
# plt.show()
print("File is generated.")
