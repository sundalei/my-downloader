#!/usr/bin/env python3

"""
OnlyFans Downloader - A tool to download content from OnlyFans accounts

Configuration variables:
- user_id: User ID for authentication
- user_agent: HTTP user agent string
- x_bc: X-BC header value
- session_cookie: Session cookie for authentication
- verbosity: Logging verbosity level (0-4)
- download_dir: Directory to save downloaded content
- skip_accounts: List of accounts to skip downloading from
"""

import os
import sys
import json
import shutil
import pathlib
import requests
import urllib3
import hashlib
from datetime import datetime, timedelta

urllib3.disable_warnings()

# Configuration

# Session variables
user_id = ""
user_agent = ""
x_bc = ""
session_cookie = ""

# 0 = do not print file names or api calls
# 1 = print file names only when max_age is set
# 2 = always print file names
# 3 = print api calls
# 4 = print skipped files that already exist
verbosity = 2
# Download Directory. Use CMD if null
download_dir = ""
# List of accounts to skip
skip_accounts = []

print(urllib3)
print(os)
print(sys)
