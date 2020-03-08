import os
import argparse


def read_reffile(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
        lines = [' '.join(line.split(' ')) for line in lines]
        assert(len(lines) == 1)
        return lines[0]
def read_outfile(file):
    with open(file) as f:
        lines = [line.strip().split(' ') for line in f.readlines()]
        for i in range(1, len(lines)):
            lines[0] += lines[i]
        line = lines[0]
        return ' '.join(line)
    
def accumulate(dir, outfile, ref, size):
    lines = []
    for file in sorted(os.listdir(dir)):
        if ref:
            line = read_reffile(os.path.join(dir, file))
        else:
            line = read_outfile(os.path.join(dir, file))
        lines.append(line)
        if len(lines) % 1000 == 0:
            print(len(lines), '....')
    assert(len(lines) == size)
    with open(outfile, 'w') as f:
        for line in lines:
            print(line, file=f)

parser = argparse.ArgumentParser()
parser.add_argument('-out_dir', type=str, required=True)
parser.add_argument('-ref_dir', type=str, required=True)
parser.add_argument('-out_output', type=str, required=True)
parser.add_argument('-ref_output', type=str, required=True)
parser.add_argument('-size', type=int, required=True)

args = parser.parse_args()

out_dir = args.out_dir
ref_dir = args.ref_dir
out_output = args.out_output
ref_output = args.ref_output

accumulate(out_dir, out_output, ref=False, size=args.size)
accumulate(ref_dir, ref_output, ref=True, size=args.size)
