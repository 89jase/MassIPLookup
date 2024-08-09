# IP WHOIS Lookup Script

This Python script is designed to check the WHOIS information for a large list of IP addresses. It retrieves the Internet Service Provider (ISP) name associated with each IP address and saves the results to a CSV file.

## Features

- **Multithreading**: The script uses multithreading to perform WHOIS lookups concurrently, speeding up the processing of large IP address lists.
- **Error Handling**: The script handles exceptions during WHOIS lookups, ensuring that the script continues to run even if some IP addresses fail to be processed.
- **Progress Indicator**: The script provides a progress indicator to show the percentage of completion during execution.
- **Output to CSV**: The results of the WHOIS lookups are saved to a CSV file, `isp_report.csv`, with columns for the IP address and the corresponding ISP name.

## Requirements

- Python 3.x
- `ipwhois` library

You can install the required library using pip:

```bash
pip install ipwhois
```

## Usage

1. **Prepare IP Address List**: Create a text file named `ips.txt` in the same directory as the script. This file should contain a list of IP addresses, one per line.

2. **Run the Script**: Execute the script using Python:

   ```bash
   python whois_lookup.py
   ```

3. **View Results**: After the script completes, the results will be saved to `isp_report.csv` in the same directory.

## Script Overview

- `lookup_ip(ip_address)`: This function performs the WHOIS lookup for a given IP address using the `ipwhois` library and returns a dictionary with the IP address and ISP name.
  
- `main()`: This is the main function that reads the list of IP addresses from `ips.txt`, performs the WHOIS lookups concurrently, and saves the results to `isp_report.csv`.

## Error Handling

- If the `ips.txt` file is not found, the script will print an error message and terminate.
- If a WHOIS lookup fails for any IP address, the script will print an error message for that specific IP, and the result for that IP will be recorded as "Lookup failed".

## License

This project is licensed under the MIT License.

## Contact

For any issues or questions, please contact [Your Name] at [Your Email].

---

Feel free to customize this `README.md` to include more specific details or contact information as needed.
