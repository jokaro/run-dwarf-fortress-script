#!/usr/bin/env python
"""Use this script to launch dfhack with PyLNP without getting "x-x: unexpected operator".
This script will not lock PyLNP and allow you to launch utlities like Dwarf Therapist.

Add this script to the df_linux folder.
In PyLNP open File -> Configure terminal... and add the following in the text box.

python run.py $

:copyright: (c) 2015 by Joakim Karlsson.
:license: MIT, see LICENSE for more details.
"""

import sys
import subprocess

subprocess.Popen(["xterm","-e",sys.argv[1]])

