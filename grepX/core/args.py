import argparse

parser = argparse.ArgumentParser(description="grep stuff")
parser.add_argument('file', help="Specify the file")
parser.add_argument('pattern', help="Specify the pattern")
parser.add_argument('-s', '--silent', help="This option will disable the printing of URLs.", action="store_true")
parser.add_argument('-o', '--output', help="Specify the output file.", default='grepX_output.txt')
args = parser.parse_args()
FILE = args.file
PATTERN = args.pattern
SILENT = args.silent
OUTPUT = args.output