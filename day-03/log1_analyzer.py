import json
# this is blueprint og Loganalyzer class
class LogAnalyzer: # creating class

    """
        Class has 2 things
        data memebers (variables) & member funcations (functions)

    """
    def __init__(self,file_name,output_file):
        self.file_name = file_name
        self.output_file = output_file
        
    def read_logs(self):
        with open(self.file_name, "r") as file:
            return file.readlines()

    def analyze(self):
        log_count = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }
        lines=self.read_logs()

        for line in lines:
            if "INFO" in line:
                log_count["INFO"] += 1
            elif "WARNING" in line:
                log_count["WARNING"] += 1
            elif "ERROR" in line:
                log_count["ERROR"] += 1

        return log_count

    def write_json(self, counts):
        with open("output1.json","w+") as output_file:
            json.dump(counts,output_file)

# creating object
log=LogAnalyzer("app2.log", "output1.json")
log_1=LogAnalyzer("app2.log", "output2.json")
log_count=log_1.analyze()
log_1.write_json(log_count)
print("Log counts are:", log_count)

