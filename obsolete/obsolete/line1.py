from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation 
from matplotlib import pyplot as plt
import numpy as np
# I want it to be 10 frames per second, 3000 frames, 300 seconds
x_vals = np.arange(0, 10*np.pi, 0.1)
y_vals = 85 + np.sin(x_vals)

fig = plt.figure()
ax = plt.subplot(1, 1, 1)

data_skip = 5

def init_func():
    ax.clear()
    plt.xlabel('Time (S)')
    plt.ylabel("Confidence Level (%)")
    ax.set_xticks([i for i in range(0, 31, 5)])  # Set ticks at every 5 seconds
    ax.set_xticklabels([str(i) for i in range(0, 31, 5)])  # Label ticks with every 5 seconds
    ax.set_ylim(0, 100)
    ax.set_xlim(x_vals[0], x_vals[-1])
    
def update_plot(i):
    ax.plot(x_vals[i:i+data_skip], y_vals[i:i+data_skip], color='b')

anim = FuncAnimation(fig,
                     update_plot,
                     frames= 3000, # range(0, len(x_vals), data_skip), # duration = frames / interval = 30s
                     init_func=init_func,
                     interval=100) # interval = time between each frame

plt.tight_layout()
# plt.show()

# saving to m4 using ffmpeg writer 
Writer = animation.FFMpegWriter(fps=10)  # 1 frame per second for 85 seconds
anim.save("line1.gif", writer=Writer)
plt.close() 

