lines = ["one", "two", "three"]
with open("input.txt", "w") as file:
    for i in lines:
        file.write(f"cycle run {i}")
    print("done")