import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.lines import Line2D

#plt.figure()
fig, ax = plt.subplots(1,1, figsize = (8,8))
ax.plot([1/3, 1/3], [0, 1], 'k')  
ax.plot([2/3, 2/3], [0, 1], 'k')  
ax.plot([0, 1], [1/3, 1/3], 'k')  
ax.plot([0, 1], [2/3, 2/3], 'k')  
ax.axis("equal")
symbols = []

def drawacircle(position):
    Osym = Circle(position, 0.1, color='b', fill=False, linewidth=2)
    ax.add_artist(Osym) #stack overflow dis que ca marche
    symbols.append(Osym)

def draxanx(position):
    x, y = position
    Cross1 = Line2D([x - 0.1, x + 0.1], [y - 0.1, y + 0.1], color='r', linewidth=3)
    Cross2 = Line2D([x - 0.1, x + 0.1], [y + 0.1, y - 0.1], color='r', linewidth=3)
    ax.add_artist(Cross1)
    ax.add_artist(Cross2)
    symbols.append(Cross1)
    symbols.append(Cross2)
drawacircle((0.85, 0.85))
draxanx((0.5, 0.5))
ax.set_xlim((0, 1))
ax.set_ylim((0, 1))
ax.set_xticks([])
ax.set_yticks([])
print("troll")
plt.show()
