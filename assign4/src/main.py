from processing_unit import ProcessingUnit
from block_file_handle import block_file_handle
import sys


def main():
    file_name = 'user_blocks.txt'
    blocks = block_file_handle(sys.path[0] + '/' + file_name)

    print('Block sequence loaded from {}'.format(file_name))
    process_unit = ProcessingUnit(blocks)

    while True:
        print("String for process :: ", end = '')
        print(process_unit.process(input()))


if __name__ == '__main__':
    main()
