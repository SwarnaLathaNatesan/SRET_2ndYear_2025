import pygame
import sys
import math
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1100, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sum Problem Visualization")

# Enhanced colors for better visual appeal
BACKGROUND = (25, 35, 50)  # Dark blue-gray
ARRAY_COLOR = (30, 144, 255)  # Dodger blue - more vibrant
HIGHLIGHT = (255, 215, 0)  # Gold - brighter
TEXT_COLOR = (240, 240, 250)  # Light gray-blue
DICT_BG = (45, 55, 75)  # Dark blue-gray
DICT_BORDER = (100, 130, 160)  # Medium blue-gray - brighter
SUCCESS = (50, 205, 50)  # Lime green - more vibrant
FAIL = (255, 99, 71)  # Tomato red - more vibrant
CONTAINER_COLOR = (70, 170, 200)  # Bright blue for dictionary items

# Fonts
font_large = pygame.font.SysFont('Arial', 34, bold=True)
font_medium = pygame.font.SysFont('Arial', 26)
font_small = pygame.font.SysFont('Arial', 20)

# Two sum problem parameters
numbers = [7, 12, 4, 9, 3, 15]
target = 10

class NumberBall:
    def __init__(self, number, index, x, y):
        self.number = number
        self.index = index
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.radius = 32
        self.color = ARRAY_COLOR
        self.speed = 0.1
        self.moving = False
        self.highlight = False
        self.highlight_time = 0
        self.gloss_angle = random.uniform(0, 2 * math.pi)
        self.in_container = False
        self.show_index = True
        
    def draw(self, surface):
        # Draw main ball with gradient
        for i in range(self.radius, 0, -1):
            alpha = 255 - (self.radius - i) * 5
            if alpha < 0:
                alpha = 0
            # Create gradient from dark to light
            color = (
                max(self.color[0] - (self.radius - i) * 2, 0),
                max(self.color[1] - (self.radius - i) * 2, 0),
                max(self.color[2] - (self.radius - i) * 2, 0)
            )
            pygame.draw.circle(surface, color, (int(self.x), int(self.y)), i)
        
        # Draw specular highlight (main gloss)
        highlight_size = self.radius * 0.6
        highlight_x = self.x - self.radius * 0.3
        highlight_y = self.y - self.radius * 0.3
        
        for i in range(int(highlight_size), 0, -1):
            alpha = 180 - i * 4
            if alpha < 0:
                alpha = 0
            highlight_surf = pygame.Surface((i * 2, i * 2), pygame.SRCALPHA)
            pygame.draw.circle(highlight_surf, (255, 255, 255, alpha), (i, i), i)
            surface.blit(highlight_surf, (highlight_x - i, highlight_y - i))
        
        # Draw secondary highlight (smaller, brighter)
        small_highlight_size = self.radius * 0.3
        small_highlight_x = self.x - self.radius * 0.2
        small_highlight_y = self.y - self.radius * 0.2
        
        for i in range(int(small_highlight_size), 0, -1):
            alpha = 200 - i * 8
            if alpha < 0:
                alpha = 0
            small_highlight_surf = pygame.Surface((i * 2, i * 2), pygame.SRCALPHA)
            pygame.draw.circle(small_highlight_surf, (255, 255, 255, alpha), (i, i), i)
            surface.blit(small_highlight_surf, (small_highlight_x - i, small_highlight_y - i))
        
        # Draw highlight effect if active
        if self.highlight:
            pygame.draw.circle(surface, HIGHLIGHT, (int(self.x), int(self.y)), self.radius + 4, 3)
            self.highlight_time += 1
            if self.highlight_time > 40:
                self.highlight = False
                self.highlight_time = 0
        
        # Draw number with shadow effect
        shadow_text = font_medium.render(str(self.number), True, (0, 0, 0, 100))
        shadow_rect = shadow_text.get_rect(center=(int(self.x) + 2, int(self.y) + 2))
        surface.blit(shadow_text, shadow_rect)
        
        text = font_medium.render(str(self.number), True, (255, 255, 255))
        text_rect = text.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(text, text_rect)
        
        # Draw index if enabled
        if self.show_index:
            index_text = font_small.render(f"Index: {self.index}", True, TEXT_COLOR)
            index_rect = index_text.get_rect(center=(int(self.x), int(self.y) + self.radius + 18))
            surface.blit(index_text, index_rect)
    
    def move_to_target(self):
        if self.moving:
            dx = self.target_x - self.x
            dy = self.target_y - self.y
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance < 2:
                self.x = self.target_x
                self.y = self.target_y
                self.moving = False
                self.in_container = True
                # Hide index when in container to reduce clutter
                self.show_index = False

class DictionaryVisualizer:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.entries = {}
        self.entry_positions = {}
        
    def add_entry(self, key, value):
        self.entries[key] = value
        # Calculate position - place on right side of container with more space
        row = len(self.entries) - 1
        max_per_col = 4
        
        if row < max_per_col:
            # First column
            self.entry_positions[key] = (self.x + 100, self.y + 80 + row * 70)
        else:
            # Second column
            self.entry_positions[key] = (self.x + 250, self.y + 80 + (row - max_per_col) * 70)
        
    def draw(self, surface):
        # Draw dictionary container with rounded corners
        pygame.draw.rect(surface, DICT_BG, (self.x, self.y, self.width, self.height), border_radius=12)
        pygame.draw.rect(surface, DICT_BORDER, (self.x, self.y, self.width, self.height), 3, border_radius=12)
        
        # Draw title
        title_text = font_medium.render("Dictionary (Number → Index)", True, TEXT_COLOR)
        surface.blit(title_text, (self.x + 20, self.y + 15))
        
        # Draw entry labels
        for i, (key, value) in enumerate(self.entries.items()):
            pos_x, pos_y = self.entry_positions[key]
            
            # Draw key → value text
            key_text = font_medium.render(f"{key} → {value}", True, TEXT_COLOR)
            surface.blit(key_text, (pos_x - 25, pos_y - 30))

def draw_array(surface, nums, current_index):
    # Draw array indices
    for i in range(len(nums)):
        color = HIGHLIGHT if i == current_index else TEXT_COLOR
        index_text = font_small.render(f"[{i}]", True, color)
        surface.blit(index_text, (120 + i * 100, 100))
    
    # Draw array values
    for i, num in enumerate(nums):
        color = HIGHLIGHT if i == current_index else TEXT_COLOR
        value_text = font_medium.render(str(num), True, color)
        surface.blit(value_text, (120 + i * 100, 130))

def draw_legend(surface):
    # Draw legend
    pygame.draw.rect(surface, (40, 50, 70), (WIDTH - 220, HEIGHT - 150, 200, 140), border_radius=8)
    pygame.draw.rect(surface, DICT_BORDER, (WIDTH - 220, HEIGHT - 150, 200, 140), 2, border_radius=8)
    
    legend_title = font_small.render("Legend", True, HIGHLIGHT)
    surface.blit(legend_title, (WIDTH - 210, HEIGHT - 140))
    
    # Current element
    pygame.draw.circle(surface, HIGHLIGHT, (WIDTH - 210, HEIGHT - 110), 10)
    current_text = font_small.render("Current element", True, TEXT_COLOR)
    surface.blit(current_text, (WIDTH - 195, HEIGHT - 115))
    
    # In dictionary
    pygame.draw.circle(surface, CONTAINER_COLOR, (WIDTH - 210, HEIGHT - 85), 10)
    dict_text = font_small.render("In dictionary", True, TEXT_COLOR)
    surface.blit(dict_text, (WIDTH - 195, HEIGHT - 90))
    
    # Solution
    pygame.draw.circle(surface, SUCCESS, (WIDTH - 210, HEIGHT - 60), 10)
    solution_text = font_small.render("Solution pair", True, TEXT_COLOR)
    surface.blit(solution_text, (WIDTH - 195, HEIGHT - 65))
    
    # Need complement
    pygame.draw.circle(surface, FAIL, (WIDTH - 210, HEIGHT - 35), 10)
    complement_text = font_small.render("Need complement", True, TEXT_COLOR)
    surface.blit(complement_text, (WIDTH - 195, HEIGHT - 40))

def main():
    # Create number balls with more spacing
    number_balls = []
    for i, num in enumerate(numbers):
        ball = NumberBall(num, i, 120 + i * 100, 240)
        number_balls.append(ball)
    
    # Create dictionary visualizer with more space on the right
    dict_visualizer = DictionaryVisualizer(700, 100, 350, 500)
    
    # Animation state
    state = "start"
    current_index = 0
    found_pair = None
    complement = None
    animation_timer = 0
    message = "Two Sum Problem: Find two numbers that add up to " + str(target)
    
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and state == "done":
                    # Reset animation
                    number_balls = []
                    for i, num in enumerate(numbers):
                        ball = NumberBall(num, i, 120 + i * 100, 240)
                        number_balls.append(ball)
                    dict_visualizer = DictionaryVisualizer(700, 100, 350, 500)
                    state = "start"
                    current_index = 0
                    found_pair = None
                    complement = None
                    animation_timer = 0
        
        # Update number balls
        for ball in number_balls:
            ball.move_to_target()
        
        # Animation states
        if state == "start":
            if animation_timer > 60:
                state = "processing"
                animation_timer = 0
                
        elif state == "processing":
            if animation_timer % 60 == 0 and current_index < len(numbers):
                current_num = numbers[current_index]
                complement = target - current_num
                
                # Highlight current number
                number_balls[current_index].highlight = True
                
                if complement in dict_visualizer.entries:
                    # Found a pair
                    found_pair = (dict_visualizer.entries[complement], current_index)
                    state = "found"
                    message = f"Found pair: {numbers[found_pair[0]]} + {numbers[found_pair[1]]} = {target}"
                    number_balls[found_pair[0]].color = SUCCESS
                    number_balls[found_pair[1]].color = SUCCESS
                    # Show indices for solution
                    number_balls[found_pair[0]].show_index = True
                    number_balls[found_pair[1]].show_index = True
                else:
                    # Add to dictionary
                    dict_visualizer.add_entry(current_num, current_index)
                    # Move the ball to the dictionary
                    target_x, target_y = dict_visualizer.entry_positions[current_num]
                    number_balls[current_index].target_x = target_x
                    number_balls[current_index].target_y = target_y
                    number_balls[current_index].moving = True
                    number_balls[current_index].color = CONTAINER_COLOR
                    message = f"Added {current_num} to dictionary. Need complement: {complement}"
                    current_index += 1
            elif current_index >= len(numbers):
                state = "not_found"
                message = "No solution found!"
        
        elif state == "found":
            # Highlight both numbers in the pair
            if animation_timer % 30 == 0:
                number_balls[found_pair[0]].highlight = True
                number_balls[found_pair[1]].highlight = True
                
        elif state == "not_found":
            pass
            
        # Draw everything
        screen.fill(BACKGROUND)
        
        # Draw decorative background elements
        for i in range(20):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            size = random.randint(1, 3)
            alpha = random.randint(20, 100)
            dot_color = (100, 120, 150, alpha)
            dot_surf = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
            pygame.draw.circle(dot_surf, dot_color, (size, size), size)
            screen.blit(dot_surf, (x, y))
        
        # Draw title
        title_text = font_large.render("Two Sum Problem Visualization", True, TEXT_COLOR)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 20))
        
        # Draw target
        target_text = font_medium.render(f"Target: {target}", True, HIGHLIGHT)
        screen.blit(target_text, (WIDTH - 150, 25))
        
        # Draw array
        draw_array(screen, numbers, current_index)
        
        # Draw dictionary
        dict_visualizer.draw(screen)
        
        # Draw number balls
        for ball in number_balls:
            ball.draw(screen)
        
        # Draw legend
        draw_legend(screen)
        
        # Draw status message box
        pygame.draw.rect(screen, (40, 50, 70), (WIDTH // 2 - 300, HEIGHT - 120, 600, 100), border_radius=10)
        pygame.draw.rect(screen, DICT_BORDER, (WIDTH // 2 - 300, HEIGHT - 120, 600, 100), 2, border_radius=10)
        
        message_text = font_medium.render(message, True, TEXT_COLOR)
        screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, HEIGHT - 95))
        
        # Draw complement info if needed
        if complement is not None and state == "processing":
            complement_text = font_small.render(f"Complement for {numbers[current_index]} is {complement}", True, HIGHLIGHT)
            screen.blit(complement_text, (WIDTH // 2 - complement_text.get_width() // 2, HEIGHT - 65))
        
        # Draw instructions
        if state == "done" or state == "found" or state == "not_found":
            instruction = font_small.render("Press SPACE to restart", True, HIGHLIGHT)
            screen.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, HEIGHT - 40))
        else:
            instruction = font_small.render("Watch the algorithm check for complements...", True, TEXT_COLOR)
            screen.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, HEIGHT - 40))
        
        pygame.display.flip()
        clock.tick(60)
        animation_timer += 1
        
        # Move to next state after a delay
        if state == "found" and animation_timer > 180:
            state = "done"
        elif state == "not_found" and animation_timer > 120:
            state = "done"
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()