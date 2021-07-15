<h1 align="center">grepX</h1>
<h3 align="center">Find URLs that contains XSS, SQLI, SSRF, SSTI, LFI, IDOR, RCE, REDIRECT patterns</h3>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![GitHub license](https://img.shields.io/github/license/DevanshRaghav75/grepX.svg)](https://github.com/DevanshRaghav75/grepX/blob/master/LICENSE.md)

## What is grepX?

`grepX` is a python script that finds `xss, sqli, idor, ssrf, ssti, rce, redirect ` paramters/patterns from URLs.  

## Usage

### Finding xss patterns
```
$ grepx urls_file xss
```

### Finding sqli patterns

```
$ grepx urls_file.txt sqli
```

### Finding idor patterns

```
$ grepx urls.txt idor
```

### Finding ssrf patterns

```
$ grepx urls.txt ssrf
```

**Hope you understood :)**

### Inspired by
* <a href="https://github.com/1ndianl33t/Gf-Patterns">Gf_Patterns by @1ndianl33t</a>
* <a href="https://github.com/tomnomnom/gf">gf by @tomnomnom</a>
