user_input = input("camelCase: ")
snake_case = ""

for alphabet in user_input:
    if alphabet.isupper():
        snake_case += "_" + alphabet.lower()
    else :
        snake_case += alphabet
print(snake_case)
    