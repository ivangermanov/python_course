#!c:\users\ivang\desktop\python_course\app_8_financial_graph\mysite\virtual\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'fix-yahoo-finance==0.0.22','console_scripts','sample'
__requires__ = 'fix-yahoo-finance==0.0.22'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('fix-yahoo-finance==0.0.22', 'console_scripts', 'sample')()
    )
