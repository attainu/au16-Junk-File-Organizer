from methods.selected_method import OrganiseMethod
import sys
import argparse


def run(args):
    OrganiseMethod(args.d, args.o)
    return 'Finish'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    comment_one = "Give the directory address where you want to run the"
    comment_one += "junk_file_organiser"
    parser.add_argument('-d', type=str, default=None, help=comment_one)

    comment_two = "Give the organising method"
    parser.add_argument('-o', type=str, default=None, help=comment_two)

    args = parser.parse_args()
    sys.stdout.write(run(args))
