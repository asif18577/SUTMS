#!/bin/bash

# Path to your IoC file
IoC="/path_to/blacklisted_IP.txt"

# Delete existing rules
iptables -F

# Read blacklisted_IP.txt and add drop rules
while IFS= read -r line; do
    # Ignore comments and empty lines
    if [[ $line != \#* ]] && [ -n "$line" ]; then
        # Add rule to block traffic from the blacklisted_IP.txt
        iptables -A INPUT -s "$line" -j DROP
    fi
done < "$IoC"
