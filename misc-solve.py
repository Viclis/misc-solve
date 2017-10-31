import argparse
import importlib

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Scripts for CTF misc problems.')
	parser.add_argument('-s', '--script', required = True, help = 'Select a script.')
	parser.add_argument('file', help = 'Path of the file you want to process.')
	parser.add_argument('-a', '--args', nargs = argparse.REMAINDER)
	args = parser.parse_args().__dict__
	if args['script'] != None:
		script = importlib.import_module('scripts.' + args['script'])
		script.ms_main(args)