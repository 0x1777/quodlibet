# -*- coding: utf-8 -*-

import os

HOME    = os.path.expanduser("~")
DIR     = os.path.join(HOME, ".quodlibet")
CONTROL = os.path.join(DIR,  "control")
CONFIG  = os.path.join(DIR,  "config")
CURRENT = os.path.join(DIR,  "current")
LIBRARY = os.path.join(DIR,  "songs")
ACCELS  = os.path.join(DIR,  "accels")

CREDITS = ["Joe Wreschnig",
           "Michael Urman",
           "Iñigo Serna",
           "Bastian Kleineidam",
           "Michal Nowikowski",

           "Anders Carlsson",
           "Sun Microsystems, Inc.",
           "Lee Willis",
           "Jan Arne Petersen",
           "Gustavo J. A. M. Carneiro"]
