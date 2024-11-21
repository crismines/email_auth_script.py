User Guide for Email Authentication Script
This guide will walk you through how to use the Email Authentication Script to check the login credentials of multiple email accounts. The script supports filtering logins based on keywords and allows you to easily update the list of accounts in logins.txt.

Prerequisites:
Python 3: Ensure you have Python 3.x installed.
SMTP Server Details: The script uses SMTP servers to authenticate the email credentials. By default, it checks BT Internet but you can customize it to use other email providers like Gmail, Yahoo, etc.
Emails List: You must create a file called logins.txt containing email addresses and passwords, separated by a comma (e.g., email@example.com,password123).

Setup:
Install Python and Dependencies: Ensure Python is installed on your system. No additional libraries are required as the script uses built-in Python libraries.

Prepare logins.txt: Create a file named logins.txt and enter email/password pairs, each on a new line. Example:

graphql
Copy code
email1@example.com,password123
email2@example.com,password456

Run the Script: Save the script to your local machine and execute it using Python:
bash
Copy code
python email_auth_script.py
Main Features:
Menu Options: After running the script, a menu will be displayed with various options. You can choose from:
Run with default settings: Check email logins with the current settings.
Customize settings: Change the SMTP server, port, SSL option, and keywords for filtering.
Add email and password manually: Add new email and password pairs to logins.txt.
Test SMTP server connection: Test the connection for a specific email account.
View recent logs: View the latest log of successful and failed email authentications.
Clear output folder: Delete all previous results stored in the output folder.
Update default settings: Change SMTP server settings.
Change websites/keywords for filtering: Modify the list of keywords used to filter successful logins.
Exit: Quit the script.
Detailed Guide for Menu Options:
Option 1 - Run with default settings:

This will run the script using the default configuration and will check the email credentials in logins.txt. It will save the results based on matching keywords (e.g., amazon, paypal) to the output folder.
Option 2 - Customize settings:

You can change the SMTP server, port, SSL usage, and the list of keywords used to filter the email logins. These settings are saved for future runs.
Option 3 - Add email and password manually:

If you want to add more email addresses and passwords, you can manually input them here. The script will automatically append these entries to logins.txt.
Option 4 - Test SMTP server connection:

If you are unsure whether your email provider's server works with the script, you can test a single account's login credentials here. It will attempt to log in to the provided email using the configured SMTP server.
Option 5 - View recent logs:

This will display the latest authentication logs, showing details of both successful and failed logins.
Option 6 - Clear output folder:

Deletes all files in the output folder where previous results are stored. This is useful if you want to start fresh with new results.
Option 7 - Update default settings:

Allows you to update the SMTP server, port, and SSL settings. Changes are saved in config.txt.
Option 8 - Change websites/keywords for filtering:

Modify the list of keywords used for filtering successful logins. For example, you might want to focus only on emails containing the word “paypal.”
Option 9 - Exit:

Exits the script and returns to the command line.

Working with logins.txt:

Adding Entries: You can add new email/password pairs by selecting the option to add manually. Alternatively, you can edit logins.txt directly.
Removing Entries: The script allows you to remove specific email addresses by ID.
Format: Each line in the file must be in the format: email@example.com,password123.

Example Use Case:
Run the script:
bash
Copy code
python email_auth_script.py

Choose Option 1 to run with default settings.
The script will check each email and password from logins.txt against the specified SMTP server.
It will save the successful logins to the output folder based on the defined keywords (e.g., amazon, paypal).
Optionally, you can add/remove accounts or modify settings through the menu.

Troubleshooting:
Invalid email format: Ensure the emails in logins.txt are properly formatted (e.g., email@example.com).
SMTP Authentication Error: If the credentials are incorrect, the script will log a failure.
No logs: Check if logins.txt contains any entries and that the SMTP server details are correct.

Important Notes:
The script uses SMTP authentication to check the login credentials. Ensure that the email provider supports SMTP login (e.g., Gmail, Yahoo, etc.).
Keywords: The script filters successful logins by keywords. Modify these keywords in the settings if needed.

This user guide should help you understand how to use the script efficiently.
