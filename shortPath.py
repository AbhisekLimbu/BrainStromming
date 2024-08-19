# Dictionary to map each letter to its numerical position in the alphabet
alphabet_position = {
    'a': 1,  'b': 2,  'c': 3,  'd': 4,  'e': 5,
    'f': 6,  'g': 7,  'h': 8,  'i': 9,  'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26
}

# Function to get the numerical value of a given position
def get_numerical_value(position):
    return alphabet_position.get(position.lower())

# Function to calculate the total distance between two positions
def calculate_total_distance(my_position, desired_position):
    my_numerical_value = get_numerical_value(my_position)
    desired_numerical_value = get_numerical_value(desired_position)
    return abs(desired_numerical_value - my_numerical_value)

# Function to calculate forward or backward distance
def calculate_direction(my_position, desired_position):
    total_distance = calculate_total_distance(my_position, desired_position)
    
    if total_distance <= 13:
        direction = "forward"
    else:
        direction = "backward"
    
    return total_distance, direction

# Function to get user input
def user_input():
    my_position = input("Enter your position (a-z): ")
    desired_position = input("Where do you want to go (a-z)?: ")
    return my_position, desired_position

# Example usage
my_position, desired_position = user_input()
distance, direction = calculate_direction(my_position, desired_position)

print(f"The total distance from '{my_position}' to '{desired_position}' is {distance}.")
print(f"It is more feasible to go {direction}.")
