# FreeSMS Changelog

## Unreleased

- Add type hints
- Raise an exception if no password is provided
- Remove `FreeResponse.__nonzero__` (Python 2 compatibility)

## v0.3.0 (2025/03/20)

- Drop support for Python 3.3, 3.4, 3.5, 3.6, 3.7
- Add official support for Python 3.10, 3.11, 3.12, 3.13

## v0.2.1 (2025/03/20)

- `FreeResponse` now have a reference to the underlying `requests.Response` object
- `FreeResponse#success` now returns the result of `requests.Response#ok`
- `FreeClient` now accepts a `password=` argument by default. The previous wording `passwd=` is still supported

## v0.2.0 (2021/05/17)

- Fix license string in `setup.py` (#7 by @cdce8p)
- Drop official support for Python 2.x. It probably works, but it’s not tested anymore.
- Don’t hide insecure request warning when not using ``verify=True`` (this reverts the change in v0.1.2).
  It’s problematic to hide a warning _by default_, and the caller should be able to do it
  [by themselves](https://stackoverflow.com/a/28002687/735926).

## v0.1.2 (2017/11/03)

- Fix an insecure request warning when not using ``verify=True``. Contributed by @nalepae

## v0.1.1 (2016/10/28)

- Fix an encoding error when installing with Python 3.x and a non utf-8 locale

## v0.1.0 (2015/01/19)

- initial release
