import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

fig, ax = plt.subplots(figsize=(12, 8), facecolor='black')
ax.set_facecolor('black')

def animate_spiral_wave(frame):
    ax.clear()
    ax.set_facecolor('black')
    
    t = frame * 0.1
    
    theta = np.linspace(0, 8*np.pi, 500)
    r = np.linspace(0.1, 5, 500)
    
    x = r * np.cos(theta + t) * np.cos(t * 0.5)
    y = r * np.sin(theta + t) * np.sin(t * 0.3)
    
    colors = np.sin(theta + t * 2) * 0.5 + 0.5
    
    scatter = ax.scatter(x, y, c=colors, s=50, cmap='plasma', alpha=0.8)
    
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.set_title('Animated Spiral Wave', color='white', fontsize=16, pad=20)
    
    return scatter,

ani = animation.FuncAnimation(fig, animate_spiral_wave, frames=200, 
                            interval=50, blit=False, repeat=True)

plt.tight_layout()
plt.show()

print("🌟 Cool visualization created! Press Ctrl+C to stop the animation.")