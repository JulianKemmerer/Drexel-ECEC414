#!/bin/sh

echo 'Branch mispredicts'
cat "$1"/stats.txt | grep 'system.cpu0.BPredUnit.condIncorrect';
cat "$1"/stats.txt | grep 'system.cpu1.BPredUnit.condIncorrect';
cat "$1"/stats.txt | grep 'system.cpu2.BPredUnit.condIncorrect';
cat "$1"/stats.txt | grep 'system.cpu3.BPredUnit.condIncorrect';
