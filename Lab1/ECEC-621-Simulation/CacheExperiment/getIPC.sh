#!/bin/sh

echo 'IPC'
cat "$1"/stats.txt | grep 'system.cpu0.ipc_total';
cat "$1"/stats.txt | grep 'system.cpu1.ipc_total';
cat "$1"/stats.txt | grep 'system.cpu2.ipc_total';
cat "$1"/stats.txt | grep 'system.cpu3.ipc_total';
