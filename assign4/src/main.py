from processing_unit import ProcessingUnit
from block_file_handle import block_file_handle
import sys


def main():
    file_name = 'user_blocks.txt'
    blocks = block_file_handle(sys.path[0] + '/../' + file_name)

    print('Block sequence loaded from {}'.format(file_name))
    process_unit = ProcessingUnit(blocks)

    demo_inputs = ['123dsdfaw34saf',
        '0asd9fADSFf',
        'AbcZZ##']
    if demo_inputs:
        print('\nDemo mode in use.\n')
        for line in demo_inputs:
            print("String for process :: " + line, end = '')
            print(process_unit.process(line))
    else:
        while True:
            print("String for process :: ", end = '')
            print(process_unit.process(input()))


if __name__ == '__main__':
    main()
