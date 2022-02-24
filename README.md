# mutation_testing_python

```
pyenv shell 3.9.1
python -m venv venv
source venv/bin/activate
pip install mutmut
pip install mut.py
pip install pytest
```

With MutMut

```
rm -rf .mutmut-cache && mutmut run --paths-to-mutate rover.py
mutmut html && open html/index.html

```

With Mut.Py (for some reason this doesn't seem to work anymore as it used to do 😡)

```
mut.py --target services.py --unit-test test/test_services.py -m --report-html output --runner pytest
```
