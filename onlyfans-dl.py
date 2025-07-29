#!/usr/bin/env python3

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

print(urllib3)
