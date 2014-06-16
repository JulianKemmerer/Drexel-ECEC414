#!/bin/sh

echo 'CPU cycles'
cat "$1"/stats.txt | grep 'system.cpu0.numCycles';
cat "$1"/stats.txt | grep 'system.cpu1.numCycles';
cat "$1"/stats.txt | grep 'system.cpu2.numCycles';
cat "$1"/stats.txt | grep 'system.cpu3.numCycles';
