import os
import argparse
import numpy

def process(infile, outout, outref):
	data = numpy.load(infile)
	with open(outref, 'w') as f:
		for dd in data:
			for d in dd:
				print(d[0], file=f)
	with open(outout, 'w') as f:
		for dd in data:
			for d in dd:
				print(d[1], file=f)
	
		

parser = argparse.ArgumentParser()
parser.add_argument('-res_file', type=str, required=True)
parser.add_argument('-out_output', type=str, required=True)
parser.add_argument('-ref_output', type=str, required=True)

args = parser.parse_args()

process(args.res_file, args.out_output, args.ref_output)
