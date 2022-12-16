#!/bin/bash

export PYTHONIOENCODING=utf-8


if [ -f "$1" ]; then

	echo running whisper on file
	whisper "$1"
else
	echo no file found
fi
