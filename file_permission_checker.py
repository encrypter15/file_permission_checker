#!/usr/bin/env python3
# File Permission Checker
# Author: Rick Hayes
# License: MIT
# Version: 2.73
# README: Works on POSIX systems. Checks file permissions.

import os
import stat
import argparse
import logging
import json

def setup_logging():
    """Configure logging to file."""
    logging.basicConfig(filename='file_permission_checker.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file: str) -> dict:
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Config loading failed: {e}")
        return {"warn_mode": "777"}

def get_permissions(path: str) -> str:
    """Get file permissions in octal format."""
    try:
        st = os.stat(path)
        mode = oct(st.st_mode & 0o777)[-3:]
        return mode
    except (FileNotFoundError, OSError) as e:
        logging.error(f"Permission check failed for {path}: {e}")
        return ""

def main():
    """Main function to parse args and check permissions."""
    parser = argparse.ArgumentParser(description="File Permission Checker")
    parser.add_argument("--path", required=True, help="File or directory path")
    parser.add_argument("--config", default="config.json", help="Config file path")
    args = parser.parse_args()

    setup_logging()
    config = load_config(args.config)

    logging.info(f"Checking permissions for {args.path}")
    perms = get_permissions(args.path)
    if perms:
        logging.info(f"Permissions: {perms}")
        print(f"Permissions for {args.path}: {perms}")
        if int(perms, 8) > int(config["warn_mode"], 8):
            logging.warning(f"Permissions {perms} exceed warning threshold {config['warn_mode']}")
            print(f"Warning: Permissions are more permissive than {config['warn_mode']}")
    else:
        print(f"Error: Could not check permissions for {args.path}")

if __name__ == "__main__":
    main()
