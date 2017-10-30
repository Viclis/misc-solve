def ms_main(args):
	filename = args['file']
	fp = open(filename)
	content = fp.read()
	print(content)