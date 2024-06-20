# 0x03. Log Parsing
This project includes a Python script that reads logs from standard input (stdin) line by line, parses the log entries, and computes various metrics such as total file size and the count of different HTTP status codes.

## Description
The script reads logs from stdin in a specific format, computes the total file size and counts the occurrences of specified HTTP status codes. It prints the computed metrics after every 10 lines and upon receiving a keyboard interrupt (CTRL + C).

## Usage
1. Save the script as `0-stats.py`.
2. Ensure the script has execute permissions:

```chmod +x 0-stats.py```

3. Run the script and pipe logs to it:

```./0-generator.py | ./0-stats.py```