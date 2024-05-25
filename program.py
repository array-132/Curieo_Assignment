from bisect import bisect_left,bisect_right
from collections import defaultdict
import re

class LogSystem:
    def __init__(self) -> None:
        self.global_logs = []
        self.logs_by_type = defaultdict(list)

    def add_log(self,timestamp,log_type,severity):
        self.global_logs.append((timestamp,log_type,severity))
        self.logs_by_type[log_type].append((timestamp,severity))

    def query_logs_for_log_type(self,log_type):
        logs = self.logs_by_type[log_type]
        if not logs:
            return 0.0,0.0,0.0
        severities = [log[1] for log in logs]
        return self.calculate_stats(severities)

    def query_logs_before_for_log_type(self,timestamp,log_type):
        logs = self.logs_by_type[log_type]
        # print(logs)
        index = bisect_right(logs,(timestamp,-float('inf'))) -1
        # print(index)
        if index <0:
            return 0.0,0.0,0.0
        severities = [log[1] for log in logs[:index+1]]
        return self.calculate_stats(severities)
    
    def query_logs_after_for_log_type(self,timestamp,log_type):
        logs = self.logs_by_type[log_type]
        index = bisect_left(logs,(timestamp,-float('inf')))
        # if index == len(logs):
        #     return 0.0,0.0,0.0
        severities = [log[1] for log in logs[index:]]
        return self.calculate_stats(severities)
    
    def query_logs_before(self,timestamp):
        # print(self.global_logs)
        index = bisect_right(self.global_logs,(timestamp,"",-float('inf')))-1
        # print(index)
        if index < 0:
            return 0.0,0.0,0.0
        severities = [log[2] for log in self.global_logs[:index+1]]
        return self.calculate_stats(severities)
    
    def query_logs_after(self,timestamp):
        index = bisect_left(self.global_logs,(timestamp,"",-float('inf')))
        # if index == len(self.global_logs):
        #     return 0.0,0.0,0.0
        severities = [log[2] for log in self.global_logs[index:]]
        return self.calculate_stats(severities)
    
    def calculate_stats(self,severities):
        if not severities:
            return 0.0,0.0,0.0
        min_severity = min(severities)
        max_severity = max(severities)
        sum_severity = sum(severities)
        count = len(severities)
        mean_severity = sum_severity/count if count > 0 else 0.0
        return min_severity,max_severity,mean_severity
    
    def main(self):
        # print(" I have entered main")
        try:
         with open('output.txt','w') as outfile:
          with open('input.txt','r') as file:
            # print("Input.txt has been read")
            for line in file:
                # print(f"Line {line} is being read")
                entry = line.strip()
                entry = re.split(r'[ ;]',entry)
                entry = [e for e in entry if e]
                # print(entry)
                if entry[0] == '1':
                    self.add_log(int(entry[1]),entry[2],float(entry[3]))
                    continue
                elif entry[0] == '2':
                    min_severity,max_severity,mean_severity = self.query_logs_for_log_type(entry[1])
                    outfile.write(f"Min: {min_severity}, Max: {max_severity}, Mean: {mean_severity}\n")
                elif entry[0] == '3' and entry[1].lower() == 'before' :
                    min_severity,max_severity,mean_severity = self.query_logs_before(int(entry[2]))
                    outfile.write(f"Min: {min_severity}, Max: {max_severity}, Mean: {mean_severity}\n")
                elif entry[0] == '3' and entry[1].lower() == 'after' :
                    min_severity,max_severity,mean_severity = self.query_logs_after(int(entry[2]))
                    outfile.write(f"Min: {min_severity}, Max: {max_severity}, Mean: {mean_severity}\n")
                elif entry[0] == '4' and entry[1].lower() == 'before':
                    min_severity,max_severity,mean_severity = self.query_logs_before_for_log_type(int(entry[3]),entry[2])
                    outfile.write(f"Min: {min_severity}, Max: {max_severity}, Mean: {mean_severity}\n")                
                elif entry[0] == '4' and entry[1].lower() == 'after':
                    min_severity,max_severity,mean_severity = self.query_logs_after_for_log_type(int(entry[3]),entry[2])    
                    outfile.write(f"Min: {min_severity}, Max: {max_severity}, Mean: {mean_severity}\n")
          file.close()
         outfile.close()
        except FileNotFoundError:
            print("The file was not found")
        except IOError:
            print("An error occured while reading the file")   

if __name__=="__main__":                
    l = LogSystem()
    l.main()