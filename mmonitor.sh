#!/bin/bash
    while true; do
        echo "Time: $(date)"
        echo "Latency:" 
	m h1 ping -c 10 h2
	echo "Throughput:"
	m h1 iperf3 -s &
	sleep 1
	m h2 iperf3 -c h1 -t 10
	m h1 killall iperf3
	echo "Packet Loss:"
	m h1 ping -c 10 h2 | grep "packet loss"
	echo "-----------" 
	sleep 60
    done
