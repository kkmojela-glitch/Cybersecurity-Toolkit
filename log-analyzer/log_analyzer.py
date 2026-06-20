log_file = input("Enter log file name: ")

try:
    with open(log_file, "r") as file:
        lines = file.readlines()

        failed_logins = 0

        for line in lines:
            if "failed" in line.lower():
                failed_logins += 1

        print(f"Failed login attempts found: {failed_logins}")

except FileNotFoundError:
    print("Log file not found.")
