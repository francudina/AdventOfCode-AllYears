with open('input.txt') as f:
    line = [list(line.strip()) for line in f][0]

pairs = [(int(line[i]), 0 if i+1 >= len(line) else int(line[i+1])) for i in range(0, len(line), 2)]

disk = []
files, space = {}, {}
for i, (count, spaces) in enumerate(pairs):

    files[i] = (len(disk), count)
    space[len(disk)+count] = spaces

    disk.extend([i]*count)
    disk.extend(['.']*spaces)


for f_id, (f_ind, f_space) in list(files.items())[::-1]:
    s_found_ind = -1
    for s_ind, s_space in dict(sorted(space.items())).items():

        if f_ind < s_ind:
            break

        if f_space <= s_space:
            disk[s_ind:s_ind+f_space] = [f_id]*f_space
            disk[files[f_id][0]:files[f_id][0]+f_space] = ['.']*f_space

            s_found_ind = s_ind
            break

    if s_found_ind == -1:
        continue

    if f_space < space[s_found_ind]:
        space[s_found_ind+f_space] = space[s_found_ind] - f_space
    del space[s_found_ind]


rez = sum([i*v for i, v in enumerate(disk) if disk[i] != '.'])
print(f'Result: {rez}')
