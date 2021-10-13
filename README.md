<h1 align="center">grepX</h1>
<h3 align="center">Find URLs that contains XSS, SQLI, SSRF, SSTI, LFI, IDOR, RCE, REDIRECT patterns</h3>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub release](https://img.shields.io/github/release/DevanshRaghav75/grepX.svg)](https://GitHub.com/DevanshRaghav75/grepX/releases/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![GitHub license](https://img.shields.io/github/license/DevanshRaghav75/grepX.svg)](https://github.com/DevanshRaghav75/grepX/blob/master/LICENSE.md)

## What is grepX?

grepX is a multithreaded CLI tool which finds `xss, sqli, ssrf, lfi, rce, redirect, ssti, idor` patterns/parameters from the given file and saves the output.

## Installation
```
$ git clone https://github.com/DevanshRaghav75/grepX.git
$ cd grepX
$ python3 setup.py install
$ grepX -h 
```
## Args
| Args       |   Discription                        |
|------------|--------------------------------------|
|file        | Specify the URLs file                |
|Pattern     | Specify the pattern you want to find |
|-s/--silent | Enable silent mode                   |
|-c/--concurrency| Specify the concurrency, default are 100 |

## Usage

### Finding sqli patterns

```
grepx urls.txt sqli 
```
### Finding xss patterns with silent and concurrency argument

```
grepx urls.txt xss --silent -c 20
```

### Finding and saving the output

```
grepx urls.txt lfi > urls.lfi
```


### Inspired by
* <a href="https://github.com/1ndianl33t/Gf-Patterns">Gf_Patterns by @1ndianl33t</a>
* <a href="https://github.com/tomnomnom/gf">gf by @tomnomnom</a>
