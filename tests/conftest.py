"""
Shared test fixtures and configuration for data-pipeline test suite.

Refactored from duplicated fixture definitions across individual test
modules into a centralized conftest.py for maintainability.

Related issue: #6
"""

import os
import tempfile
from datetime import datetime