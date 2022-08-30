#1/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_l = my_list.copy()
    new = []
    for n in range(len(new_l)):
        if new_l[n] % 2 == 0:
            new.append(new_l[n])
        else:
            new.append(False)
    return new
