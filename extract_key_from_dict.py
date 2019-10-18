#!/usr/bin/env python
import json
import argparse
import operator
import os
import sys
def create_labels(file, output):
    if not os.path.isfile(os.path.abspath(file)):
        print("[Error] File not found: %s" % file)
        sys.exit(1)
    if not os.path.isdir(os.path.abspath(output)):
        print("[Error] Output dir is not a directory: %s" % output)
        sys.exit(1)

    try:
        with open(file, 'r') as f:
            classes = json.load(f)
    except json.decoder.JSONDecodeError as e:
        print("[Error] Input file is not in json format.")
        sys.exit(1)
    sorted_classes = sorted(classes.items(), key=operator.itemgetter(1))
    with open(os.path.join(output, "labels.txt"), 'w') as f:
        for item in sorted_classes:
            f.write(item[0] + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate classmap.json to label file.")
    parser.add_argument("jsonfile", help="Path to the classmap.json file")
    parser.add_argument("output", help= "Path to the output directory.")
    args, _ = parser.parse_known_args()

    create_labels(args.jsonfile, args.output)