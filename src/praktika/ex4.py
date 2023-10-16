# The ugly apple
# go to the end
# soad ieaiaio

user_input = input("enter a string: ")

print(f"{len(user_input)=}")

print(f"lower: {user_input.lower()}")

print(f"количество гласных: {sum([user_input.count(i) for i in ['a', 'e', 'i', 'o', 'u']])}")

print(f"ugly to beauty: {user_input.replace('ugly', 'beauty')}")

if user_input.startswith("The"):
    print("придлоежние начинается с 'The'")

elif user_input.endswith("end"):
    print("предложение заканичвается на 'end'")