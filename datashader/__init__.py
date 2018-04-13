from __future__ import absolute_import

import param
__version__ = str(param.version.Version(fpath=__file__, archive_commit="$Format:%h$",reponame="datashader"))

from .core import Canvas                                 # noqa (API import)
from .reductions import (count, any, sum, min, max,      # noqa (API import)
                         mean, std, var, count_cat, summary)
from .glyphs import Point                                # noqa (API import)
from .pipeline import Pipeline                           # noqa (API import)
from . import transfer_functions as tf                   # noqa (API import)

from . import pandas                         # noqa (build backend dispatch)
try:
    from . import dask                       # noqa (build backend dispatch)
except ImportError:
    pass


def test():
    """Run the datashader test suite."""
    import os
    try:
        import pytest
    except ImportError:
        import sys
        sys.stderr.write("You need to install py.test to run tests.\n\n")
        raise
    pytest.main([os.path.dirname(__file__)])


def examples(path='datashader-examples', verbose=False):
    """
    Copies the examples to the supplied path.
    """
    import os
    from shutil import copytree, ignore_patterns
    source = os.path.join(os.path.dirname(__file__),"examples")
    print("%s copy to %s" % (source, path))
    copytree(source, path, ignore=ignore_patterns('data', '.ipynb_checkpoints', '*.pyc', '*~'))
    print("%s copied to %s" % (source, path))
