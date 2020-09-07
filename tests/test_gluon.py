#!/usr/bin/env python3
import sys
from pynet import *


def test_reconfigure():
    a = Node()

    start()

    a.dbg(a.succeed("gluon-reconfigure"))

    finish()
