from base64 import b64decode
from binascii import Error as BinasciiError

def ms_main(args):
	fp = open(args['file'])
	fb = fp.read()
	try:
		if args['args'] == None:
			print(b64decode(fb))
		else:
			for i in range(int(args['args'][0])):
				fb = b64decode(fb)
				print(i + 1, fb)
	except BinasciiError:
		print('Cannot b64decode any more.')
