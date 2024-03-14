#This file is customized per home network. For the sake of simplicity only http,http and dns signatures are enabled as those are detected by NTOP engine

import yaml
import os

# Suricata configuration file path
suricata_config = "/etc/suricata/suricata.yaml"

# Suricata rules directory path
rules_file = "/var/lib/suricata/rules"

# Load the Suricata configuration file
with open(suricata_config, "r") as a:
    config = yaml.safe_load(a)

# Clear the existing default rule paths
config["default-rule-path"] = []

# connecting the HTTP, HTTPS, and DNS rules
enabled_rules = [
    os.path.join(rules_file, "app-layer-events.rules"),
    os.path.join(rules_file, "http-events.rules"),
    os.path.join(rules_file, "http-events-addon.rules"),
    os.path.join(rules_file, "dns-events.rules"),
]

for rule_file in enabled_rules:
    config["default-rule-path"].append(rule_file)

# Disable all other rules
config["rule-files"] = {}

# saving the config file
with open(suricata_config, "w") as a:
    yaml.dump(config, a)

print("Suricata HTTP, HTTPS, and DNS rules are enabled.”)
