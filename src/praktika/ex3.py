try:
    user_input = int(input("enter a number: "))
    print(f"2 + {user_input} = {2 + user_input}")

except ValueError:
    raise ValueError