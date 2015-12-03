#!/bin/sh

import os
import sys
import subprocess

subprocess.Popen(["xterm","-e",sys.argv[1]])

