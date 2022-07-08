from eth_account import Account
import secrets
import threading
import argparse

parser = argparse.ArgumentParser(description='Generate beautiful ETH wallet @mintertale (discord @m1ntertale#8888)')
parser.add_argument('-s', '--start',default='', help='Address start with (0x***...)')
parser.add_argument('-e','--end', default='', help='Address end with ( 0x..........***)')
parser.add_argument('-t', default=int(10), help='Threads, default: 10')

args = parser.parse_args()

notFound = True

def func():
	global notFound
	while notFound:
		private_key = "0x" + secrets.token_hex(32)
		acct = Account.from_key(private_key)
		strt = "0x"+ args.start
		if str(strt) in str(acct.address) and str(acct.address).endswith(args.end):
			print(f"FOUND! ADDR: {acct.address} | KEY (DO NOT SHARE THIS): {private_key} ")
			notFound = False


if __name__ == '__main__':
	for i in range(int(args.t)):
		print("Start thread #%s" % str(i))
		t = threading.Thread(target=func)
		t.start()
		
