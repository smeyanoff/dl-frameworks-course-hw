# dl-frameworks-course-hw

### Запуск 
```
sh start.sh # используя linux и poetry
```

После этого можно запускать `homework_1.ipynb

### Логирование экспериментов и моделей 

Логирование экспериментов осуществялется с помощью dvclive
Подбор гиперпараметров происходит с помощью optuna

Файлы сохраняются в локальную папку

### Progect tree
```
.
├── Ethos_Dataset_Binary.csv
├── README.md
├── data
│   ├── initial_data
│   │   ├── comments.csv
│   │   └── labels.csv
│   ├── intermediate_data
│   │   ├── comments_lower.csv
│   │   ├── comments_removed_stpwrds.csv
│   │   └── comments_removed_uni.csv
│   └── prepared_data
│       └── comments_tokinize.csv
├── data.dvc
├── dvclive-optuna
│   ├── dvc.yaml
│   ├── metrics.json
│   ├── params.yaml
│   └── report.html
├── dvclive-optuna.dvc
├── homework_1.ipynb
├── models
│   └── word2vec.wordvectors
├── models.dvc
├── playbooks
│   └── word2vec_params.json
├── poetry.lock
├── pyproject.toml
├── start.sh
├── support_scripts
│   └── install_nltk_libs.sh
└── utils
    ├── 
    │   ├── parsers.cpython-310.pyc
    │   └── wordtovec.cpython-310.pyc
    ├── parsers.py
    ├── preprocess_text.py
    └── wordtovec.py
```