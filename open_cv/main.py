import argparse
from detect import Detector


def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-i", "--image", default=None,
                           help="path to Image File ")
    arg_parse.add_argument("-o", "--output", type=str,
                           help="path to optional output image file")
    args = vars(arg_parse.parse_args())

    return args


if __name__ == "__main__":
    detector = Detector()
    args = argsParser()
    detector.humanDetector(args)
