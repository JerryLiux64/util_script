Split dataset into ['train', 'test', 'val'].
    This script does two things, formatting dataset and splitting dataset.
    Format dataset takes a directory containing two folders,
    one contains all the images(in this script, the path is VOCdevkit/VOC2012/JPEGImages),
    one contains labels for the each class of images(in this script, the path is VOCdevkit/VOC2012/ImageSets/Main and the label file name end with _trainval.txt)
    The method formatdata copies and pastes the images to folders of classname according to _trainval.txt.

    Splitting dataset takes folders of classname and split each of them into ['train', 'val', 'test'] in the proportion of [0.7:0.2:0.1].
    The method splitdata takes a data_dir containing images of a class and split the images to ['train', 'val', 'test'] if the class is specified in the input list 'cls'.

    The split.json file specifies the way to split data.

