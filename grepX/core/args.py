import argparse

parser = argparse.ArgumentParser(description="grep stuff")
parser.add_argument('file', help="Specify the file")
parser.add_argument('pattern', help="Specify the pattern - eg.[xss, sqli, lfi, ssrf, ssti, redirect, rce, idor]")
parser.add_argument('-s', '--silent', help="This option will disable the printing of URLs", action="store_true")
parser.add_argument('-c', '--concurrency', help="Specify concurrency, default is 100", default=100, type=int)
args = parser.parse_args()
FILE = args.file
PATTERN = args.pattern
SILENT = args.silent
CONCURRENCY = args.concurrency