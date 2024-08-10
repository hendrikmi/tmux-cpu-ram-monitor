import psutil


def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return f"{cpu_usage}%"


def get_mem_usage():
    mem = psutil.virtual_memory()
    mem_usage = mem.percent
    return f"{mem_usage}%"


def main():
    cpu = get_cpu_usage()
    mem = get_mem_usage()
    print(f"CPU: {cpu} | MEM: {mem}")


if __name__ == "__main__":
    main()
