While designing the solution to extract logs for a given date efficiently from a large log file (potentially up to 1TB in size), we explored multiple approaches:

1) Naïve Line-by-Line Search (Brute Force)

This approach involves reading the log file line by line and checking if the date exists in each line.
Drawback: This method is extremely slow for large files as it requires scanning every line sequentially, leading to O(n) complexity, where n is the number of lines.

2) Indexing-Based Search

This approach involves pre-processing the log file to create an index mapping each date to its file offsets.
Drawback: Indexing requires an additional pre-processing step and extra storage, which is inefficient for frequently updated log files.

3) Binary Search on Sorted Logs

If the log entries are chronologically sorted, we can use binary search to find the range of logs for a specific date.
Drawback: Binary search requires direct access to specific lines, which is complex in plain-text log files without fixed-length records.

4) Memory-Mapped File (Final Solution Chosen)

The final solution leverages memory-mapped file I/O (mmap), which allows us to treat the file as a byte array.
Using mmap.find(), we can quickly locate occurrences of the target date without loading the entire file into RAM.
This method significantly reduces I/O operations, making it highly efficient.

- Final Solution Summary
We chose the memory-mapped file approach because it offers a balance between speed and efficiency without requiring additional indexing. It allows for fast substring searches directly within the file while keeping memory usage minimal. The solution can handle very large log files efficiently by processing them in-place rather than loading them into memory. Additionally, it avoids the complexity of implementing a binary search on text-based logs.

- Steps to Run
Prerequisites
Ensure Python 3.x is installed on your system.
Have a log file (logs_2024.log) stored in the same directory as the script.
Install necessary dependencies (if any).
Running the Script
Save the script as extract_logs.py.
Open a terminal and navigate to the script's directory using:
VS code terminal - 
cd /path/to/your/script
Run the script with a specific date:
VS code terminal - 
python extract_logs.py YYYY-MM-DD
Example:
VS code terminal - 
python extract_logs.py 2024-01-31
Output logs will be saved in the output/ directory as output_YYYY-MM-DD.txt.

- Possible Improvements
1) Implement binary search on sorted logs for even faster range narrowing.
2) Use multithreading to parallelize searches for even larger log files.
3) Store an index file for previous searches to optimize future queries.
This solution ensures a fast, scalable, and memory-efficient way to extract logs from massive log files.






