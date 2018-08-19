#!c:\users\ivang\desktop\python_course\app_8_financial_graph\mysite\virtual\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bokeh==0.13.0','console_scripts','bokeh'
__requires__ = 'bokeh==0.13.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bokeh==0.13.0', 'console_scripts', 'bokeh')()
    )
