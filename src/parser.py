def parse_log_file(file_path):
    logs = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split()

                if len(parts) != 3:
                    print(f"⚠ Skipping invalid log entry: {line}")
                    continue

                time, ip, status = parts

                log_entry = {
                    "time": time,
                    "ip": ip,
                    "status": status
                }

                logs.append(log_entry)

    except FileNotFoundError:
        print(f"❌ Error: Log file '{file_path}' not found.")
        raise SystemExit(1)

    except Exception as e:
        print(f"❌ Unexpected error while reading log file: {e}")
        raise SystemExit(1) 

    return logs