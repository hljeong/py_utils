from datetime import datetime, timedelta, timezone
from dateutil.parser import isoparse
from functools import cached_property, total_ordering
from itertools import pairwise
from math import floor


def _any_in(s, t):
    return any(e in t for e in s)


def pretty(duration_s, fmt=""):
    duration = floor(duration_s)
    seconds = duration % 60
    duration //= 60
    minutes = duration % 60
    duration //= 60
    hours = duration % 24
    duration //= 24
    days = duration % 30

    duration -= days
    years = duration // 365
    months = years * 12 + (duration % 365) // 30
