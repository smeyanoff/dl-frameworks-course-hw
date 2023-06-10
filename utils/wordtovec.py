from gensim.models import Word2Vec
from argparse import Namespace
import json
from pathlib import Path, PurePath
import os
import numpy as np


class WordToVec():

    def __init__(self, args: Namespace) -> None:

        self.prepared_dpath: Path     = args.prepared_dpath
        self.model_path:     Path     = args.model_path
        self.train:          bool     = args.train
        self.model:          Word2Vec = Word2Vec
        self.playbook:       Path     = args.playbook

    def train_model(self) -> None:

        with open(self.playbook) as file:
            params = json.load(file)
        with open(PurePath(self.prepared_dpath, "comments_tokinize.csv"), "rt") as text:
            corpus = eval(text.read())
        self.model = self.model(corpus, **params)
        self.model.save(os.path.join(self.model_path, "word2vec.wordvectors"))
    
    def load_model(self):

        if self.train:
            self.train_model()
        else:
            self.model.load(os.path.join(self.model_path, "word2vec.model"))
        return self

    def vectorize_sentence(self, sentence):

        words_vecs = [self.model.wv[word] for word in sentence if word in self.model.wv]
        if len(words_vecs) == 0:
            return np.zeros(300) # vector size in playbook TODO() 
        words_vecs = np.array(words_vecs)
        return words_vecs.mean(axis=0)
