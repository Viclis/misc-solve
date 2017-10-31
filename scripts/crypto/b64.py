from util.args import ms_argparser
from base64 import b64decode
from binascii import Error as BinasciiError

def ms_main(args):
	parser = ms_argparser('base64 decode.')
	parser.add_argument('-l', '--loop', help = 'base64 decode loop times.')
	parser.add_argument('file', help = 'file to decode.')
	args = parser.parse_args(args)
	fp = open(args['file'])
	fb = fp.read()
	try:
		if args['loop'] == None:
			print(b64decode(fb))
		else:
			for i in range(int(args['loop'])):
				fb = b64decode(fb)
				print(i + 1, fb)
	except BinasciiError:
		print('Cannot decode anymore.')
