#!/usr/bin/env bash

if !(which pip3 >/dev/null 2>&1); then
    sudo apt-get install -y python3-pip
fi

if !(which coverage >/dev/null 2>&1); then
    python3 -m pip install -U coverage
fi

if !(which pipenv >/dev/null 2>&1); then
    python3 -m pip install -U pipenv
fi
