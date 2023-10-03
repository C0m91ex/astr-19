# Code Journal Prompt #1

# Information for the prompt is defined here
full_name = "Jason Torres"
pronouns = "he/him"  

favorite_movie = "My favorite movie is 'Star Wars: Rogue One', it's a fun side story from the events of the main movies that shows the hardships of the rebellion from a new pov."
favorite_food = "My favorite food is an In-N-Out cheese burger, a classic cheese burger from In-N-Out always hits the spot."

# This function will print the information
def PrintInformation():
    print(f"Full Name: {full_name}")
    print(f"Preferred Pronouns: {pronouns}")
    print(f"Favorite Movie: {favorite_movie}")
    print(f"Favorite Food: {favorite_food}")

# This defines the main() funtion for our program
def main():
    PrintInformation()

# When we run the program this executes first
if __name__=="__main__":
    main()