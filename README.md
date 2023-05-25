[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/bsingh23/nornir_crc_errors) [![Run in Cisco Cloud IDE](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-runable-icon.svg)](https://developer.cisco.com/devenv/?id=devenv-vscode-base&GITHUB_SOURCE_REPO=https://github.com/bsingh23/nornir_crc_errors) ![Python3.6](https://camo.githubusercontent.com/723530d950ad33dbac30bac267a80043cbc66f07605537e22cdf8eb3801452f7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e392d3337373641422e7376673f7374796c653d666c6174266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)


# Nornir Script: Find Interfaces with CRC Errors

This Nornir script collects CRC errors from Cisco network devices and writes the data to a CSV file and provide output on screen using RICH table.

Script will prompt the user to enter the minimum number of CRC errors.

The RICH table and CSV file contains the hostname, interface, and the number of CRC errors for each interface.

## Requirements

* Python 3.9+
* Nornir 3.x
* Nornir-scrapli plugin
* Nornir-utils plugin
* Scrapli library
* Genie library
* Devices configured for SSH access

Note: Code tested on Python 3.9.6

## Configuration

Configure your network devices in the `hosts.yaml` file using the following format:

``` yaml
host_name:
    hostname: ip_address
    platform: ios
    username: username
    password: password
    groups: (Optional)
        - <group_name>
```

You can also specify SSH port and any other connection options in the inventory file. Refer to the Nornir documentation for more information.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/bsingh23/nornir_crc_errors.git
   ```

2. Install the dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

3. Modify the `config_test.yaml` file in the `nornir` directory with your specific settings.

4. Run the script:

   ```bash
   python3 crc_error_v1.0.py
   ```

5. The script will create a CSV file in the same directory as the script with the following name format: `crcerror_<current_datetime>.csv`.

## Sample Output

| Hostname  | Interface            | CRC Error |
| --------- | -----------------    | --------- |
| switch1   | GigabitEthernet1/0/1 | 1214      |
| switch2   | GigabitEthernet0/0/1 | 57        |
| switch3   | GigabitEthernet2/0   | 150       |

## Notes

* The script uses the Genie library to parse the output of the `show interfaces` command. Make sure your network devices support the show interfaces command output in a format that can be parsed by Genie.

* Testing done on IOS and IOS-XE
