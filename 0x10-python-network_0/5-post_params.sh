#!/bin/bash
# sends a POST requst to a URL
curl -s -X POST -H "email: test@gmail.com&subject: I will always be here for PLD" "${1}"