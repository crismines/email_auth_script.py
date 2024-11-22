Email Authentication Checker
This is a simple tool designed to help check email logins and filter them based on keywords. It can be used to validate whether an email and password combination works with a specified mail server, and filter accounts based on certain keywords.

Features:
Check if email login works with a mail server.
Filter successful logins by specific keywords.
Save filtered results in a file.
Installation
To use this script, you'll need to install Python and a few required libraries.

Step 1: Install Python
If you don’t have Python installed on your computer:

Download and install Python from here.
Ensure that Python is added to your system’s PATH during installation.
Step 2: Install Dependencies
Once you have Python installed, open your terminal (or Command Prompt on Windows) and navigate to the folder where you saved the script. Run the following command to install the required libraries:

bash
Copy code
pip install -r requirements.txt
This will install all the necessary packages to run the script, including dependencies like openai.

Setup
Before using the script, make sure you have a file called logins.txt in the same folder as the script. This file should contain the email and password combinations you want to check. Each line should have the format:

css
Copy code
email@example.com,password
Example:

graphql
Copy code
user1@example.com,password123
user2@example.com,securepassword456
Usage
Running the Script
To run the script, open your terminal (or Command Prompt) and run:

bash
Copy code
python emaillogin.py
Menu Options
Once the script starts, you’ll see a menu with options. Here's how each option works:

Run with default settings: Runs the script with default email checking settings.
Customize settings: Allows you to change the server address, port, and other settings.
Add email and password manually: Allows you to add an email and password pair directly in the script.
Test SMTP server connection: Test if the SMTP server is reachable.
View recent logs: View recent log entries of the script’s activity.
Clear output folder: Clears the files saved in the output/ folder.
Update default settings: Allows you to update the default server settings.
Change websites/keywords for filtering: Modify the list of keywords the script uses to filter results.
Exit: Exit the program.
Update input.txt file: Allows you to add/remove email-password pairs from the logins.txt file.
Running Example:
If you choose Option 1 (Run with default settings), the script will:

Check each email in your logins.txt file.
Try to log in using the provided credentials.
Filter successful logins based on pre-configured keywords.
Save the results in a file within the output/ folder.
Important Notes
Educational Use Only: This script is meant for educational purposes. Use it responsibly and ensure you have permission to check email credentials.
No Liability: The author is not responsible for any misuse, damage, or legal consequences that arise from using this script. By using this script, you agree to comply with all applicable laws.
License
This project is licensed under the MIT License - see the LICENSE file for details.

