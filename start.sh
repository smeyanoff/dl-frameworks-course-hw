#!/bin/bash

pip3 install poetry
poetry install
poetry run poe install_nltk_libs
