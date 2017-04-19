#!/bin/bash

COUNTER=0
for x in ls */models/model_normalized.solid.binvox; do
	echo "$COUNTER: Copied $x to /media/jarvis/pubData/ShapeNetData/mug/solid_binvox/"$COUNTER"-model_normalized.solid.binvox"
	cp $x "/media/jarvis/pubData/ShapeNetData/mug/solid_binvox/"$COUNTER"-model_normalized.solid.binvox"
	let COUNTER=COUNTER+1
done

