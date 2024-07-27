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

# Set plot limits and labels
ax.set_xlim(0, total_seconds*fps) # 75 seconds in total 60 high 15 low
ax.set_ylim(0, 100)
ax.set_xlabel('Elapsed Time (s)', fontsize=20)
ax.set_ylabel('System Confidence Level (%)', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=18)

timeoffset = 60 # Starting time of the x-axis

tick_interval = 5  # Interval of 5 seconds
ax.set_xticks([i * fps for i in range(0, total_seconds + 1, tick_interval)])  # Set ticks at every 5 seconds
ax.set_xticklabels([str(i + timeoffset) for i in range(0, total_seconds + 1, tick_interval)])  # Label ticks with every 5 seconds

confidence_values = [85]  # Confidence default starts at 100

# Calculate the confidence value
def calculate_confidence(frame, previous_value):
    # Generate a random offset
    if (frame / fps > 15): 
        return previous_value - 0.06
        
    offset = random.uniform(-1, 1)
    new_value = previous_value + offset
    new_value = max(82, min(new_value, 88))

    return new_value

# Update the line at each frame
def update(frame):
    if frame == len(confidence_values):
        # Calculate new value based on the last value in the list
        new_value = calculate_confidence(frame, confidence_values[-1])
        confidence_values.append(new_value)

    # Update the line data
    line.set_data(range(frame+1), confidence_values[:frame+1])

    return line,

# Create the animation
anim = animation.FuncAnimation(fig, update, frames=total_frames, interval = 1000/fps)

# plt.show()
# Save the animation as a GIF
Writer = animation.FFMpegWriter(fps=fps)  # 1 frame per second for 85 seconds
anim.save("d60of.gif", writer=Writer)
