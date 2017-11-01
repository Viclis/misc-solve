from util.args import ms_argparser
import re
def ms_main(args):
	parser = ms_argparser(description = 'hex transform.')
	parser.add_argument('file', help = 'file with hex string to process.')
	args = parser.parse_args(args)
	if args['file'] == None:
		print('No file specifed!')
		return
	fp = open(args['file'])
	fb = fp.read()
	fp.close()
	fb = re.sub(r'\s+', '', fb)
	print('original:', fb)
	# to int
	print('int:', int(fb, 16))
	# to ascii
	print('ascii:', end = ' ')
	if len(fb) % 2:
		print('cannot divide by 2.')
	else:
		print(''.join(chr(int(c, 16)) for c in re.findall(r'[0-9A-Fa-f]{2}', fb)))
