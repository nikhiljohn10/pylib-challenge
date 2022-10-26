#!/usr/bin/env bash

coverage run --source=file_db -m unittest discover test && coverage report -m
