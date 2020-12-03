<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/requires42.svg?maxAge=3600)](https://pypi.org/project/requires42/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/requires42.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/requires42.py/actions)

### Installation
```bash
$ [sudo] pip install requires42
```

#### Examples
```bash
$ export REQUIRES42_TOKEN=XXX # https://requires42.com/token/
$ requires42 . > requirements.txt
$ requires42 . | awk -F '=' '{print $1}' > requirements.txt # without versions
```

curl api:
```bash
set -- curl -s -X POST -H "Authorization: Token $REQUIRES42_TOKEN"
files="$(find "$PWD" -type f -not -path "$PWD/tests/*" -name "*.py" -type f)"
[[ -n "$files" ]] && while IFS= read f; do
    set -- "$@" -F "file[]=@$f"
done <<< "$files"
set -- "$@" https://api.requires42.com/requires
"$@" . > requirements.txt
```

python api:
```python
import requests

url = 'https://api.requires42.com/requires'
headers = {'Authorization': 'Token REQUIRES42_TOKEN'}

files = {
    'package/__init__.py': open('package/__init__.py','rb'),
    'package/base.py': open('package/base.py','rb')
}
r = requests.post(url,headers=headers,files=files)
open('requirements.txt','w').write(r.text)
```

#### Links
+   [requires42.com](https://requires42.com/)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
