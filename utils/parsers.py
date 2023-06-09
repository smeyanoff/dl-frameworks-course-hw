from argparse import ArgumentParser
from os import PathLike


def parser():
    parser = ArgumentParser()

    subpursers = parser.add_subparsers()

    return subpursers

def preprocess_text_parse():
    preprocess_text_parser = parser().add_parser("preprocess")

    preprocess_text_parser.add_argument("--dpath", default="./data/initial_data")
    preprocess_text_parser.add_argument("--prepared_dpath", default="./data/prepared_data")
    preprocess_text_parser.add_argument("--intermediate_dpath", default="./data/intermediate_data")

    return preprocess_text_parser.parse_args()

# def train_wordtovec_parse_args():
#     parser = ArgumentParser()

#     parser.add_argument("--")
