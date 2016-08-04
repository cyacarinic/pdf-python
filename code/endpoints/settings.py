# -*- coding: utf-8 -*-

import	os

_BASE_DIR = os.path.dirname(os.path.dirname(__file__))
_PATH_URL = os.path.join(_BASE_DIR, "pdfs/from_url/")
_PATH_HTML = os.path.join(_BASE_DIR, "pdfs/from_html/")
_PATH_TEXT = os.path.join(_BASE_DIR, "pdfs/from_text/")
_PATH_TEMPLATE = os.path.join(_BASE_DIR, "pdfs/from_template/")
_FILE_TYPES = ['.pdf', '.xls']

_OFFSET_GET = 0
_LIMIT_GET = 10
