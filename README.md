<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/badge/language-Python-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/requires42.svg?maxAge=3600)](https://pypi.org/project/requires42/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/requires42.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/requires42.py/)

#### Installation
```bash
$ [sudo] pip install requires42
```

#### Pros
+   super fast. designed to generate a large number of requirements.txt files
+   [customizable](https://requires42.com/mapping/)

#### Scripts usage
command|`usage`
-|-
`requires42` |`usage: requires42 path`

#### Examples
```bash
$ export REQUIRES42_TOKEN=XXX # https://requires42.com/token/
$ cd path/to/repo
$ requires42 . > requirements.txt
```

python api:
```python
url = 'https://api.requires42.com/requires'
headers = {'Authorization': 'Token REQUIRES42_TOKEN'}

data = dict(imports=['django','requests','sqlalchemy'])
requests.post(url,headers=headers,data=data)

data = dict(files=[open('file.py').read()])
requests.post(url,headers=headers,data=data)
```

#### Links
+   [requires42.com](https://requires42.com/)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>