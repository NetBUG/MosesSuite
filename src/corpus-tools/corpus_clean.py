#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    corpus clean

    :copyright: Copyright 2012 by Leo Jiang <leo.jiang.dev@gmail.com>
    :license: LGPL, see LICENSE for details.
"""

import sys

if __name__ == '__main__':
    from corpustools.cleantool import main
    sys.exit(main(sys.argv))
