# Artifact
SUTMS - Unified Threat Management System for Home Networks

## Features

- Antibot - Automated Firewall response
- Efficient IDS - integrated according to flow/applications.
- Anomaly detection 

## Installation

- Install Ubuntu 22.04 LTS available on https://ubuntu.com/download/desktop/thank-you?version=22.04.4&architecture=amd64
- Install Suricata 6.0.0 ( Available on https://suricata.io/download/)
- Install NTOP packages ( Available on https://www.ntop.org/get-started/download/)
- Install webmin package
- Install iptables via Ubuntu terminal.

## Usage
One the required softwares are installed as listed in installation instructions, perform the following tasks.
SUTMS - Firewall Module with dynamic IoC feeds
- create manual rules (sample recommended fw rules included in "iptables.rules file for testing.
- setup stix/taxii feed like (https://www.anomali.com/resources/staxx).
- Run the python program (sutms_conversion.py) attached, it will download and convert the IoC into a file name called "blacklisted_IP"
- Flush the iptables rules and run the script "ioc.sh".
- Automate the above tasks by adding the entries listed in "sutms_cronjobs" file
- Verify the rules by command line interface or using webmin. 
  
SUTMS - IDS Module according to application detection
- Download the latest SUTMS rules by executing "sudo suricata-update".
- Learn the protocols in use via NTOP engine.
- Run the python script (sutms_suricate.py) to only enable the relevant signatures. (please select the protocols according to your environment)
- Automate the above tasks by adding the entries listed in "sutms_cronjobs" file.
- Review the logs and make sure for neccessary hits

SUTMS - Anomaly detection
- NTOP can be used to detect anomalies, certain use cases are include in "ntop_lua" file.


