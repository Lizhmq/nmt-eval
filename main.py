from evaluation_utils import evaluate
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-out', type=str, required=True)
  parser.add_argument('-ref', type=str, required=True)
  args = parser.parse_args()
  out_file = args.out
  ref_file = args.ref
  print(evaluate(ref_file, out_file, 'bleu'))
  print(evaluate(ref_file, out_file, 'rouge'))
  
if __name__ == '__main__':
  main()