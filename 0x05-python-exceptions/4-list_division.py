#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = [0 for i in range(list_length)]
    for n in range(list_length):
        try:
           res[n] = (my_list_1[n] / my_list_2[n])
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            pass
    return res 
