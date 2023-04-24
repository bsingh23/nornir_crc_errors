from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_command
from datetime import datetime
import os
import csv

nr = InitNornir(config_file="/net_ops/nornir/config_test.yaml")

# Define the header row for the CSV file
header = ["Hostname", "Interface", "CRC Error"]

# Get the current date and time as a string to use in the file name
time_now = datetime.now().strftime("%Y%m%d_%H%M%S")

# Create the file name using the current date and time
filename = (f"crcerror_{time_now}.csv")

# Check if the file already exists; if not, create the file and write the header row
if not os.path.isfile(filename):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

def crc_error(task):
    response = task.run(task=send_command, command="show interfaces")

    task.host["facts"] = response.scrapli_response.genie_parse_output()
    
    hostname = task.host.name

    # Filter interfaces that have CRC errors (List comprehension)
    interfaces = [intf for intf in task.host["facts"] if task.host["facts"][intf]['counters']['in_crc_errors'] >= 10]

    # Write the data to the CSV file
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for intf in interfaces:
            in_crc_errors = task.host['facts'][intf]['counters']['in_crc_errors']
            writer.writerow([hostname, intf, in_crc_errors])

my_results = nr.run(task=crc_error)
