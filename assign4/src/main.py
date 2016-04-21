from processing_unit import ProcessingUnit
from block_create import block_create
import sys


def main():
    with open(sys.path[0] + '/filename.txt', 'r') as file:
        input_string = file.read().splitlines()
    blocks = map(block_create, input_string)


if __name__ == '__main__':
    main()
