# Curieo_Assignment
Code for assigment by Curieo AI

## Documentation
The file program.py consists of a class LogSystem.
LogSystem has two attributes : global_logs and logs_by_type
 global_logs is a list containing (timestamp,log_type,severity) tuples
 logs_by_type is a dictionary of log_type mapped to (timestamp,severity) tuples
LogSystem consists of 8 member functions, namely:
1.    add_log(self,timestamp,log_type,severity) -> adds the logs(tuples) of (timestamp,log_type,severity) to the global_logs list and to logs_by_type where (timestamp,severity) data is stored according to log_type  
2.    query_logs_for_log_type(log_type) -> finds all log entries specific to a given log_type and returns computed min,max and mean severity for those entries using a helper function
3.    query_logs_before_for_log_type(timestamp,log_type) -> finds all severities associated with log entries specific to a given log_type and before a given timestamp(excluding it) and returns computed min,max and mean severity for those entries using a helper function
4.    query_logs_after_for_log_type(timestamp,log_type) -> finds all severities associated with log entries specific to a given log_type and after a given timestamp(excluding it) and returns computed min,max and mean severity for those entries using a helper function
5.    query_logs_before(timestamp) -> finds all severities associated with log entries before a given timestamp(excluding it) and returns computed min,max and mean severity for those entries using a helper function
6.    query_logs_after(timestamp) -> finds all severities associated with log entries after a given timestamp(excluding it) and returns computed min,max and mean severity for those entries using a helper function
7.    calculate_stats(severities) -> helper function to calculate min,max and mean severity for a given list of severities.
8.    main() -> reads input from input.txt and based on the input type executes one of the first 6 functions and writes the output(for functions 2 to 6) to file output.txt

## Running Instructions
#### Build docker image
 ```sh
 cd your_project_directory
 docker build -t my-python-app .
 ```
#### Run the docker container
 ```sh
 docker run --name my-running-app my-python-app
 ```
