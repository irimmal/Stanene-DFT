
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

datasn = np.loadtxt('PBAND_Sn_SOC.dat',dtype=np.float64)
datao = np.loadtxt('PBAND_Sn_SOC.dat',dtype=np.float64)

data2=np.loadtxt('REFORMATTED_BAND.dat',dtype=np.float64)
#--------------------- PLOTs ------------------------
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
axe = plt.subplot(111)
axe.axhline(y=0, xmin=0, xmax=1,linestyle= '--',linewidth=1.0,color='0.5')
for i in xtick[1:-1]:
    axe.axvline(x=i, ymin=0, ymax=1,linestyle= '--',linewidth=1.0,color='0.5')
colormaps='blue'
axe.plot(data2[:,0],data2[:,1:],linewidth=0.4,color=colormaps)
gap = 15
size = 120
label_list = ["s","py",     "pz",     "px",    "dxy",    "dyz",    "dz2",    "dxz",  "x2-y2"]
color_list = ["#000000","#ff0000","#00ff00","#0000ff","#ff00ff","#00ffff","#ffff00","#ff8000","#8000ff"]
marker_list = ['s','o','v','^','<','>','*','p','h']
for i in range(9):
    xs = datasn[i*2::gap,0]
    ys = datasn[i*2::gap,1]
    xn = datao[i*2::gap,0]
    yn = datao[i*2::gap,1]
    Sn = datasn[i*2::gap,i+2] * size
    other = datao[i*2::gap,i+2] * size
    axe.scatter(x=xs, y=ys, s = Sn, marker=marker_list[i], edgecolors=color_list[i], linewidth=0.9,
                facecolors='none', label="Sn "+label_list[i], alpha=0.6)
    #axe.scatter(x=xn, y=yn, s = other, alpha=0.7, marker=marker_list[i], edgecolors=color_list[i], linewidth=0.9,
     #           facecolors='none', label="F "+label_list[i])
axe.set_ylabel(r'$E-E_{\rm F}$ (eV)',fontdict=font)
axe.set_xticks(xtick)
plt.yticks(fontsize=font['size'],fontname=font['family'])
axe.set_xticklabels(group_labels, rotation=0,fontsize=font['size'],fontname=font['family'])
axe.set_xlim((xtick[0], xtick[-1]))
axe.legend(loc='upper right',fontsize=9,frameon=False)
plt.ylim(( -0.04, 0.04)) # set y limits manually
fig = plt.gcf()
fig.set_size_inches( 8, 6)
# ax = plt.gca()
# ax.set_facecolor((0.9, 0.9, 0.9))
#plt.savefig('band.png',dpi= 300)
plt.savefig('strain0/_0.1.png', format="png", dpi=300, bbox_inches='tight') 
