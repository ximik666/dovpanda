import inspect
import pathlib

import pandas

# Dirs
PANDAS_DIR = pathlib.Path(inspect.getsourcefile(pandas)).parent.absolute()
CURDIR = pathlib.Path(inspect.getsourcefile(inspect.currentframe())).parent.absolute()
z = inspect.getsourcefile(inspect.currentframe())
RESTRICTED_DIRS = [PANDAS_DIR, CURDIR]
# pandas mathods
READ_METHODS = [method for method in dir(pandas) if 'read' in method]
WRITE_TEXT_METHODS = ['DataFrame.to_csv', 'DataFrame.to_json']
DF_CREATION = READ_METHODS + ['DataFrame']
SERIES_CREATION = READ_METHODS + ['Series.__init__']
GET_ITEM = ['DataFrame.__getitem__', 'Series.__getitem__',
            'core.indexing._NDFrameIndexer.__getitem__', 'core.indexing._LocationIndexer.__getitem__']
TIME_COLUMNS = ['year', 'month', 'week', 'day', 'hour', 'minute', 'second', 'weekday', 'time']
# Translation dict
ndim_to_obj = {1: 'series', 2: 'df'}

#
CATEGORY_SHARE_THRESHOLD = 4

MAX_CSV_SIZE = 100000000  # Size in bytes, 100 MB

try:
    with (CURDIR / 'resource' / 'logo').open('r') as f:
        logo = f.read()
except FileNotFoundError:
    logo = None


# HTMLs
html_bug = '''
<h1>SADPANDA</h1><br>
I'm so sorry, but I crashed on <code>{hint}</code> with error <code>{e}</code><br>
But you can change that! Please
<a href="https://github.com/dovpanda-dev/dovpanda/issues/new?assignees=&labels=bug&template=bug_report.md&title=">
    Report a bug
</a>
'''
