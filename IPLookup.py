import ipwhois
import csv
import codecs
from concurrent.futures import ThreadPoolExecutor, as_completed

def lookup_ip(ip_address):
    try:
        obj = ipwhois.IPWhois(ip_address)
        result = obj.lookup_rdap()
        
        isp_info = {
            'ip': ip_address,
            'isp': result['network']['name']
        }
        return isp_info
    except Exception as e:
        print(f"Error looking up IP {ip_address}: {e}")
        return {'ip': ip_address, 'isp': 'Lookup failed'}

def main():
    ip_file = 'ips.txt'
    ip_addresses = []

    try:
        with codecs.open(ip_file, 'r', 'utf-8-sig') as file:
            ip_addresses = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{ip_file}' not found.")
        return

    total_ips = len(ip_addresses)
    results = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_ip = {executor.submit(lookup_ip, ip): ip for ip in ip_addresses}

        for i, future in enumerate(as_completed(future_to_ip)):
            result = future.result()
            results.append(result)
            
            # Print progress
            percent_complete = (i + 1) / total_ips * 100
            print(f"Progress: {percent_complete:.2f}%", end='\r')

    with open('isp_report.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['ip', 'isp'])
        writer.writeheader()
        writer.writerows(results)

    print("\nISP report saved to isp_report.csv")

if __name__ == "__main__":
    main()
