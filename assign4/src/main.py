from processing_unit import ProcessingUnit
from block_file_handle import block_file_handle
import sys


def main():
    file_name = 'user_blocks.txt' #Venkat: Can we move the user_blocks.txt file from src to assign4. This should not belong in the src directory.
    blocks = block_file_handle(sys.path[0] + '/' + file_name)

    print('Block sequence loaded from {}'.format(file_name))
    process_unit = ProcessingUnit(blocks)

    while True: #Venkat: use a couple of hard coded input here for demo purpose. That way it can be easily automated in the run to show program working
        print("String for process :: ", end = '')
        print(process_unit.process(input()))


if __name__ == '__main__':
    main()
