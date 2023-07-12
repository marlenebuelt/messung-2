#!/bin/bash

# Set the time interval (in seconds) to track the process
time_interval=1

# Set the process name
process_name="python3.7 03_svm.py"

# Set the output file path
output_file="processes_svm.log"

# Start the loop
while true; do
    # Get the current timestamp
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")

    # Check if the process is running
    if pgrep -f "$process_name" > /dev/null; then
        # Process is running, append the timestamp and process information to the file
        echo "$timestamp $(ps -C "$process_name" -o pid,ppid,%cpu,%mem,cmd --no-headers)" >> "$output_file"
    else
        # Process is not running, append the timestamp and a message to the file
        echo "$timestamp $process_name is not running" >> "$output_file"
    fi

    # Wait for the specified time interval
    sleep "$time_interval"
done
