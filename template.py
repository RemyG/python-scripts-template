import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="show program version", action="store_true")

args = parser.parse_args()

if args.version:
    print("Version 0.1")
