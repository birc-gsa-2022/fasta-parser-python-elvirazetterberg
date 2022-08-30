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
    newline = ''
    for line in (args.fasta):
        if '>' in line:
            name = line.replace('>',  '')
            name = name.strip()
            printer += newline + name + '\t'
            newline = '\n'
        else:
            printer += line.strip()

    sys.stdout.write(printer)


if __name__ == '__main__':
    main()
