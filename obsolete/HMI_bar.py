import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
#
# default size
plt.rcParams['figure.figsize'] = (8, 6)

fig, ax = plt.subplots()

threshold = 50

bar = ax.bar([0], [0], width=0.2, color='green')

def draw_marker():
    ax.axhline(y=threshold, color='red', linestyle='--')
    ax.text(0.25, threshold, 'Threshold', fontsize=8, ha='center', va='center')

# Function to update the plot at each animation frame
def update(frame):
    global value

    if frame < 120:
        period = 20  # Period of fluctuation in seconds
        phase = (frame % period) / period * (2 * np.pi)  # Adjust the phase for sinusoidal fluctuation
        value = 87.5 - 2.5 * np.cos(phase)  # Fluctuate between 85 and 100 for the first 60 seconds
    else:
        value = 60 + 1 * (frame - 120)  # Range from 60 to 85 for the next 15 seconds
        if value > 85:
            value = 85

    bar[0].set_height(value)

    if value < 50:
        bar[0].set_color('red')
    else:
        bar[0].set_color('blue')

    ax.clear()
    ax.set_ylim([0, 100])
    ax.set_yticks(range(0, 101, 10))
    ax.set_ylabel('Autonomous Driving Confidence', fontsize=8)
    ax.set_xticks([])
    draw_marker()
    ax.add_patch(bar[0])
    ax.set_xlim([-0.5, 0.5])

# Update the frames to 156 for the extended animation duration (2 seconds per frame for 60 seconds)
anim = animation.FuncAnimation(fig, update, frames=range(0, 156), interval=1000)

# Save the animated figure as a GIF with a specific size (width x height)
Writer = animation.PillowWriter(fps=2, metadata=dict(artist='Me'), bitrate=1800)
anim.save("Inc.gif", writer=Writer, dpi=80)  # Adjust dpi to set the desired size
plt.show()
