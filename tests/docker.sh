#!/usr/bin/env bash

#
# Script to run all tests in a docker image.
#
# Arguments:
#   1. The docker image, defaults to "python:3.8".
#   2. Interactive flag, when "1", a bash is opened instead of running the tests and exit, defaults
#      to "".
#

action() {
    local this_file="$( [ ! -z "$ZSH_VERSION" ] && echo "${(%):-%x}" || echo "${BASH_SOURCE[0]}" )"
    local this_dir="$( cd "$( dirname "$this_file" )" && pwd )"
    local repo_dir="$( cd "$( dirname "$this_dir" )" && pwd )"

    local docker_image="${1:-python:3.8}"
    local interactive="$2"

    if [ "$interactive" = "1" ]; then
        docker run --rm -ti -v "$repo_dir":/root/order -w /root/order "$docker_image" \
            bash
    else
        docker run --rm -t -v "$repo_dir":/root/order -w /root/order "$docker_image" \
            bash -c "pip install -r requirements_test.txt && python -m unittest tests"
    fi
}
action "$@"
