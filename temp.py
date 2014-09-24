#python
import sys
for num in range(1, 101):
    print_num = True
    if num % 3 == 0:
        sys.stdout.write("Crackle")
        #print('Crackle', end='',flush=True);
        print_num = False
    if num % 5 == 0:
        sys.stdout.write("Pop")
        print_num = False
    if print_num:
        print num,
    print