import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (15, 212, 34)

# Snake segments
snake_segments = [(width // 2, height // 2)]
snake_direction = (0, 0)

# Food position
food_x = random.randint(0, width - 20)
food_y = random.randint(0, height - 20)

# Move the snake
def move_snake():
    global snake_segments
    head_x, head_y = snake_segments[0]
    dx, dy = snake_direction
    new_head_x = head_x + dx
    new_head_y = head_y + dy
    
    # Check if the snake has hit the wall
    if new_head_x < 0 or new_head_x >= width or new_head_y < 0 or new_head_y >= height:
        return False

    # Move all segments of the snake
    new_segments = [(new_head_x, new_head_y)] + snake_segments[:-1]
    snake_segments = new_segments
    return True

# Check collision with food
def check_collision():
    head_x, head_y = snake_segments[0]
    return (head_x < food_x + 20 and head_x + 20 > food_x and
            head_y < food_y + 20 and head_y + 20 > food_y)

# Draw the snake
def draw_snake():
    for segment in snake_segments:
        pygame.draw.rect(screen, green, (*segment, 20, 20))

# Draw the food
def draw_food():
    pygame.draw.rect(screen, white, (food_x, food_y, 20, 20))

# Add a segment to the end of the snake
def grow_snake():
    head_x, head_y = snake_segments[0]
    dx, dy = snake_direction
    new_segment = (head_x - dx, head_y - dy)
    snake_segments.append(new_segment)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    keys = pygame.key.get_pressed()  # Get the state of all keys
    if keys[pygame.K_w] and snake_direction != (0, 20):
        snake_direction = (0, -20)
    elif keys[pygame.K_s] and snake_direction != (0, -20):
        snake_direction = (0, 20)
    elif keys[pygame.K_a] and snake_direction != (20, 0):
        snake_direction = (-20, 0)
    elif keys[pygame.K_d] and snake_direction != (-20, 0):
        snake_direction = (20, 0)

    # Move the snake
    if not move_snake():
        running = False  # End the game if the snake hits the wall

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check collision with food
    if check_collision():
        food_x = random.randint(0, width - 20)
        food_y = random.randint(0, height - 20)
        grow_snake()

    # Clear the screen
    screen.fill(black)

    # Draw the snake and food
    draw_snake()
    draw_food()

    # Update the display
    pygame.display.flip()
    
    # Limit the frame rate
    clock.tick(15)  # Limit frame rate to 15 FPS

# Quit Pygame
pygame.quit()