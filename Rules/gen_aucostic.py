#coding: utf-8

import sys
import re
import os
import argparse
from string import punctuation
import itertools
import north, central, south

news_onset = []
def diff(list1, list2):
    return list(set(list1).symmetric_difference(set(list2)))