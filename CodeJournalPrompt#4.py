# Coding Journal Prompt #4

class SeaOtter:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length  # Length of the arms (float)
        self.leg_length = leg_length  # Length of the legs (float)
        self.num_eyes = num_eyes  # Number of eyes (int)
        self.has_tail = has_tail  # Does it have a tail? (bool)
        self.is_furry = is_furry  # Is it furry? (bool)

    def describe_animal(self):
        print("Sea Otter Characteristics:")
        print(f"Arm Length: {self.arm_length} inches")
        print(f"Leg Length: {self.leg_length} inches")
        print(f"Number of Eyes: {self.num_eyes}")
        print(f"Has Tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is Furry: {'Yes' if self.is_furry else 'No'}")

# Create an instance of the FavoriteAnimal class
my_favorite_animal = SeaOtter(4.5, 3.0, 2, True, True)

# Call the describe method to print the characteristics
my_favorite_animal.describe_animal()