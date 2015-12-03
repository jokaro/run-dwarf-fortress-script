#!/bin/sh

import sys
import subprocess

subprocess.Popen(["xterm","-e",sys.argv[1]])

