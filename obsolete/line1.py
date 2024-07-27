import matplotlib.pyplot as plt
from matplotlib import animation
import random

# Set the figure size
plt.rcParams['figure.figsize'] = (8, 6)

# Initialize the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)  # Initialize an empty line

# Set plot limits and labels
ax.set_xlim(0, 15*24) # 75 seconds in total 60 high 15 low
ax.set_ylim(0, 100)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Autonomous Driving Confidence')

tick_interval = 5  # Interval of 5 seconds
ax.set_xticks([i * fps for i in range(0, 15 + 1, tick_interval)])  # Set ticks at every 5 seconds
ax.set_xticklabels([str(i) for i in range(0, 15 + 1, tick_interval)])  # Label ticks with every 5 seconds

confidence_values = [100]  # Confidence default starts at 100

def calculate_confidence(frame, previous_value):
    time = frame / fps  # Divide by FPS to calculate time
    
    # Generate a random offset
    offset = random.uniform(-2, 2)
    new_value = previous_value + offset
    
    if time < 6:
        new_value = max(85, min(new_value, 100))
    else:
        new_value = max(60, min(new_value, 85))
    return new_value

def update(frame):
    confidence_values.append(calculate_confidence(frame, confidence_values[-1]))
    line.set_data(range(len(confidence_values)), confidence_values)
    return line,

def create_animation():
    anim = animation.FuncAnimation(fig, update, frames=total_frames)
    Writer = animation.FFMpegWriter(fps=fps)  # 1 frame per second for 85 seconds
    anim.save("line_graph2.gif", writer=Writer)

def main():
    create_animation()
    plt.show()

if __name__ == "__main__":
    main()