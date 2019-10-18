Split dataset into ['train', 'test', 'val'].
    This script does two things, formatting dataset and splitting dataset.
    Format dataset takes a directory containing two folders,
    one contains all the images (Ex:sample/images),
    one contains labels.txt for the each class of images(the label file name has to end with _trainval.txt, ex:sample/*_trainval.txt)
    The method formatdata copies and pastes the images to folders of classname according to _trainval.txt.

    Splitting dataset takes folders of classname and split each of them into ['train', 'val', 'test'] in the proportion of [0.7:0.2:0.1].
    The method splitdata takes a data_dir containing images of a class and split the images to ['train', 'val', 'test'] if the class is specified in the input list 'cls'.

    The split.json file specifies the way to split data.


Usage:
./splitdata.py split.json -d sample/
