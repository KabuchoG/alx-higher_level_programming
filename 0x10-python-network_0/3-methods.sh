#!/bin/bash
# Gets the list of allowed http methods from the server
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
