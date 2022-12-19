#!/bin/bash
# Post Json.i.
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "${1}"
