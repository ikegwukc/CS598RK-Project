#!/bin/bash

# Simple Script to to convert test files to binvox

BINVOX=~/Downloads/binvox  # Change to path of binvox
DATA=/media/jarvis/pubData  # Expression should list out all model files
for filename in $DATA; do
	$BINVOX filename
$BINVOX decorated_cup_1.stl
$BINVOX decorated_cup_2.stl
$BINVOX mugV02_1x.stl
$BINVOX simple_cup.stl
$BINVOX test2.stl
$BINVOX test.stl