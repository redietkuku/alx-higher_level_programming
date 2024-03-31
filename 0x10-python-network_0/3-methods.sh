#!/bin/bash
# Display all HTTP methods that can be accepted by a server.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
