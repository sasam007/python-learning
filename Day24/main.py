try:
    with open("text.txt") as data:
        print(data.read())
except FileNotFoundError:
    print("The file text.txt does not exist.")
