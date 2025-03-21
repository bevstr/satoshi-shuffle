#!/usr/bin/env python3
import sys
import re

exclude_patterns = [
    r"warnings\.warn",
    r"urllib3",
    r"NotOpenSSLWarning",
    r"LibreSSL",
    r"Serving Flask app",
    r"Debug mode",
]

for line in sys.stdin:
    # Skip excluded patterns
    if not any(re.search(pattern, line) for pattern in exclude_patterns):
        # Write the line as-is
        sys.stdout.write(line)
        sys.stdout.flush()