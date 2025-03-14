import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('C:\Users\dialk\KNES381\KNES381_vo2data\subject_1232.csv')
df.info
df.head(10)
#df = df.rename(columns={'':''})
'''
x = df['TIME']
y1 = df['VO2']
y2 = df['VE']
y1max = max(y1)
xmax = x[y1.argmax()]

plot1 = plt.subplot(2,1,1)
plot1.annotate(f'V\u0307O\u2082={y1max:.2f}L/min', xy=(xmax,y1max), xytext=(xmax +.5, y1max +.5), 
                arrowprops=dict(facecolor='red', shrink=0.05))
plot1.plot(x, y1, label='V\u0307O\u2082', c='b')
plot1.spines(['top', 'right']).set_visible=False
plot1.set(ylabel='L/min')
plot1.legend()

plot2 = plt.subplot(2,1,2)
plot2.plot(x, y2, label='VE', c='r')
plot2.spines(['top', 'right']).set_visible(False)
plot2.set(ylabel='breaths/min')
plot2.legend()

plt.show
'''

