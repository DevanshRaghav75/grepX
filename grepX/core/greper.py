import re
import grepX.core.config as path
from grepX.core.colors import GRAY, GREEN, RESET, RED
from grepX.core.path_checker import compatible_path
from grepX.core.args import PATTERN, FILE

grepX_dir = compatible_path(path.__file__.replace(compatible_path('/core/config.py'), ''))
 
xss_patterns = [
"q=",
"s=",
"search=",
"lang=",
"keyword=",
"query=",
"page=",
"keywords=",
"year=",
"view=",
"email=",
"type=",
"name=",
"p=",
"callback=",
"jsonp=",
"api_key=",
"api=",
"password=",
"email=",
"emailto=",
"token=",
"username=",
"csrf_token=",
"unsubscribe_token=",
"id=",
"item=",
"page_id=",
"month=",
"immagine=",
"list_type=",
"url=",
"terms=",
"categoryid=",
"key=",
"l=",
"begindate=",
"enddate="
]

ssti_patterns = [

"template=",
"preview=",
"id=",
"view=",
"activity=",
"name=",
"content=",
"redirect="
]

ssrf_patterns = [

"access=", 
"admin=", 
"dbg=", 
"debug=", 
"edit=", 
"grant=", 
"test=", 
"alter=", 
"clone=", 
"create=", 
"delete=", 
"disable=", 
"enable=", 
"exec=", 
"execute=", 
"load=", 
"make=", 
"modify=", 
"rename=", 
"reset=", 
"shell=", 
"toggle=", 
"adm=", 
"root=", 
"cfg=",
"dest=", 
"redirect=", 
"uri=", 
"path=", 
"continue=", 
"url=", 
"window=", 
"next=", 
"data=", 
"reference=", 
"site=", 
"html=", 
"val=", 
"validate=", 
"domain=", 
"callback=", 
"return=", 
"page=", 
"feed=", 
"host=", 
"port=", 
"to=", 
"out=",
"view=", 
"dir=", 
"show=", 
"navigation=", 
"open=",
"file=",
"document=",
"folder=",
"pg=",
"php_path=",
"style=",
"doc=",
"img=",
"filename="

]

sqli_patterns = [

         "id=",
        "select=",
        "report=",
        "role=",
        "update=",
        "query=",
        "user=",
        "name=",
        "sort=",
        "where=",
        "search=",
        "params=",
        "process=",
        "row=",
        "view=",
        "table=",
        "from=",
        "sel=",
        "results=",
        "sleep=",
        "fetch=",
        "order=",
        "keyword=",
        "column=",
        "field=",
        "delete=",
        "string=",
        "number=",
        "filter="
]

lfi_patterns = [

        "file=",
        "document=",
        "folder=",
        "root=",
        "path=",
        "pg=",
        "style=",
        "pdf=",
        "template=",
        "php_path=",
        "doc=",
        "page=",
        "name=",
        "cat=",
        "dir=",
        "action=",
        "board=",
        "date=",
        "detail=",
        "download=",
        "prefix=",
        "include=",
        "inc=",
        "locate=",
        "show=",
        "site=",
        "type=",
        "view=",
        "content=",
        "layout=",
        "mod=",
        "conf=",
         "url="
         

]

rce_patterns = [
 
        "daemon=",
        "upload=",
        "dir=",
        "download=",
        "log=",
        "ip=",
        "cli=",
        "cmd=",
        "exec=",
        "command=",
        "execute=",
        "ping=",
        "query=",
        "jump=",
        "code=",
        "reg=",
        "do=",
        "func=",
        "arg=",
        "option=",
        "load=",
        "process=",
        "step=",
        "read=",
        "function",
        "req=",
        "feature=",
        "exe=",
        "module=",
        "payload=",
        "run=",
        "print="
]

idor_patterns = [

 "id=",
 "user=",
 "account=",
 "number=",
 "order=",
 "no=",
 "doc=",
 "key=",
 "email=",
 "group=",
 "profile=",
 "edit=",
 "report="
 
 ]

redirect_patterns =  [
"Lmage_url=",
"Open=",
"callback=",
"cgi-bin/redirect.cgi",
"cgi-bin/redirect.cgi?",
"checkout=",
"checkout_url=",
"continue=",
"data=",
"dest=",
"destination=",
"dir=",
"domain=",
"feed=",
"file=",
"file_name=",
"file_url=",
"folder=",
"folder_url=",
"forward=",
"from_url=",
"go=",
"goto=",
"host=",
"html=",
"image_url=",
"img_url=",
"load_file=",
"load_url=",
"login?to=",
"login_url=",
"logout=",
"navigation=",
"next=",
"next_page=",
"out=",
"page=",
"page_url=",
"path=",
"port=",
"redir=",
"redirect=",
"redirect_to=",
"redirect_uri=",
"redirect_url=",
"reference=",
"return=",
"returnTo=",
"return_path=",
"return_to=",
"return_url=",
"rt=",
"rurl=",
"show=",
"site=",
"target=",
"to=",
"uri=",
"url=",
"val=",
"validate=",
"view=",
"window="
]

def grep_xss():
    with open (FILE) as File:
        read_f = File.readlines()
    for each_read in read_f:
        for each_pattern in xss_patterns:
            if re.findall(each_pattern, each_read):
                print(each_read)
            
def grep_sqli():
    F = open(FILE, "r")
    read = F.readlines()
    
    for TAR in read:
        for pattern in sqli_patterns:
            if re.findall(pattern, TAR):
                print(TAR)

def grep_lfi():
    F = open(FILE, "r")
    read = F.readlines()

    for TAR in read:
        for pattern in lfi_patterns:
            if re.findall(pattern, TAR):
                print(TAR)

def grep_ssrf():
    F = open(FILE, "r")
    read = F.readlines()
    
    for TAR in read:
        for pattern in ssrf_patterns:
            if re.findall(pattern, TAR):
                print(TAR)
    
def grep_ssti():
    F = open(FILE, "r")
    read = F.readlines()

    for TAR in read:
        for pattern in ssti_patterns:
            if re.findall(pattern, TAR):
                print(TAR)

def grep_rce():
    F = open(FILE, "r")
    read = F.readlines()

    for TAR in read:
        for pattern in rce_patterns:
            if re.findall(pattern, TAR):
                print(TAR)

def grep_idor():
    F = open(FILE, "r")
    read = F.readlines()

    for TAR in read:
        for pattern in idor_patterns:
            if re.findall(pattern, TAR):
                print(TAR)

def grep_redirect():
    F = open(FILE, "r")
    read = F.readlines()

    for TAR in read:
        for pattern in redirect_patterns:
            if re.findall(pattern, TAR):
                print(TAR)