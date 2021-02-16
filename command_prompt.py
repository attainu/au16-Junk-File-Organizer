from methods.selected_method import OrganiseMethod
import sys
import argparse


def run(args):
    OrganiseMethod(args.d, args.o)
    return 'Finish'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-d', type = str, default = None,
                        help = "Give the directory address where you want to run the junk_file_organiser")

    parser.add_argument('-o', type = str, default = None,
                        help = "Give the organising method")

    args = parser.parse_args()
    
    sys.stdout.write(run(args))

# python command_prompt.py -d "C:\Users\Vibhor Verma\Desktop\testing" -o "extension"