import argparse
import sys

class ms_argparser(argparse.ArgumentParser):
	def __init__(self, description = '', prog = ''):
		if not prog:
			prog = sys.argv[0] + ' ' + sys.argv[1]
		super(ms_argparser, self).__init__(prog = prog, description = description)

	def parse_args(self, args):
		if args != None:
			return super(ms_argparser, self).parse_args(args).__dict__
		else:
			return super(ms_argparser, self).parse_args().__dict__
