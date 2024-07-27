import matplotlib.pyplot as plt
from matplotlib import animation
import random

confidence_values = [100]  # Confidence default starts at 100

# Calculate the confidence value
def calculate_confidence(frame, previous_value):
    time = frame / fps  # Divide by FPS to calculate time
    
    # Generate a random offset
    offset = random.uniform(-2, 2)
    new_value = previous_value + offset
    
    if time < 60:
        new_value = max(85, min(new_value, 100))
    else:
        new_value = max(60, min(new_value, 85))
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


def main() -> None:
    fps = 24
    total_seconds = 75 # 75 seconds in total 60 high 15 low
    total_frames = total_seconds * fps
    # Set the figure size
    plt.rcParams['figure.figsize'] = (8, 6)

    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)  # Initialize an empty line

    # Set plot limits and labels
    ax.set_xlim(0, 15*24) # Only show 15 time interval
    ax.set_ylim(0, 100)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Autonomous Driving Confidence')


    
    # Create the animation
    anim = animation.FuncAnimation(fig, update, frames=total_frames)

    # Save the animation as a GIF
    Writer = animation.FFMpegWriter(fps=fps)  # 1 frame per second for 85 seconds

    anim.save("line_graph2.gif", writer=Writer)
    # show tickers

# tick_interval = 5  
# ax.set_xticks([i * fps for i in range(0, 15 + 1, tick_interval)])  
# ax.set_xticklabels([str(i) for i in range(0, 15 + 1, tick_interval)]) 








