
def load_struct(lines: [str]):

    def current_struct(current: [], paths: {}):
        tmp = paths
        for c in current:
            tmp = tmp[c]
        return tmp

    file_paths = {
        '/': {}
    }
    current_path = ['/']

    for l in lines[1:]:

        is_command = '$' == l[0]

        if is_command and 'cd' in l:
            dir_name = l.split(' ')[2]
            # dir_name = '' if dir_name == '/' else dir_name

            if dir_name == '..':
                # last element is parent
                current_path.pop()
            else:
                # next element is child
                current_path.append(dir_name)

        elif is_command and 'ls' in l:
            # skip ls because it's expected after 'cd *'
            continue

        else:
            dir_or_file_name = l.split(' ')[1]
            dir_or_file_value = {} if 'dir' in l else {'size': int(l.split(' ')[0]), 'file': True}

            current_file_paths: {} = current_struct(current_path, file_paths)
            current_file_paths[dir_or_file_name] = dir_or_file_value

    return file_paths


def calculate(file_paths: {}, values: [], max_limit: int):

    if 'file' in file_paths.keys():
        # get file size
        return file_paths['size']

    total = sum([
        calculate(file_paths[k], values, max_limit) for k in file_paths
    ])

    # check file limit
    if total <= max_limit:
        values.append(total)

    return total


with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

file_paths = load_struct(lines)

max_limit = 100000
values = []

total_results = calculate(file_paths, values, max_limit)
print(f"Total result: {sum(values)}")
