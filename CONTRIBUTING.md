# Contributing to freesms

## Run the tests

    python2 tests/test.py
    python3 tests/test.py

## Release a new version

Ensure you have up-to-date distributing tools:

    python3 -m pip install --upgrade pip setuptools wheel twine

Then:

1. Update the Changelog
2. Bump the version in `freesms/__init__.py`
3. Ensure the tests pass
4. Commit and tag
5. `rm -rf dist/*`
6. `python3 setup.py sdist bdist_wheel`
7. `twine check dist/*`
8. `twine upload dist/*`

[More info here](https://packaging.python.org/tutorials/packaging-projects/).
