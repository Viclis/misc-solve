import argparse
import importlib

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Scripts for CTF misc problems.')
	parser.add_argument('script', help = 'Select a script.')
	parser.add_argument('args', nargs = argparse.REMAINDER, help='Args for script.')
	args = parser.parse_args().__dict__
	script = importlib.import_module('scripts.' + args['script'])
	script.ms_main(args['args'].copy())
