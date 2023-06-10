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

def wordtovec_parse_args():
    word2vec_parser = parser().add_parser("word2vec_parser")

    word2vec_parser.add_argument("--prepared_dpath", default="./data/prepared_data")
    word2vec_parser.add_argument("--model_path", default="./models")
    word2vec_parser.add_argument("--train", type=bool, default=False)
    word2vec_parser.add_argument("--playbook", default="./playbooks/word2vec_params.json")

    return word2vec_parser
