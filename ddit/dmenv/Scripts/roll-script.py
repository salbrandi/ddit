#!c:\users\owner\desktop\ddit\ddit\dmenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'DDIT','console_scripts','roll'
__requires__ = 'DDIT'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('DDIT', 'console_scripts', 'roll')()
    )
