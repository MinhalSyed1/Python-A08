def function_names(filename):
    total = []
    read_file = filename.readlines()
    for line in read_file:
        if (line.startswith('def ')):
            func_names = line[4:line.find('(')]
            total = total + [func_names]
    return total