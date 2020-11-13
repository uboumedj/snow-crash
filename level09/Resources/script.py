import sys

for i, char in enumerate(sys.argv[1]):
        sys.stdout.write(chr(ord(char) - i))
sys.stdout.write("\n")