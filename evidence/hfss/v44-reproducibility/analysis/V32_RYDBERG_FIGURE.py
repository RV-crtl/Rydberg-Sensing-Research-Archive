from pathlib import Path
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Rectangle
R=Path(__file__).resolve().parents[1]/'figures'
navy='#183247';red='#bd4f40';blue='#267bc0';gold='#bd8937';teal='#007d82'
fig=plt.figure(figsize=(4.9,3.0));ax=fig.add_axes([.03,.07,.94,.87]);ax.set(xlim=(0,10),ylim=(-.15,6.5));ax.axis('off')
# horizontal levels
for y,left,right,label in [(0.50,.45,3.80,r'$|1\rangle$  5S$_{1/2}$'),(2.00,.45,3.80,r'$|2\rangle$  5P$_{3/2}$'),(4.30,.45,3.80,r'$|3\rangle$  Rydberg $|r\rangle$'),(5.85,.45,3.80,r'$|4\rangle$  $|r\prime\rangle$')]:
 ax.plot([left,right],[y,y],color=navy,lw=1.75);ax.text(3.87,y,label,va='center',fontsize=8.9,color=navy)
def arrow(y1,y2,x,col,label):
 ax.add_patch(FancyArrowPatch((x,y1+.1),(x,y2-.1),arrowstyle='-|>',mutation_scale=13,color=col,lw=2.2));ax.text(x+.14,(y1+y2)/2,label,fontsize=8.6,color=col,va='center',weight='bold')
arrow(.5,2,1.0,red,'780 nm')
arrow(2,4.3,2.35,blue,'480 nm')
arrow(4.3,5.85,3.3,gold,r'$\Omega_{\rm RF}$')
ax.plot([6.4,6.4],[-.03,6.4],color='#cddadd',lw=1)
for y,t1,t2 in [(5.4,'Local microwave coupling',r'$\Omega_{\rm RF}=|\mathbf{d}\cdot\mathbf{E}|/\hbar$'),(3.2,'Atomic susceptibility',r'$\chi(\Delta_p;|\Omega_{\rm RF}|^2)$'),(1.0,'Optical readout',r'$T(\Delta_p)=e^{-k_p\int\!\operatorname{Im}\chi\,dz}$')]:
 ax.add_patch(Rectangle((6.75,y-.72),3.10,1.40,facecolor='#f1f6f7',edgecolor='#c4d6d8',lw=.8));ax.text(6.91,y+.36,t1,fontsize=8.9,weight='bold',color=navy);ax.text(6.9,y-.18,t2,fontsize=8.15,color=teal)
ax.text(.42,6.3,'Rubidium four-level ladder',fontsize=9,weight='bold',color=navy)
for e in ['pdf','svg','png']:
 fig.savefig(R/('F02_RYDBERG_LEVELS.'+e),bbox_inches='tight',pad_inches=.10,dpi=240 if e=='png' else 150)
plt.close(fig)
