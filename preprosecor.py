import glob


def add_include(_line):
    include_file_name = _line.split("\"", 2)[1]
    with open(include_file_name) as include_file:
        return include_file.read()


for filename in glob.glob('*.c*'):
    with open(filename, 'r+') as cpp:
        include_content = ""
        for line in cpp:
            if line.startswith("#includ"):
                include_content += add_include()
            if line.startswith("#defind"):
                pass

    cpp.write(include_content)
