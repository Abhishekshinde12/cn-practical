import ipaddress

def subnet_calculator(ip_address, subnet_prefix_length):
    # Parse the input IP address to ensure it's a valid IP address
    ip = ipaddress.IPv4Address(ip_address)
    # Calculate the subnet mask based on the prefix length , strict = False means it will accept the input even if doesn't satisfy IP standards
    subnet_mask = ipaddress.IPv4Network(f'{ip}/{subnet_prefix_length}', strict=False).netmask
    # Calculate the network address and the range of usable IP addresses
    network_address = ipaddress.IPv4Network(f'{ip}/{subnet_mask}', strict=False).network_address
    # as network_address gives the address of network hence , network_address+1 gives the first host address
    first_host = network_address + 1
    # here we subtract 2 (as one IP corresponds to the broadcasting address and other IP represents the network itself and not the hosts in the network)
    last_host = network_address + (2 ** (32 - subnet_prefix_length)) - 2
    # used to broadcast data all the hosts in the network
    broadcast_address = network_address + (2 ** (32 - subnet_prefix_length)) - 1
    # Print the results
    print(f"IP Address: {ip}")
    print(f"Subnet Mask: {subnet_mask}")
    print(f"Network Address: {network_address}")
    print(f"Usable IP Range: {first_host} - {last_host}")
    print(f"Broadcast Address: {broadcast_address}")

def main_menu():
    while True:
        print("\nSubnetting Menu:")
        print("1. Calculate Subnet Mask and Network Info")
        print("2. Quit")
        choice = input("Enter your choice (1/2): ")
        if choice == '1':
            ip_address = input("Enter an IP address (e.g., 192.168.1.1): ")
            subnet_prefix_length = int(input("Enter the subnet prefix length (e.g., 24 for /24): "))
            if 0 <= subnet_prefix_length <= 32:
                subnet_calculator(ip_address, subnet_prefix_length)
            else:
                print("Invalid subnet prefix length. It should be between 0 and 32.")
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()