import os


files = os.listdir("components/fonts/Dana")
all_fonts = []

for file in files:
    all_fonts.append(file.split('.')[0])


print(", ".join(all_fonts))