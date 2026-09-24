# Timeout config

`config.timeout` maps an empty string to the documented default of 30 seconds.
An explicit integer string selects that integer; other input raises `ValueError`.
The parser and its checks live in this directory. Run `python -B -m unittest -v`.
