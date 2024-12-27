import socket

# Banniere ASCII
def print_banner():
    banner = r"""
    ╔═════════════════════════════════════════════════╗
    ║    _____                 _ _ _____      _       ║
    ║   /  ___|               | | |_   _|    | |      ║
    ║   \ `--. _ __ ___   __ _| | | | | _ __ | | __   ║
    ║    `--. \ '_ ` _ \ / _` | | | | || '_ \| |/ /   ║
    ║   /\__/ / | | | | | (_| | | |_| || | | |   <    ║
    ║   \____/|_| |_| |_|\__,_|_|_|\___/_| |_|_|\_\   ║
    ║                                                 ║
    ║           - The Small Storm of Print -          ║
    ║                 by 7h30th3r0n3                  ║
    ╚═════════════════════════════════════════════════╝
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
        print(f"Done sending to {ip}")
    except socket.timeout:
        print(f"Connection to {ip} timed out")
    except Exception as e:
        print(f"An error occurred with {ip}: {e}")

# Main function to send data to printers from a list
def main():
    # Display the banner
    print_banner()

    # Ask for the IPs file
    ips_file = input("Enter the file path containing the list of printer IPs: ")

    # Read the list of IPs
    try:
        with open(ips_file, 'r', encoding='utf-8', errors='ignore') as f:
            ips = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading IPs file: {e}")
        return

    if not ips:
        print("The IPs file is empty or invalid.")
        return

    # Ask for the file to send
    file = input("Enter the file path to send to the printers: ")

    # Read the content to send
    try:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Confirm the action
    confirm = input(f"Are you sure you want to send the content of '{file}' to all printers in '{ips_file}'? (y/n): ")
    if confirm.lower() != 'y':
        print("Operation cancelled.")
        return

    # Send data to all specified printers
    for ip in ips:
        send_to_printer(ip, content)

    print("Operation completed.")

if __name__ == "__main__":
    main()
