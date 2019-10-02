# GTRI-exercise
Work on an exercise provided by GTRI
<br>
**Wed Oct  2 18:04:34 EDT 2019**

## Overview

The document SRE-coding-test.docx contains the exercise tasks.

This will be an exercise involving packaging the Apache Tika server `jar` file in a Docker container, running it locally, writing a script that uploads documents to the Tika server for text extraction, and an exercise that configures `iptables` to allow traffic to the Tika server from a given IP network during certain hours only.

## Format

My intention is to turn in the assignment as the Git repository where this `README` resides. 

There will be a simple Bash script that can be used to quickly build the Docker container and run it. It won't be very rigorous, however.

## Python

Python 3.7.4 (as of this writing) is installed in a virtualenv in ${PROJECT_ROOT}/envs. To activate:

    $ source ${PROJECT_ROOT}/envs/bin/activate

## Results

Here are the "answers" to the questions, identified in the code base:

 1. The Tika server `.jar` file can be found in the `docker` directory. The sign key (\*.asc) is in the project root directory. Here's how I verified the code:

    ```
    (envs) bick-ubtu3 ~/projects/GTRI (master)$ gpg --verify tika-server-1.22.jar.asc docker/tika-server-1.22.jar 
    gpg: Signature made Mon 29 Jul 2019 12:27:53 EDT
    gpg:                using RSA key 184454FAD8697760F3E00D2E4A51A45B944FFD51
    gpg: Good signature from "Tim Allison (ASF signing key) <tallison@apache.org>" [unknown]
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.
    Primary key fingerprint: 1844 54FA D869 7760 F3E0  0D2E 4A51 A45B 944F FD51
    (envs) bick-ubtu3 ~/projects/GTRI (master)$ 
    ```

 1. The `Dockerfile` used to create the environment is in the `docker` directory as well. There's also a `mk_docker.sh` script in `bin` that will run the commands to create the image and run it. The screenshots *mk_docker Running with Results.png* and *Tika Server Running.png* can be found in the `screenshots` directory. The first screenshot shows an empty docker setup and shows `mk_docker.sh` creating the container for the Tika server. Then it shows the server running with its "Hello World" result (`GET ... /tika`).
 1. The Python script in `bin` called `upload_docs.py` is a rudimentary script to send files to the Tika server to identify the type (`plain/text`, for example), then again to the server to extract the text. I didn't write tests for this, though that would certainly be something I would do normally. The screenshot *Running upload_docs_dot_py.png* illustrates two sample data files (included in the Git repo) demonstrating a `.txt` file and a `.pdf` file.
 1. The instructions for implementing the `iptables` solution are as follows:
    1. I found it necessary to first perform the following:
       ```
       $ sudo iptables -I INPUT -s docker0 -j DOCKER-USER
       ```
       I'm not sure whether that's advisable, but it was the only way I could get iptables to limit access to Docker. Perhaps this particular server setup only uses the INPUT rule, not the FORWARD rule, as seems to be the norm.
    1. Next I needed to add the following to `iptables`. This goes below the rule we're about to add next, and provides the default action for this IP network when it is not the time allowed.

       ```
       $ sudo iptables -I DOCKER-USER -s 192.168.0.0/16 -j DROP
       ```

    1. Finally, the following rule needs to be inserted to allow access at the needed times.
       It should be pointed out here that these times are assumed to be UTC, as that's what `iptables` works with.

       ```
       $ sudo iptables -I DOCKER-USER -s 192.168.0.0/16 -j RETURN -m time --timestart 07:00 --timestop 19:00
       ```
For the `iptables` exercise, I tested the operation using the address Docker had chosen for my container. The results of that testing can be found in the screenshot, *iptables Testing.png*. Here, you'll see the results of `iptables --list --verbose`, a few `date` commands to orient you to the time, and two `curl` attempts to the server. You can see when the one was prevented when not inside the time window.

I also provided the output to `iptables-save` as required in `data/iptables_restricted.dat`. The values here are from my testing, so the IP networks listed vary from the assigned value.

I didn't script this, as it seemed redundant to do so given the detailed instructions outlined above and the fact that there were only a few steps. 

# Summary

This was a challenging and educational exercise. I apprecate the opportunity to respond and I hope that my solutions are acceptable to you. 

Thank you for the opportunity.
