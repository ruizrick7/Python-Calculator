#ask user foer their username
name = input("What's your name? ").strip().title()

# split username into first name and last name
first, last = name.split(" ")

# say hello to user
print(f"Hello, {first}") 