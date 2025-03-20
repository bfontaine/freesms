# Contributing to freesms

## Run the tests

    ./ci.sh

## Making a release

1. Update the CHANGELOG
2. Update the version in `pyproject.toml` and in `freesms/__init__.py`
3. Commit and tag with `v` followed by the version (e.g. `git tag v0.2.1`)
4. Push (without the tag) and wait for the [CI job][ci1] to succeed
5. Push the tag
6. Wait for the [CI job][ci2] to finish

[ci1]: https://github.com/bfontaine/freesms/actions/workflows/build.yml
[ci2]: https://github.com/bfontaine/freesms/actions/workflows/publish.yml
