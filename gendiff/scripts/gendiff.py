#!/usr/bin/env python
import argparse
from gendiff.gendiff import generate_diff


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()
answer = generate_diff(args.first_file, args.second_file)


def main():
    print(answer)


if __name__ == '__main__':
    main()
