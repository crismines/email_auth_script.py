import os
import smtplib
import logging
import openai
from datetime import datetime
import json

# Configure OpenAI API Key
openai.api_key = os.getenv('OPENAI_API_KEY')

def display_banner():
    print("\n" + "=" * 50)
    print("Email Authentication Checker & AI Filter Tool")
    print("=" * 50 + "\n")

def display_menu():
    menu = [
        "1. Run email check and filtering (default settings)",
        "2. Add or update email accounts",
        "3. Customize SMTP settings",
        "4. Test SMTP connection",
        "5. Update keywords for filtering",
        "6. View logs",
        "7. Exit"
    ]
    for item in menu:
        print(item)
    return input("\nEnter your choice (1-7): ").strip()

def load_config():
    config_file = "config.json"
    default_config = {
        "smtp_server": "mail.btinternet.com",
        "port": 587,
        "use_ssl": False,
        "keywords": ["amazon", "cryptocurrency", "wallet", "reward", "passport"],
    }

    if not os.path.isfile(config_file):
        with open(config_file, "w") as f:
            json.dump(default_config, f, indent=4)
        return default_config
    with open(config_file, "r") as f:
        return json.load(f)

def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

def check_email_login(email, password, server, port, use_ssl):
    try:
        if use_ssl:
            with smtplib.SMTP_SSL(server, port) as smtp:
                smtp.login(email, password)
        else:
            with smtplib.SMTP(server, port) as smtp:
                smtp.starttls()
                smtp.login(email, password)
        return True
    except smtplib.SMTPAuthenticationError:
        return False
    except Exception as e:
        logging.error("Error during SMTP connection: %s", e)
        return False

def run_email_check(config, input_file="logins.txt", output_folder="output"):
    os.makedirs(output_folder, exist_ok=True)
    log_file = os.path.join(output_folder, "script_log.txt")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
    )

    try:
        with open(input_file, "r") as f:
            accounts = [line.strip().split(",") for line in f if line.strip()]
        if not accounts:
            print("No email accounts found in logins.txt.")
            return

        print("\nChecking email accounts...")
        successful = []
        for email, password in accounts:
            if check_email_login(email, password, config["smtp_server"], config["port"], config["use_ssl"]):
                successful.append(f"{email},{password}")
                print(f"✔ {email}: Login successful")
            else:
                print(f"✘ {email}: Login failed")

        if successful:
            print("\nFiltering successful logins...")
            save_filtered_results(successful, config["keywords"], output_folder)
        else:
            print("No successful logins to filter.")
    except FileNotFoundError:
        print("Error: logins.txt file not found. Please add email accounts first.")

def save_filtered_results(logins, keywords, output_folder):
    filtered = {keyword: [] for keyword in keywords}
    for login in logins:
        for keyword in keywords:
            if keyword.lower() in login.lower():
                filtered[keyword].append(login)

    for keyword, results in filtered.items():
        if results:
            filename = os.path.join(output_folder, f"{keyword}_logins.txt")
            with open(filename, "w") as f:
                f.write("\n".join(results))
            print(f"Saved filtered results for '{keyword}' to {filename}")

def update_email_accounts():
    input_file = "logins.txt"
    print("\nUpdating email accounts in logins.txt...")
    if not os.path.isfile(input_file):
        open(input_file, "w").close()

    while True:
        action = input("\nChoose action: (A)dd, (R)emove, (Q)uit: ").strip().lower()
        if action == "a":
            email = input("Enter email address: ").strip()
            password = input("Enter password: ").strip()
            with open(input_file, "a") as f:
                f.write(f"{email},{password}\n")
            print(f"Added {email} to logins.txt.")
        elif action == "r":
            email_to_remove = input("Enter email address to remove: ").strip()
            with open(input_file, "r") as f:
                lines = f.readlines()
            with open(input_file, "w") as f:
                for line in lines:
                    if email_to_remove not in line:
                        f.write(line)
            print(f"Removed {email_to_remove} from logins.txt.")
        elif action == "q":
            print("Exiting email account update.")
            break
        else:
            print("Invalid choice. Try again.")

def main():
    display_banner()
    config = load_config()

    while True:
        choice = display_menu()
        if choice == "1":
            run_email_check(config)
        elif choice == "2":
            update_email_accounts()
        elif choice == "3":
            config["smtp_server"] = input("Enter SMTP server: ").strip() or config["smtp_server"]
            config["port"] = int(input("Enter port (default: 587): ").strip() or 587)
            config["use_ssl"] = input("Use SSL? (yes/no): ").strip().lower() == "yes"
            save_config(config)
            print("SMTP settings updated.")
        elif choice == "4":
            email = input("Enter email address: ").strip()
            password = input("Enter password: ").strip()
            if check_email_login(email, password, config["smtp_server"], config["port"], config["use_ssl"]):
                print("SMTP connection successful!")
            else:
                print("Failed to connect to SMTP server.")
        elif choice == "5":
            config["keywords"] = input("Enter keywords (comma-separated): ").strip().split(",")
            save_config(config)
            print("Keywords updated.")
        elif choice == "6":
            log_file = os.path.join("output", "script_log.txt")
            if os.path.isfile(log_file):
                with open(log_file, "r") as f:
                    print(f.read())
            else:
                print("No logs available.")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

