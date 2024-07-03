filename = 'example.txt'
for i in range(100):
    with open(filename, 'a') as file:
        file.write(f"This is line{i}.\n")