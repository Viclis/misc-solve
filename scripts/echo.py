from util.args import ms_argparser

def ms_main(args):
	parser = ms_argparser('Echo file content, ascii file only.')
	parser.add_argument('file', help = 'File to echo.')
	args = parser.parse_args(args)
	filename = args['file']
	fp = open(filename)
	content = fp.read()
	print(content)
