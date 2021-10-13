# Coded by @HS Devansh Raghav
# follow me on instagram :) - https://instagram.com/hs_devansh_raghav.75

import threading
from concurrent.futures import ThreadPoolExecutor
from grepX.core.args import PATTERN, FILE, CONCURRENCY
from grepX.core.colors import RED, RESET
from grepX.core.greper import  greper ,xss_patterns, sqli_patterns, ssrf_patterns, ssti_patterns, lfi_patterns, rce_patterns, idor_patterns, redirect_patterns

def grep():
    if PATTERN == 'xss':
        try:
            with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
                for each_pattern in xss_patterns:
                    executor.submit(greper, each_pattern)
        except KeyboardInterrupt:
            quit()
    
    elif PATTERN == 'sqli':
        try:
            with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
                for each_pattern in sqli_patterns:
                    executor.submit(greper, each_pattern)
        except KeyboardInterrupt:
            quit()
    
    elif PATTERN == 'lfi':
        try:
            with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
                for each_pattern in lfi_patterns:
                    executor.submit(greper, each_pattern)
        except KeyboardInterrupt:
            quit()
    
    elif PATTERN == 'rce':
        try:
            with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
                for each_pattern in rce_patterns:
                    executor.submit(greper, each_pattern)
        except KeyboardInterrupt:
            quit()

    elif PATTERN == 'idor':
        try:
            with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
                for each_pattern in idor_patterns:
                    executor.submit(greper, each_pattern)
        except KeyboardInterrupt:
            quit()

    elif PATTERN == 'ssrf':
        try:
            with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
                for each_pattern in ssrf_patterns:
                    executor.submit(greper, each_pattern)
        except KeyboardInterrupt:
            quit()

    elif PATTERN == 'redirect':
        try:
            with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
                for each_pattern in redirect_patterns:
                    executor.submit(greper, each_pattern)
        except KeyboardInterrupt:
            quit()

    elif PATTERN == 'ssti':
        try:
            with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
                for each_pattern in ssti_patterns:
                    executor.submit(greper, each_pattern)
        except KeyboardInterrupt:
            quit()
    else:
        print(RED + '[-] ' + RESET + "No such pattern :(")
