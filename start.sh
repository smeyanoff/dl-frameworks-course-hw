#!/bin/bash

pip3 install poetry
poetry install
poetry run poe install_nltk_libs
poetry run poe prepare_data
