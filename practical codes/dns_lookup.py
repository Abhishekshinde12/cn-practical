#Write a program for DNS lookup. Given an IP address input, it should return URL and vice versa.

import socket

# socket.herror - raise error when 1)The provided hostname or IP address cannot be resolved to a valid IP address. 2) There is a problem with DNS resolution, such as DNS server unavailability or misconfiguration. 3) The provided IP address or hostname format is invalid

def ip_to_url(ip_address):
    try:
        url = socket.gethostbyaddr(ip_address)
        return url[0]
    except socket.herror:
        return "Could not resolve the IP address to a URL."

# socket.gaierror - raise error when 1)The provided hostname or IP address does not exist. 2)There is a problem with DNS resolution, such as DNS server unavailability or misconfiguration. 3)The provided service or port information is invalid. 4) A hostname or service name could not be resolved

def url_to_ip(url):
    try:
        ip = socket.gethostbyname(url)
        return ip
    except socket.gaierror:
        return "Could not resolve the URL to an IP Address."

while True:

    print("DNS Lookup Menu:")
    print("1. IP to URL")
    print("2. URL to IP") 
    print("3. Exit")

    choice = input("Enter your Choice: ")
    
    if choice=='1':
        ip_address = input("Enter the IP Address:")
        url = ip_to_url(ip_address)
        print(f"The URL for {ip_address} is: {url}")
    
    elif choice =='2':
        url = input("Enter the URL: ")
        ip_address = url_to_ip(url)
        print(f"The IP address for {url} is: {ip_address}")
    
    elif choice=='3':
        print("Exit")
        break
    
    else:
        print("Invalid Choice.Please select a valid option.")   
        