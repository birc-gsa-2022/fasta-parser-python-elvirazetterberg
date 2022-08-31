import argparse

def main():
    argparser = argparse.ArgumentParser(
        description="Extract Simple-FASTA records"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    # print(f"Now I need to process the records in {args.fasta}")

    printerlist = []
    i = -1
    for line in (args.fasta):
        if '>' in line:
            i += 1
            name = line.replace('>',  '')
            name = name.strip()
            printerlist.append(name + '\t')
        else:
            printerlist[i] += line

    # f = open('test-data/genome-1.fa-fasta-recs-expected', 'r')
    # reflines = f.readlines()

    # for i,ref in enumerate(reflines):
    #     if printerlist[i] == ref:
    #         print("match")
    #     else:
    #         print("mismatch")
    #         print(printerlist[i]+'end')
    #         print(ref+'end')
        

    for f in printerlist:
        print(f, end = '')

    # print()

if __name__ == '__main__':
    main()
