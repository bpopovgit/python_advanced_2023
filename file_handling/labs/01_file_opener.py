try:
    file = open("text.txt", "r")
    print(f"Found")
    file.close()
except FileNotFoundError:
    print("File not found")
