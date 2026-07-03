# sample to read the file
with open("01-python\\day05\\learning_notes.txt","r+") as file:
    print(file.read())
    lines_to_write = ["Line1\n","Line2"]
    file.writelines(lines_to_write)

