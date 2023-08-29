python -m doctest -v $(grep -r -l '>>>' osa*/*.py)
pylint $(git ls-files '*.py')
mypy .