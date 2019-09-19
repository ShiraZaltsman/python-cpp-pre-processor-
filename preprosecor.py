import glob
import re


def get_include_path(_line):
    if "\"" in _line:
        return _line.split("\"", 2)[1]
    return "system/" + _line.split("<")[1].replace(">", ".h")


def include_list(header_filename, files):
    with open(header_filename, 'r') as header_file:
        for line in header_file:
            if line.startswith("#include \""):
                name = get_include_path(line.strip())
                files.append(name)
                return include_list(name, files)
            if line.startswith("#include <"):
                name = get_include_path(line.strip())
                files.append(name)

    return


def get_include_content(_headers_list):
    content = ""
    for file in _headers_list:
        with open(file, 'r') as f:
            for line in f:
                if not line.startswith("#include"):
                    content += line
    return content


def get_macros(ppfile):
    define_list = []
    lines = ppfile.split("\n")
    for line in lines:
        if line.startswith("#define"):
            define_list.append(line)
    return define_list


def get_param(line_param):
    parm = (line_param.split("(")[1].split(")")[0].replace(" ", "")).split(",")
    return parm


def set_macros(define_list, ppfile):
    for define in define_list:
        ppfile = ppfile.replace(define, "")
        if "__" not in define:
            define = define.replace("#define ", "")
            if "(" in define:
                macro_name = define.split("(")[0]
                parameters = get_param(define)
                action = define.split(")", 1)[1]
                reg = re.search(macro_name + "\(.*?\)", ppfile)
                if reg:
                    reg_match = reg.group(0)
                    values = get_param(reg_match)
                    new_action = action
                    for i in range(len(values)):
                        new_action = new_action.replace(parameters[i], values[i])
                    ppfile = ppfile.replace(reg_match, new_action)

            else:
                macro_name = define.split(" ")[0]
                value = define.split(" ")[1]
                ppfile = ppfile.replace(macro_name, value)

    return ppfile


for filename in glob.glob('*.cpp'):
    with open(filename, 'r+') as cpp:
        listofheaders = []
        include_list(filename, listofheaders)
        listofheaders.append(filename)
        listofheaders=set(listofheaders)
        ppfile = get_include_content(listofheaders)
        define_list = get_macros(ppfile)
        ppfile = set_macros(define_list, ppfile)
        newppFile = open(filename.replace("cpp", "pp"), "w")
        newppFile.write(ppfile)
