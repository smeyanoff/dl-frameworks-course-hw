#!/bin/bash

poetry run python -m nltk.downloader averaged_perceptron_tagger
poetry run python -m nltk.downloader punkt
poetry run python -m nltk.downloader stopwords
