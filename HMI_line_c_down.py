# Curve down

import matplotlib.pyplot as plt
from matplotlib import animation
import random

fps = 24
total_seconds = 30
total_frames = total_seconds * fps
# Set the figure size
plt.rcParams['figure.figsize'] = (15, 6)

# Initialize the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=6)  # Initialize an empty line

timeoffset = 120 # Starting time of the x-axis
tick_interval = 5  # Interval of 5 seconds
confidence_values = [85]  # Confidence default starts at 85

# Calculate the confidence value
def calculate_confidence(frame, previous_value):
    
    offset = random.uniform(-0.5, 0.5)
    if (15 < (frame / fps) <= 27):
        offset = random.uniform(-1.2, 1.2)
        return -3622.959+665.7375*(frame / fps)-44.08617*(frame / fps)**2+1.277463*(frame / fps)**3-0.01373142*(frame / fps)**4 + offset
    new_value = previous_value + offset
    if (frame / fps > 27):
        new_value = max(58, min(new_value, 62))
        return new_value    
    new_value = max(83, min(new_value, 87))
    return new_value

# Update the line at each frame
def update(frame):
    if frame == len(confidence_values):
        # Calculate new value based on the last value in the list
        new_value = calculate_confidence(frame, confidence_values[-1])
        confidence_values.append(new_value)

    # Clear the current plot
    ax.clear()

    # Set plot limits and labels
    ax.set_xlim(0, total_seconds*fps)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Elapsed Time (s)', fontsize=20)
    ax.set_ylabel('System Confidence Level (%)', fontsize=20)
    plt.tick_params(axis='both', which='major', labelsize=18)
    ax.set_xticks([i * fps for i in range(0, total_seconds + 1, tick_interval)])
    ax.set_xticklabels([str(i + timeoffset) for i in range(0, total_seconds + 1, tick_interval)])

    # Plot the first part of the data in blue
    ax.plot(range(min(frame, 15*fps)), confidence_values[:min(frame, 15*fps)], lw=6)

    # Plot the last 15 seconds of the data in a different color
    if frame > 15*fps:
        ax.plot(range(15*fps, frame), confidence_values[15*fps:frame], color='orange', lw=6)

    return line,

# Create the animation
anim = animation.FuncAnimation(fig, update, frames=total_frames, interval = 1000/fps)

# plt.show()
# Save the animation as a GIF
Writer = animation.FFMpegWriter(fps=fps)
anim.save("120cdown.gif", writer=Writer) # curve up 60 offset
