import argparse
import sys

def main():
    argparser = argparse.ArgumentParser(
        description="Extract Simple-FASTA records"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    print(f"Now I need to process the records in {args.fasta}")

    printer = ''
    for line in (args.fasta):
        if '>' in line:
            name = line.replace('>',  '')
            name = name.strip()
            printer += name + '\t'
        else:
            printer += line

    sys.stdout.write(printer)


if __name__ == '__main__':
    main()
