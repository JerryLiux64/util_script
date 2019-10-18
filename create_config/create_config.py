#!/usr/bin/python
import os
import argparse
import logging
import sys
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(__name__)

def create_config(filename, keyword, num):
    filename = os.path.abspath(filename)
    if not os.path.isfile(filename):
        logger.error("File %s not found." % filename)
        sys.exit()
    
    if num < 0:
        logger.error("Numgpu must greater than 0.")
        sys.exit()
    
    with open(filename, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    keyword = keyword+"="
    for idx, line in enumerate(lines):
        if keyword in line:
            lines[idx] = keyword + str(num)
    
    name, ext = os.path.splitext(filename)
    output = name + str(num) + ext
    with open(output, 'w') as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create config files with different gpu-idx.")
    parser.add_argument("filename", type = str, help="Config file that contains the base configurations.", metavar = "FILENAME")
    parser.add_argument("keyword", type = str, help="Keyword that the value will be change.", metavar = "KEYWORD")
    parser.add_argument("num", type = int, help = "Max number.", metavar = "NUMBER_OF_GPU")
    args, _ = parser.parse_known_args()

    for i in range(args.num):
        create_config(args.filename, args.keyword, i)