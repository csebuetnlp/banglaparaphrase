from ast import arg
import jsonlines
import json
import argparse

# filters from log files of PINC filtered json files.

if __name__ == '__main__':

    # Create the parser
    parser = argparse.ArgumentParser(
        description='path to jsonl log file, output source and output target and the lower and upper limit of BertScore')

    # Add the arguments
    parser.add_argument('--j',
                        metavar='jl',
                        type=str,
                        help='the path to the jsonl log file')

    parser.add_argument('--s',
                        metavar='t',
                        type=str,
                        help='the path to the generated source file')

    parser.add_argument('--t',
                        metavar='t',
                        type=str,
                        help='the path to the generated target file')

    parser.add_argument('--l',
                        metavar='l',
                        type=float,
                        help='the lower limit of bbertscore')

    parser.add_argument('--u',
                        metavar='u',
                        type=float,
                        help='the upper limit of bbertscore')

    # Execute the parse_args() method
    args = parser.parse_args()

    banglabert_path = args.j
    source_path = args.s
    target_path = args.t
    threshold1 = args.l
    threshold2 = args.u

    linecount = 0
    sourcebuffer = ""
    targetbuffer = ""
    banglabertfilteredcount = 0

    banglabertfile = jsonlines.open(banglabert_path)
    sourcefile = open(
        source_path, 'w', encoding='utf-8')
    targetfile = open(
        target_path, 'w', encoding='utf-8')

    for line in banglabertfile.iter():
        srcbangla = ""
        trgtbangla = ""
        maxbangla = -1
        for key, values in line.items():
            srcbangla = key
            for value in values:
                if value[1] > maxbangla:
                    trgtbangla = value[0]
                    maxbangla = value[1]

        if(maxbangla >= threshold1 and maxbangla < threshold2):
            sourcebuffer += srcbangla
            targetbuffer += trgtbangla
            banglabertfilteredcount += 1
            if(banglabertfilteredcount == 50000):
                sourcefile.write("%s" % sourcebuffer)
                targetfile.write("%s" % targetbuffer)
                sourcebuffer = ""
                targetbuffer = ""
                banglabertfilteredcount = 0

        linecount += 1
        if linecount % 50000 == 0:
            print(linecount)
    sourcefile.write("%s" % sourcebuffer)
    targetfile.write("%s" % targetbuffer)
    # closing all the files
    banglabertfile.close()
    sourcefile.close()
    targetfile.close
