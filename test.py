def get_file_lines(file):
    fi = open(file, 'r')

    all_content = fi.read()
    line_list = all_content.split("\n")

    return len(line_list)

def get_school(school):
    file = "hello.txt"

    fi = open(file, 'r')

    for i in range(get_file_lines(file) - 1):
        line = fi.readline()
        if school in line:
            return line


    return "No school applicable"

def get_number(school):
    line = get_school(school)
    returnValue = line.split("/")

    return returnValue[1]




print(get_number("Waterloo"))