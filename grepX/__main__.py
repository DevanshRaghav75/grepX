from grepX.core.args import PATTERN, FILE, OUTPUT
from grepX.core.greper import grep_idor, grep_lfi, grep_rce, grep_redirect, grep_sqli, grep_ssrf, grep_ssti, grep_xss
from grepX.core.colors import RED, RESET

def grep():
    if PATTERN == 'xss':
        grep_xss()
    elif PATTERN == 'sqli':
        grep_sqli()
    elif PATTERN == 'lfi':
        grep_lfi()
    elif PATTERN == 'rce':
        grep_rce()
    elif PATTERN == 'idor':
        grep_idor()
    elif PATTERN == 'ssrf':
        grep_ssrf()
    elif PATTERN == 'redirect':
        grep_redirect()
    elif PATTERN == 'ssti':
        grep_ssti()
    else:
        print(RED + '[-] ' + RESET + "No such pattern :(")
