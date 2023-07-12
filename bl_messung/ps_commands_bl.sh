#!/bin/bash

# Set the time interval (in seconds) to track the processes
time_interval=1

# Set the output file path
output_file="processes.log"

# Clear the output file
> "$output_file"

# Start the loop
while true; do
    # Get the current timestamp
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")

    # Run the ps command to get the process details
    ps_output=$(ps aux)

    # Use awk to calculate the totals for CPU and memory utilization
    cpu_total=$(echo "$ps_output" | awk 'NR>1 {sum+=$3} END {printf "%.2f", sum}')
    mem_total=$(echo "$ps_output" | awk 'NR>1 {sum+=$4} END {printf "%.2f", sum}')

    # Append the timestamp and totals to the file
    echo "$timestamp", "$cpu_total%", "$mem_total%">> "$output_file"
    #echo "CPU Utilization Total: $cpu_total%" >> "$output_file"
    #echo "Memory Utilization Total: $mem_total%" >> "$output_file"
    #echo >> "$output_file"  # Add an empty line as separator

#echo "$timestamp $(ps -C "$process_name" -o pid,ppid,%cpu,%mem,cmd --no-headers)" >> "$output_file"

    # Wait for the specified time interval
    sleep "$time_interval"
done
