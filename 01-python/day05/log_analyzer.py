# This program analyze the server log and sumarize count of info , warning and error 

info_count = 0
warning_count = 0
error_count = 0

with open("01-python\\day05\\server.log") as file:
    lines = file.readlines()
    for line in lines:
        if "INFO" in line:
            info_count = info_count + 1 
        if "ERROR" in line:
            error_count = error_count + 1 
        if "WARNING" in line:
            warning_count = warning_count + 1 

print("======================")
print("Log Summary")
print("======================")
print(f"INFO    : {info_count}")
print(f"WARNING : {warning_count}")
print(f"ERROR   : {error_count}")



