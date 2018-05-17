import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

#多合一显示
plt.figure()

#前两个值为大图的分割方法
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])

plt.subplot(2,3,4)
plt.plot([0,1],[0,1])

plt.subplot(2,3,5)
plt.plot([1,0],[1,0])

plt.subplot(2,3,6)
plt.plot([0,1],[1,1])

#多合一显示
plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),rowspan=1,colspan=3)
ax1.plot([0,1],[0,1])
ax1.set_label('xxxxx')

ax1 = plt.subplot2grid((3,3),(1,0),rowspan=1,colspan=1)

ax2 = plt.subplot2grid((3,3),(1,1),rowspan=1,colspan=1)

ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2,colspan=1)

ax4 = plt.subplot2grid((3,3),(2,0),rowspan=1,colspan=2)

#多合一显示
plt.figure()
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:2])
ax3 = plt.subplot(gs[1:,2])
ax4 = plt.subplot(gs[-1,0])
ax5 = plt.subplot(gs[-1,-2])

#一个figure中多个图
fig = plt.figure()
x = np.random.uniform(0,1,10)
y = np.random.uniform(0,1,10)

left,bottom,width,height = 0.1,0.1,0.8,0.8
ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(x,y)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('main')

ax2 = fig.add_axes([0.2,0.6,0.2,0.2])
ax2.plot(y,x)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('1_small')

plt.axes([0.6,0.2,0.2,0.2])
plt.plot(y,x)
plt.xlabel('x')
plt.ylabel('y')
plt.title('2_small')


#次坐标轴
plt.figure()

fig,ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot([0,1],[0,1],'r--')
ax2.plot([0,1],[1,0],'b-')

plt.show()



