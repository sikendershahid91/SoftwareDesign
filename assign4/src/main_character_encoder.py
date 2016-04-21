from processing_unit import ProcessingUnit
from block_create import block_create
import sys


def main():
    with open(sys.path[0] + '/filename.txt', 'r') as file:
        input_string = file.read().splitlines()
        print(input_string)
    for x in input_string:
        print(x)
        blocks = block_create(x)
        print(blocks)
    #blocks = map(block_create("{:s}".format(input_string)), input_string)
    #print(blocks)


if __name__ == '__main__':
    main()
