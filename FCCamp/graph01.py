import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Basic Graph
x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8, 10]

# Resize your Graph (dpi specifies pixels per inch.  When saving probably use )
plt.figure(figsize=(5,3), dpi=300)

# Line 1

# Keyword Argument Notation
# plt.plot(x, y, label='2x', color='red', linestyle='--', linewidth=2, marker='.', markersize=10, markeredgecolor='blue')

# Use shorthand notation
# fmt = '[color][marker][line]'
plt.plot(x, y, 'b^--', label='2x')

# Line Number 2

# select interval we want to plot points at
x2 = np.arange(0,4.5,0.5)

# Plot part of the graph as line
plt.plot(x2[:6], x2[:6]**2, 'r', label='x^2')

# Plot remainder of graph as a dot
plt.plot(x2[5:], x2[5:]**2, 'r--')

# Add a title (specify font parameter with fontdict)
plt.title('Our first Graph!', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})
 
# X and Y lables
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# X, Y axis Tickmarks (scale of your graph)
plt.xticks([0, 1, 2, 3, 4])
plt.yticks([0, 2, 4, 6, 8, 10])

# Add a Legend
plt.legend(loc='upper left')

# Save figure (dpi 300 is good when saving so graph has high resolution)
plt.savefig('mygraph.png', dpi=300)

# Show plot
plt.show()