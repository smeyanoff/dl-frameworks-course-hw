from abc import ABC, abstractmethod
from argparse import Namespace
import os
import re
from pathlib import PurePath
import nltk
from nltk.corpus import stopwords
from parsers import preprocess_text_parse


class TextPreprocessor(ABC):

    def __init__(self, args: Namespace) -> None:
        self.dpath = args.dpath
        self.prepared_dpath = args.prepared_dpath
        self.intermediate_dpath = args.intermediate_dpath

    def _text_normalize(self) -> None:

        with open(PurePath(self.dpath, "comments.csv"), "r") as comments_f:
            commments = comments_f.readlines()
            with open(PurePath(self.intermediate_dpath, 
                               "comments_lower.csv"), 
                      "w") as comments_lower_f:
                for comment in commments:
                    comments_lower_f.write(comment.lower()+"\n")
    
    def _removing_unicode(self) -> None:

        regex = r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?"

        with open(PurePath(self.intermediate_dpath, 
                           "comments_lower.csv"), 
                  "r") as comments_f:
            commments = comments_f.readlines()
            with open(PurePath(self.intermediate_dpath, 
                               "comments_removed_uni.csv"), 
                      "w") as comments_rem_f:
                for comment in commments:
                    comments_rem_f.write(re.sub(regex, "", comment)+"\n")

    def _removing_stopwords(self) -> None:

        stop = stopwords.words("english")

        with open(PurePath(self.intermediate_dpath, 
                           "comments_removed_uni.csv"), 
                  "r") as comments_f:
            commments = comments_f.readlines()
            with open(PurePath(self.intermediate_dpath, 
                               "comments_removed_stpwrds.csv"), 
                      "w") as comments_rem_f:
                for comment in commments:
                    comments_rem_f.write(
                        " ".join([word for word in comment.split() if word not in (stop)])
                        +"\n"
                    )
    
    def _word_tokinize(self) -> None:

        tokens_list = []
        with open(PurePath(self.intermediate_dpath, 
                            "comments_removed_stpwrds.csv"), 
                    "r") as comments_f:
            commments = comments_f.readlines()
            with open(PurePath(self.prepared_dpath, 
                                "comments_tokinize.csv"), 
                        "w") as comments_rem_f:
                for comment in commments:
                    tokens = nltk.word_tokenize(comment)
                    pos_tags = nltk.pos_tag(tokens)
                    tokens_list.append([str(tag) for tag in pos_tags])
                comments_rem_f.write(
                str(tokens_list)
                )

    def data_pipeline(self) -> None:
        self._text_normalize()
        self._removing_unicode()
        self._removing_stopwords()
        self._word_tokinize()

if __name__=="__main__":
    preprocessor = TextPreprocessor(preprocess_text_parse())
    preprocessor.data_pipeline()
