#codesnippet references
#Appending file line by line: https://www.geeksforgeeks.org/python-append-to-a-file/
#Reading file line by line: https://favtutor.com/blogs/read-file-line-by-line-python
#Error Handling: https://docs.python.org/3/tutorial/errors.html
#Reference for Timeit module: https://ioflood.com/blog/timeit-python/

import argparse
from porridge import Porridge

parser = argparse.ArgumentParser(description='Porridge password storage and verification')
subparsers = parser.add_subparsers(dest='operation')

storing = subparsers.add_parser('store', help='Store a password')
storing.add_argument('password', type=str, help='Password to store')
storing.add_argument('key', type=str, help='Key for the password')
storing.add_argument('secret', type=str, help='Secret for the password')

verify = subparsers.add_parser('verify', help='Verify a stored password')
verify.add_argument('password', type=str, help='Password to verify')
verify.add_argument('key', type=str, help='Key for the password')
verify.add_argument('secret', type=str, help='Secret for the password')
args = parser.parse_args()

op=args.operation
passwd=args.password
key=args.key
secret=args.secret
key_secret=key+":"+secret

if op == 'store':
    porridge = Porridge(key_secret)
    boiled_pass = porridge.boil(passwd)

    with open('pseudo_db.file', 'a') as f:
        f.write(boiled_pass+'\n')
    
    print('Success\r\n', end='', flush=True)

elif op == 'verify':
    porridge = Porridge(key_secret)

    with open('pseudo_db.file', 'r') as f:
        l = []
        for i in f:
            i = i.strip()
            l.append(i)
            
    for boiled_pass in l:
        try:
            verify = porridge.verify(passwd, boiled_pass)
        except: 
            verify = False
        if verify == True:
            break

    if verify == True:
        print('Verified\r\n', end='', flush=True)
    else:
        print('Not Found\r\n', end='', flush=True)