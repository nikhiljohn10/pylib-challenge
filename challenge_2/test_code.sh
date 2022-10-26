#!/usr/bin/env bash

coverage run --source=yaml_parser -m unittest discover test && coverage report -m
