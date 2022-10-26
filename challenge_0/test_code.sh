#!/usr/bin/env bash

coverage run --source=sample_lib -m unittest discover test && coverage report -m
