#!/usr/bin/python
import os
import glob
import re
import shutil
import argparse
import logging
import sys
import json
from os.path import join as join_path
from random import shuffle
# from tqdm import tqdm # tqdm for progress bar


logging.basicConfig(level=logging.INFO,
					format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
					datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(__name__)

# def enum2(xs, st = 1):
# 	g = (x for x in xs)
# 	ls = []
# 	for i in range(0, len(xs), st):
# 		tmp = []
# 		for k in range(i, i+st):
# 			if k == len(xs):
# 				break
# 			tmp.append(next(g))
# 		ls.append(tmp)
# 	return ls

def formatdata(data_dir=''):
	if not data_dir:
		logger.error("data_dir not set.")

	source_dir = data_dir
	target_dir = join_path(data_dir, "formatted")


	suffix = '_trainval.txt'
	classes_dir = join_path(source_dir, "")
	images_dir = join_path(source_dir, "images")
	classes_files = glob.glob(classes_dir+"/*"+suffix)

	# for file in tqdm(classes_files):
	for file in classes_files:
		# get the filename and make output class folder
		classname = os.path.basename(file)
		if classname.endswith(suffix):
			classname = classname[:-len(suffix)]
			target_dir_path = join_path(target_dir, classname)
			if not os.path.exists(target_dir_path):
				os.makedirs(target_dir_path)
		else:
				continue

		with open(file) as f:
			content = f.readlines()

		for line in content:
			tokens = re.split('\s+', line)
			if tokens[1] == '1':
				# copy this image into target dir_path
				target_file_path = join_path(target_dir_path, tokens[0] + '.jpg')
				src_file_path = join_path(images_dir, tokens[0] + '.jpg')
				shutil.copyfile(src_file_path, target_file_path)

def splitdata(split_dir, cls, data_dir):
	SOURCE_DIR=join_path(data_dir, 'formatted')
	if not os.path.isdir(SOURCE_DIR):
		logger.error("%s is not a directory" % SOURCE_DIR)
		sys.exit(1)
	dir_list = next(os.walk(SOURCE_DIR))[1]
	# dir_split_list = enum2(dir_list,3)
	# for each dir, create a new dir in split
	for dir_i in dir_list:
		if dir_i not in cls:
			continue
		TARGET_DIR=os.path.join(data_dir, split_dir)
		newdir_train = os.path.join(TARGET_DIR, 'train', dir_i)
		newdir_val = os.path.join(TARGET_DIR, 'val', dir_i)
		newdir_test = os.path.join(TARGET_DIR, 'test', dir_i)

		if not os.path.exists(newdir_train):
				os.makedirs(newdir_train)
		if not os.path.exists(newdir_val):
				os.makedirs(newdir_val)
		if not os.path.exists(newdir_test):
				os.makedirs(newdir_test)

		img_list = glob.glob(os.path.join(SOURCE_DIR, dir_i, '*.jpg'))
		# shuffle data
		shuffle(img_list)

		for j in range(int(len(img_list)*0.7)):
				shutil.copy2(img_list[j], os.path.join(TARGET_DIR, 'train', dir_i))

		for j in range(int(len(img_list)*0.7), int(len(img_list)*0.8)):
				shutil.copy2(img_list[j], os.path.join(TARGET_DIR, 'val', dir_i))

		for j in range(int(len(img_list)*0.8), len(img_list)):
				shutil.copy2(img_list[j], os.path.join(TARGET_DIR, 'test', dir_i))
	
def parse_json(file, *args, **kwargs):
	with open(file, 'r') as f:
		try:
			content = json.load(f)
		except json.decoder.JSONDecodeError as e:
			logger.error("Cannot parser json file. Please check if the file is in json format. Error: %s" % e)
	return content

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Parse the split config .json file and split the dataset accordingly.")
	parser.add_argument("config", type=str, help="Path to the split config .json file.")
	parser.add_argument("-d", "--data", type=str, help="Path to the formatted data directory.", default="data")
	args, _ = parser.parse_known_args()
	file_path = os.path.abspath(args.config)
	if not os.path.isfile(file_path):
		logger.error("Cannot find config file \"%s\"" % file_path)
		sys.exit(1)

	data_dir = os.path.abspath(args.data)
	if not os.path.isdir(data_dir):
		logger.error("\"%s\" is not a directory" % data_dir)
		sys.exit(1)

	content = parse_json(file_path)

	logger.info("Formatting dataset...")
	formatdata(data_dir)
	logger.info("Splitting dataset...")
	# for key in tqdm(content.keys()):
	for key in content.keys():
		splitdata(key, content[key], data_dir)


