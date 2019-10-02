# GTRI-exercise
Work on an exercise provided by GTRI

## Overview

The document SRE-coding-test.docx contains the exercise tasks.

This will be an exercise involving packaging the Apache Tika server `jar` file in a Docker container, running it locally, writing a script that uploads documents to the Tika server for text extraction, and an unrelated exercise that configures `iptables` to allow traffic to the Tika server from a given IP network during certain hours only.

## Format

My intention is to turn in the assignment as the Git repository where this `README` resides. 

There will be a simple Bash script that can be used to quickly build the Docker container and run it. It won't be very rigorous, however.

## Python

Python 3.7.4 (as of this writing) is installed in a virtualenv in ${PROJECT_ROOT}/envs. To activate:

    $ source ${PROJECT_ROOT}/envs/bin/activate

The Python script supplied (`upload_docs.py`) will be written so that activation should not be necessary.
