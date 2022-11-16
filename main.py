import argparse
import lang


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--key', type=str, required=True)
	return parser.parse_args()


def main()->None:
	args = parse_args()
	lang.search(args.key)

if __name__ == "__main__":
	main()
