#!/bin/sh

echo 'ICache hits'
cat "$1"/stats.txt | grep 'system.cpu0.icache.overall_hits::total';
cat "$1"/stats.txt | grep 'system.cpu1.icache.overall_hits::total';
cat "$1"/stats.txt | grep 'system.cpu2.icache.overall_hits::total';
cat "$1"/stats.txt | grep 'system.cpu3.icache.overall_hits::total';
echo 'DCache hits'
cat "$1"/stats.txt | grep 'system.cpu0.dcache.overall_hits::total';
cat "$1"/stats.txt | grep 'system.cpu1.dcache.overall_hits::total';
cat "$1"/stats.txt | grep 'system.cpu2.dcache.overall_hits::total';
cat "$1"/stats.txt | grep 'system.cpu3.dcache.overall_hits::total';
echo 'ICache misses'
cat "$1"/stats.txt | grep 'system.cpu0.icache.overall_misses::total';
cat "$1"/stats.txt | grep 'system.cpu1.icache.overall_misses::total';
cat "$1"/stats.txt | grep 'system.cpu2.icache.overall_misses::total';
cat "$1"/stats.txt | grep 'system.cpu3.icache.overall_misses::total';
echo 'DCache misses'
cat "$1"/stats.txt | grep 'system.cpu0.dcache.overall_misses::total';
cat "$1"/stats.txt | grep 'system.cpu1.dcache.overall_misses::total';
cat "$1"/stats.txt | grep 'system.cpu2.dcache.overall_misses::total';
cat "$1"/stats.txt | grep 'system.cpu3.dcache.overall_misses::total';