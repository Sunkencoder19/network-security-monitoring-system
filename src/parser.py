def parse_log_file(file_path):
    log = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            time, ip, status = line.split()

            log_entry = {
                "time": time,
                "ip": ip,
                "status": status
            }

            logs.append(log_entry)

    return logs
