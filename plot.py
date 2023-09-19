
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib as mpl
mpl.use('Agg') #silent mode
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

#------------------ FONT_setup ----------------------
font = {'family' : 'DejaVu Sans', 
    'color'  : 'black',
    'weight' : 'normal',
    'size' : 20.0,
    }

#------------------- Data Read ----------------------
group_labels=[];xtick=[]
with open('KLABELS','r') as reader:
    lines=reader.readlines()[1:]
for i in lines:
    s=i.encode('utf-8')#.decode('latin-1')
    if len(s.split())==2 and not s.decode('utf-8','ignore').startswith('*'):
        group_labels.append(s.decode('utf-8','ignore').split()[0])
        xtick.append(float(s.split()[1]))
for index in range(len(group_labels)):
    if group_labels[index]=='GAMMA':
        group_labels[index]=u'Γ'

datan=np.loadtxt('REFORMATTED_BAND.dat',dtype=np.float64)
datas=np.loadtxt('REFORMATTED_BAND_SOC.dat',dtype=np.float64)
#--------------------- PLOTs ------------------------
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
axe = plt.subplot(111)
axe.axhline(y=0, xmin=0, xmax=1,linestyle= '--',linewidth=1.0,color='0.5')
for i in xtick[1:-1]:
    axe.axvline(x=i, ymin=0, ymax=1,linestyle= '--',linewidth=1.0,color='0.5')
colormaps='blue'
axe.plot(datan[:,0],datan[:,1:],linewidth=0.4,color=colormaps)
axe.plot(datas[:,0],datas[:,1:],linewidth=0.4,color='red',linestyle='--')
linen, = plt.plot('-', color=colormaps)
lines, = plt.plot('-', color='red',linestyle='--')
axe.set_ylabel(r'$E-E_{\rm F}$ (eV)',fontdict=font)
axe.set_xticks(xtick)
plt.yticks(fontsize=font['size'],fontname=font['family'])
axe.set_xticklabels(group_labels, rotation=0,fontsize=font['size'],fontname=font['family'])
axe.set_xlim((xtick[0], xtick[-1]))
axe.legend(handles=[linen,lines],
           labels=['without SOC','with SOC'],
           loc='upper right',fontsize=9,frameon=False)
plt.ylim(( -3, 3)) # set y limits manually
fig = plt.gcf()
fig.set_size_inches( 8, 6)
# ax = plt.gca()
# ax.set_facecolor((0.9, 0.9, 0.9))
#plt.savefig('band.png',dpi= 300)
plt.savefig('./plot/band_sn.png', format="png", dpi=300, bbox_inches='tight') 
