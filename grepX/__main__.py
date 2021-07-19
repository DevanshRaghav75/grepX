import threading
from concurrent.futures import ThreadPoolExecutor
from grepX.core.args import PATTERN, FILE, OUTPUT, THREADS
from grepX.core.greper import grep_idor, grep_lfi, grep_rce, grep_redirect, grep_sqli, grep_ssrf, grep_ssti, grep_xss
from grepX.core.colors import RED, RESET

def grep():
    if PATTERN == 'xss':
        try:
            with ThreadPoolExecutor(max_workers=THREADS) as executor:
                executor.submit(grep_xss)
        except KeyboardInterrupt:
            quit()
    elif PATTERN == 'sqli':
        try:
            with ThreadPoolExecutor(max_workers=THREADS) as executor:
                executor.submit(grep_sqli)
        except KeyboardInterrupt:
            quit()
    elif PATTERN == 'lfi':
        try:
            with ThreadPoolExecutor(max_workers=THREADS) as executor:
                executor.submit(grep_lfi)
        except KeyboardInterrupt:
            quit()
    elif PATTERN == 'rce':
        try:
            with ThreadPoolExecutor(max_workers=THREADS) as executor:
                executor.submit(grep_rce)
        except KeyboardInterrupt:
            quit()
    elif PATTERN == 'idor':
        try:
            with ThreadPoolExecutor(max_workers=THREADS) as executor:
                executor.submit(grep_idor)
        except KeyboardInterrupt:
            quit()
    elif PATTERN == 'ssrf':
        try:
            with ThreadPoolExecutor(max_workers=THREADS) as executor:
                executor.submit(grep_ssrf)
        except KeyboardInterrupt:
            quit()
    elif PATTERN == 'redirect':
        try:
            with ThreadPoolExecutor(max_workers=THREADS) as executor:
                executor.submit(grep_redirect)
        except KeyboardInterrupt:
            quit()
    elif PATTERN == 'ssti':
        try:
            with ThreadPoolExecutor(max_workers=THREADS) as executor:
                executor.submit(grep_ssti)
        except KeyboardInterrupt:
            quit()
    else:
        print(RED + '[-] ' + RESET + "No such pattern :(")
