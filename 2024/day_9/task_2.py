from task_1 import scan, disk_sum

disk, files, space = scan()

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
        space[s_found_ind+f_space] = space[s_found_ind]-f_space
    del space[s_found_ind]


print(f'Result: {disk_sum(disk=disk)}')
