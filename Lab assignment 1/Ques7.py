#7.1
with open("sample.txt","w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("It contains some sample text.\n")
with open("sample.txt","r") as file:
    content = file.read()
    print("Content of the file:")
    print(content)


#7.2
with open("sample.txt", "a") as file:
    file.write("This is additional text appended to the file.\n")
with open("sample.txt", "r") as file:
    content = file.read()
    print("Updated content of the file:")
    print(content)


#7.3
def count_lines(file_name):
    with open(file_name,"r") as file:
        lines=file.readlines()
        return len(lines)
file_name="sample.txt"
line_count=count_lines(file_name)
print(f"The number of lines in the file is:{line_count}")
