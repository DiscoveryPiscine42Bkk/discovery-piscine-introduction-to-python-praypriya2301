import sys

if len(sys.argv) != 2:
    print("none")
else:
    intput_string = sys.argv[1]
    z_chars = [char for char in intput_string if char == 'z']
    if z_chars:
        print(''.joint(z_chars))
    else:
        print("none")