import argparse

parser = argparse.ArgumentParser(description="grep patterns")
parser.add_argument('file', help="Specify the file")
parser.add_argument('pattern', help="Specify the pattern")
args = parser.parse_args()
FILE = args.file
PATTERN = args.pattern