import argparse
import sys


def main():
    argparser = argparse.ArgumentParser(
        description="Extract sub-sequences from a Simple-FASTA file"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    argparser.add_argument(
        "coords",
        nargs="?",
        type=argparse.FileType('r'),
        default=sys.stdin
    )
    args = argparser.parse_args()

    print(f"Now I need to process the records in {args.fasta}")
    print(f"and the coordinates in {args.coords}")

    # if args.coords == '' or args.coords == '-':
    #     sys.stdin()

    namedict = {}
    for line in (args.fasta):
        if '>' in line:
            name = line.replace('>',  '')
            name = name.strip()
            namedict[name] = ''
        else:
            namedict[name] += line.strip()
    
    printer = ''
    newline = '\n'
    for line in (args.coords):
        lst = line.split()
        name = lst[0].replace('>',  '')
        name = name.strip()
        if name in namedict:
            a = int(lst[1])-1
            b = int(lst[2])-1
            splice = namedict[name][a:b]
            printer += newline + splice
            newline = '\n'
    
    sys.stdout.write(printer)


if __name__ == '__main__':
    main()
