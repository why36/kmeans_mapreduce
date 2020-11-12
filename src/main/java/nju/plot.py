import numpy as np
import matplotlib.pyplot as plt
import sys

k=sys.argv[1]

#plt.rcParams['font.sans-serif']=['SimHei']
#plt.rcParams['axes.unicode_minus'] = False

x, y, c = np.loadtxt(r'./output/clusteredInstances/part-m-00000', delimiter=',', unpack=True)

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=100,xmin=0)
plt.ylim(ymax=100,ymin=0)

  

plt.scatter(x, y, c=c, alpha=0.4)
plt.savefig(r'./figure/k={_k},iter=10.png'.format(_k=k))
plt.show()


