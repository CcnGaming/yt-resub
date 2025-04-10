# What is this
This is a python script to import all your youtube subs from a Google Takeout backup
# How to use
Step 1: Get a YouTube Data API v3 Key

Go to the Google Cloud Console:
Open your web browser and go to console.cloud.google.com.
Create a New Project (or Select an Existing One):
If you don't have a project, click "Select a project" at the top, then "New Project."
Give your project a name and click "Create."
If you have a project select it.
Enable the YouTube Data API v3:
In the left-hand menu, go to "APIs & Services" > "Library."
Search for "YouTube Data API v3" and select it.
Click "Enable."
Create API Credentials:
In the left-hand menu, go to "APIs & Services" > "Credentials."
Click "Create credentials" > "API key."
Copy the API key that appears.
It is best practice to restrict the key, by clicking on the key that was created, and restricting it to the youtube data api v3.
Save the API Key:
Paste the API key into a safe place (e.g., a text file). You'll need it later.
Step 2: Download Your Google Takeout YouTube Backup

Go to Google Takeout:
Open your web browser and go to takeout.google.com.
Select "YouTube and YouTube Music":
Scroll down and find "YouTube and YouTube Music."
Click the checkbox next to it.
Configure the Export:
Click "All YouTube data included" and deselect all. Then only select subscriptions.
Click OK.
Scroll to the bottom and click "Next step."
Choose your delivery method (e.g., download link via email).
Click "Create export."
Download the Backup:
Once the export is complete, you'll receive a download link.
Download the zip file.
Extract the zip file to a folder on your computer.
Find the CSV:
Inside of the extracted folder, there will be a .csv file that contains your subscriptions.
Step 3: Install the Google API Client Library

Open a Terminal or Command Prompt:
On Windows, search for "cmd" or "PowerShell."
On macOS or Linux, open the "Terminal."
Install the Library:
Type the following command and press Enter: pip install google-api-python-client
Step 4: Save the Python Script

Copy the Python Code:
Copy the Python script from my previous response.
Create a Python File:
Open a text editor (e.g., Notepad, VS Code).
Paste the Python code into the text editor.
Save the file with a .py extension (e.g., youtube_resubscribe.py).
Step 5: Run the Python Script

Open a Terminal or Command Prompt:
Navigate to the directory where you saved the youtube_resubscribe.py file.
For example, if the file is in D:\Code\Python, you would type cd D:\Code\Python and press Enter.
Run the Script:
Type the following command and press Enter: python youtube_resubscribe.py
Enter the API Key and CSV Path:
The script will prompt you to enter your YouTube Data API v3 key.
Paste the API key you saved earlier and press Enter.
The script will then prompt you to enter the full path to the subscriptions.csv file.
Enter the full path, for example: D:\Backups\Takeout\subscriptions.csv and press enter.
Wait for the Script to Finish:
The script will process the CSV file and subscribe to the channels.
It will print messages indicating the progress.
Important Notes:

API Key Security: Keep your API key secret. Do not share it with others or commit it to version control systems.
API Quotas: The YouTube Data API v3 has usage quotas. If you have a large number of subscriptions, you might exceed the quota.
File Paths: Make sure you enter the correct file paths. An incorrect path will cause the script to fail.
Error Messages: Pay attention to any error messages that the script displays. They can provide clues about what went wrong.
# Credits
Google Gemini for writing the code and for writing the how to guide
