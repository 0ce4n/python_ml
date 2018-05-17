import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2 * x + 1
y2 = x ** 2

#某图的开始
plt.figure()

#设置x与y轴的范围
plt.xlim((-1,2))
plt.ylim((-1,4))

#设置x与y轴的标注
plt.xlabel("i am x")
plt.ylabel("i am y")

#设置x轴与y轴的标记
plt.xticks([1,2,3,4,5],['aa','bb','cc','dd','ee'])
y_ticks = np.linspace(-1,2,6)
plt.yticks(y_ticks)

#获取坐标轴对象   gca为get current axis
ax = plt.gca()

#设置图的四个轴
#设置为不显示
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#分别设置x轴和y轴所选择的脊梁
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#设置轴的位置
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

#获得两个线对象
l1, = plt.plot(x,y2,label = 'one')
l2, = plt.plot(x,y1,color = 'red',label = 'two')

#打印图例
plt.legend(handles = [l1,l2],labels = ['aaa','bbb'])

#设置标注
x0 = 0.5
y0 = y2 = x0 ** 2
plt.scatter(x0,y0,s = 50,c = 'r')
plt.plot([x0,x0],[0,y0],'k--')

#设置标注方式
plt.annotate('hhhhhh %s' % y0,xy = (x0,y0),\
xycoords = 'data',xytext = (+30,+30),textcoords = 'offset points',arrowprops = dict(arrowstyle = '->',connectionstyle = 'arc3,rad = -.2'))

#文字注释
plt.text(-1,1,'sssssssss',fontdict = {'size':16 , 'color':'r'})

#修改坐标上标注
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor = 'red', edgecolor = 'blue',alpha = 0.3))

#新建一个图
plt.figure()
count = 1024
X = np.random.normal(0,1,count)
Y = np.random.normal(0,1,count)
C = np.arctan2(Y,X)
plt.scatter(X,Y,c = C,alpha = 0.5)
plt.xlim = ((-1.5,1.5))
plt.ylim = ((-1.5,1.5))
plt.xticks(())
plt.yticks(())

#新建一个图，画柱状图
plt.figure()
XX = np.arange(12)
YY1 = (1 - XX / 12.0)*np.random.uniform(0.5,1.0,12)
YY2 = (1 - XX / 12.0)*np.random.uniform(0.5,1.0,12)

#画柱状图
plt.bar(XX,YY1,facecolor = 'green', edgecolor = 'black')
plt.bar(XX,-YY2,facecolor = 'yellow', edgecolor = 'black')

for x,y in zip(XX,YY1):
    plt.text(x+0.03, y+0.05,'%.2f'%y, ha = 'center', va = 'bottom')
for x,y in zip(XX,-YY2):
    plt.text(x+0.03, y-0.05,'%.2f'%y, ha = 'center', va = 'top')

plt.xticks(())
plt.yticks(())
axis = plt.gca()
axis.spines['top'].set_color('none')
axis.spines['bottom'].set_color('none')
axis.spines['left'].set_color('none')
axis.spines['right'].set_color('none')

#新建图片，画等高线
plt.figure()
def z(x,y):
    return x**2-y**3

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)

#将X,Y变为点阵
X,Y = np.meshgrid(x,y)

#填充颜色
plt.contourf(X,Y,z(X,Y),8,alpha = .5,cmap=plt.cm.hot)

#画等高线
C = plt.contour(X,Y,z(X,Y),8,color = 'black',linewidth = .5)

#等高线标注
plt.clabel(C,inline = True, fontsize = 10)

#新建图片

#图的绘制
plt.show()