import argparse

parser = argparse.ArgumentParser(description="grep stuff")
parser.add_argument('file', help="Specify the file")
parser.add_argument('pattern', help="Specify the pattern - eg.[xss, sqli, lfi, ssrf, ssti, redirect, rce, idor]")
parser.add_argument('-s', '--silent', help="This option will disable the printing of URLs", action="store_true")
parser.add_argument('-o', '--output', help="Specify the output file.", default='grepX_output.txt')
parser.add_argument('-t', '--threads', help="Specify the threads you want to use, default threads are 100", default=100, type=int)
args = parser.parse_args()
FILE = args.file
PATTERN = args.pattern
SILENT = args.silent
OUTPUT = args.output
THREADS = args.threads