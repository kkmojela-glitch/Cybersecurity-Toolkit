print("=== SECURITY LOG ANALYZER ===")

file_name = input("Enter log file name: ")

try:
    with open(file_name, "r") as file:
        logs = file.readlines()

    error_count = 0
    failed_logins = 0
    suspicious_activity = 0

    for line in logs:
        lower_line = line.lower()

        if "error" in lower_line:
            error_count += 1

        if "failed" in lower_line or "invalid" in lower_line:
            failed_logins += 1

        if "attack" in lower_line or "unauthorized" in lower_line:
            suspicious_activity += 1

    print("\n--- SECURITY REPORT ---")
    print(f"Total log lines: {len(logs)}")
    print(f"Errors detected: {error_count}")
    print(f"Failed login attempts: {failed_logins}")
    print(f"Suspicious activity flags: {suspicious_activity}")

except FileNotFoundError:
    print("File not found. Please check the filename.")
