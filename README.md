# File Permission Checker

## Overview
The File Permission Checker is a Python tool that retrieves and reports file or directory permissions on POSIX systems using the `os` and `stat` modules. It compares permissions against a configurable threshold to warn about overly permissive settings.

## Author
Rick Hayes

## License
MIT

## Version
2.73

## Requirements
- Python 3.x
- POSIX-compatible system (e.g., Linux, macOS)
- No additional libraries beyond the Python standard library

## Usage
Run the script with the following arguments:

```bash
python3 file_permission_checker.py --path <PATH> [--config <CONFIG_FILE>]
