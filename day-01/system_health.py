import psutil

# get the threshold values  from input
cpu_threshold=float(input("Enter the CPU threeshold (%)"))
memory_threshold=float(input("Enter the Memory threeshold (%)"))
disk_threshold=float(input("Enter the Disk threshold (%)"))
# Fetch real-time system metrics
cpu_usuage=psutil.cpu_percent(interval=1)
memory_usuage=psutil.virtual_memory().percent
disk_usuage=psutil.disk_usage('/').percent

#function to chck status
def chk_status(actual,threshold):
    return "HIGH" if actual > threshold else "OK"
# Diplay results
print("\n===== System Health Report =====")
print(f"CPU Usuage :{cpu_usuage}% --> {chk_status(cpu_usuage,cpu_threshold)}")
print(f"Memory Usage : {memory_usuage}% --> {chk_status(memory_usuage, memory_threshold)}")
print(f"Disk Usage : {disk_usuage}% --> {chk_status(disk_usuage, disk_threshold)}")
