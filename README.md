<div align="center">
  
```
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
```
> **Warning**: This tool is just a POC, use it ethicaly, responsibly and only on devices you own or have explicit permission to test.

</div>
  
## Overview
This project, **The Storm of Print**, is a POC tool designed for ethical purposes. It demonstrates the potential vulnerabilities of network printers exposed on the internet, particularly on port `9100`, which is commonly used for print jobs.

This POC tool utilizes the Shodan API to identify exposed printers, allowing researchers to send arbitrary data to these devices. This can serve as a powerful demonstration of the risks associated with leaving such devices unsecured.

> The useable script for pentesting is SmallInk that can target ip address based on a txt file.

---

## Features
- **Shodan Integration**: Queries Shodan to locate vulnerable printers.
- **Content Injection**: Sends arbitrary data to printers via port `9100`.
- **Country Filtering**: Filters results by country using ISO codes.
- **File-Based Targeting**: Reads target IPs from a file for controlled testing.
- **Ethical Warning**: Informs users about the dangers of exposing printers online.

---

## Setup
### Prerequisites
- Python 3.x
- Shodan API key

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/7h30th3r0n3/StormInk.git
   cd StormInk
   ```
2. Install required libraries:
   ```bash
   pip install shodan
   ```
3. Obtain a Shodan API key from [Shodan](https://account.shodan.io/).

4. Add your Shodan API key to the script:
   ```python
   shodan_api_key = "your_shodan_api_key"
   ```

---

## Usage

### Main Script
Run the primary script to discover printers and send data:
```bash
python storm_of_print.py
```

#### Workflow
1. **Query Shodan**: Filter by country (optional) and search for printers using port `9100`.
2. **Save Targets**: Save discovered IPs to a file.
3. **Send Data**: Send the contents of a specified file to the target printers.

### Small Storm Script
Alternatively, use the smaller script for file-based targeting:
```bash
python small_storm.py
```
This script requires:
- A file containing printer IPs.
- A file with the content to send.

---

## Ethical Usage
This tool includes a warning message to inform printer owners of their vulnerabilities:

```plaintext
WARNING: Your printer is exposed on port 9100, a port often used for direct print jobs.
Attackers could intercept print jobs, inject malicious content, or even access your entire network.
Act now to secure your printer by restricting network access, enabling firewalls, and updating firmware.
```

**Disclaimer**: This project is intended for ethical security research and education only. Unauthorized usage is strictly prohibited.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author
**7h30th3r0n3** - Ethical hacker and cybersecurity enthusiast.
