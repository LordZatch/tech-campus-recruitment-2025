import os
import sys
import mmap
from datetime import datetime, date

class LogExtractor:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self.output_dir = 'output'
        os.makedirs(self.output_dir, exist_ok=True)
    
    def extract_logs_for_date(self, target_date):
        try:
            datetime.strptime(target_date, '%Y-%m-%d')
            output_file_path = os.path.join(self.output_dir, f'output_{target_date}.txt')
            
            with open(self.log_file_path, 'rb') as file:
                mm = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
                matching_logs = []
                current_pos = 0
                
                while True:
                    line_start = mm.find(target_date.encode(), current_pos)
                    if line_start == -1:
                        break
                    
                    line_end = mm.find(b'\n', line_start)
                    if line_end == -1:
                        line_end = len(mm)
                    
                    log_entry = mm[line_start:line_end].decode('utf-8')
                    matching_logs.append(log_entry)
                    current_pos = line_end + 1
                
                with open(output_file_path, 'w') as output_file:
                    output_file.write('\n'.join(matching_logs))
                
                print(f"Logs for {target_date} extracted to {output_file_path}")
                print(f"Total logs found: {len(matching_logs)}")
                mm.close()
        
        except ValueError:
            print(f"Invalid date format. Please use YYYY-MM-DD format.")
            sys.exit(1)
        except FileNotFoundError:
            print(f"Log file not found: {self.log_file_path}")
            sys.exit(1)
        except PermissionError:
            print(f"Permission denied accessing {self.log_file_path}")
            sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)
    
    target_date = sys.argv[1]
    extractor = LogExtractor('logs_2024.log')
    extractor.extract_logs_for_date(target_date)

if __name__ == "__main__":
    main()