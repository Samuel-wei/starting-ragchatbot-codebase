import turtle
import math
import random

def setup_screen():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("🌈 Rainbow Circles - Cool Visualization!")
    screen.setup(width=800, height=600)
    screen.tracer(0)
    return screen

def create_artist():
    artist = turtle.Turtle()
    artist.speed(0)
    artist.shape("circle")
    artist.pensize(2)
    return artist

def rainbow_spiral():
    screen = setup_screen()
    artist = create_artist()
    
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
    
    for i in range(360):
        artist.pencolor(colors[i % len(colors)])
        artist.circle(i * 0.5)
        artist.right(91)
        artist.forward(i * 0.1)
        
        if i % 10 == 0:
            screen.update()
    
    screen.update()
    print("🎨 Rainbow spiral complete! Click the window to close.")
    screen.exitonclick()

def dancing_circles():
    screen = setup_screen()
    artist = create_artist()
    
    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FECA57", "#FF9FF3"]
    
    for angle in range(0, 720, 2):
        artist.pencolor(random.choice(colors))
        artist.goto(
            math.cos(math.radians(angle)) * angle * 0.2,
            math.sin(math.radians(angle)) * angle * 0.2
        )
        artist.circle(20 + angle * 0.05)
        
        if angle % 20 == 0:
            screen.update()
    
    screen.update()
    print("💃 Dancing circles complete! Click the window to close.")
    screen.exitonclick()

def main():
    print("🎉 Welcome to Cool Visualizations!")
    print("Choose your visualization:")
    print("1. Rainbow Spiral")
    print("2. Dancing Circles")
    
    choice = input("Enter 1 or 2 (or just press Enter for Rainbow Spiral): ").strip()
    
    if choice == "2":
        dancing_circles()
    else:
        rainbow_spiral()

if __name__ == "__main__":
    main()