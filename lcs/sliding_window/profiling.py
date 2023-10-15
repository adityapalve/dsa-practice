import psutil, time

def get_process_memory_info():
    process_info = []
    for process in psutil.process_iter(attrs=['pid', 'name', 'memory_info']):
        try:
            process_info.append({
                'pid': process.info['pid'],
                'name': process.info['name'],
                'memory_usage': process.info['memory_info'].rss  # Resident Set Size (RSS) in bytes
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return sorted(process_info, key=lambda x: x['memory_usage'], reverse=True)

def mBs(bytes: int) -> int:
    megabytes = bytes/ (1024*1024)
    return megabytes

def main():
    while True:
        # Get RAM usage information
        ram_info = psutil.virtual_memory()

        print(f"Total RAM: {mBs(ram_info.total)} bytes")
        print(f"Available RAM: {mBs(ram_info.available)} bytes")
        print(f"Used RAM: {mBs(ram_info.used)} bytes")
        print(f"RAM Usage Percentage: {mBs(ram_info.percent)}%")
        print("-" * 30)

        # Display top processes by RAM usage
        process_memory_info = get_process_memory_info()
        print("Top Processes by RAM Usage:")
        for process in process_memory_info[:10]:  # Display the top 10 processes
            print(f"PID: {process['pid']}, Name: {process['name']}, RAM Usage: {mBs(process['memory_usage'])} bytes")

        # You can customize the sleep interval (in seconds) as needed
        # For example, to update every 5 seconds: time.sleep(5)
        time.sleep(1)

if __name__ == "__main__":
    main()
