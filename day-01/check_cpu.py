import psutil
# take CPU threshold from User
# find out current CPU usuage & if CPU usuage is more than threshold the send email

def get_cpu_threshold():
    user_cpu_threshold=int(input("Enter the CPU threshold"))
    current_cpu=psutil.cpu_percent(interval=1) # get current cpu threshold percent
    print("Print current CPU threshold:",current_cpu)
    if current_cpu>user_cpu_threshold:

        print("CPU Alert, Email sent...")
    else:
        print("CPU in safe state")
get_cpu_threshold()


    
