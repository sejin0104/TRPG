import Color

player = {
    "max_health": 1000,
    "current_health": 10,
    "attack": 10,
    "defense": 10,
    "speed": 10,
    "level": 1,
    "experience": 0,
}

def Inventory(user):
    print('Inventory')
    
def DisplayHealth(target):
    
    health_percentage = target['current_health'] / target['max_health']

    # Determine the number of filled and empty blocks in the health bar
    filled_blocks = int(20 * health_percentage)
    empty_blocks = 20 - filled_blocks

    # Draw the health bar
    health_bar = '[' + '|' * filled_blocks + ' ' * empty_blocks + ']'
    
    # Format the health information
    health_info = f"({target['current_health']}/{target['max_health']})"

    # Print the health bar and health info
    print(Color.BRIGHT_GREEN + health_bar + Color.BRIGHT_YELLOW + health_info + Color.BRIGHT_WHITE)
    
DisplayHealth(player)
    
