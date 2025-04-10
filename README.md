# What is this
This is a python script to import all your YouTube subs from a Google Takeout backup. This is meant for if you have 2 accounts and you want to move your YouTube data or if you lost accces to your account
# How to use
1. Download the Tool:

1. Download the yt-resub.exe file.
2. Get Your YouTube Data API v3 Key:

Go to the Google Cloud Console: Open your web browser and go to console.cloud.google.com.
Create a Project: If you don't have one, create a new project. Otherwise, select your existing project.
Enable the YouTube Data API v3: In the left-hand menu, go to "APIs & Services" > "Library." Search for "YouTube Data API v3" and enable it.
Create API Credentials: In the left-hand menu, go to "APIs & Services" > "Credentials." Click "Create credentials" > "API key."
Copy and Save: Copy the API key that appears and save it in a safe place.
3. Download Your YouTube Subscription Data:

Go to Google Takeout: Open your web browser and go to takeout.google.com.
Select YouTube and YouTube Music: Scroll down and check the box next to "YouTube and YouTube Music."
Configure: Click "All YouTube data included" and deselect everything except "subscriptions". Click ok. Click next step. Select your delivery method, and create the export.
Download the CSV: Once the export is ready, download the zip file and extract it. Find the subscriptions.csv file inside.
4. Run the Tool:

Open the folder where you downloaded the yt-resub.exe
Double-click the executable file.
Enter API Key: The tool will prompt you to enter your YouTube Data API v3 key. Paste the key you saved earlier and press Enter.
Enter CSV Path: The tool will then ask for the full path to your subscriptions.csv file.
Important: You must provide the full path. For example: C:\Users\YourName\Downloads\Takeout\YouTube and YouTube Music\subscriptions\subscriptions.csv
Press Enter.
5. Wait for the Tool to Finish:

The tool will process the CSV file and resubscribe to your channels.
It will display messages indicating the progress.
#Troubleshooting:

Invalid API Key: If you get an error about an invalid API key, double-check that you copied and pasted it correctly.
Invalid File Path: If you get an error about an invalid file path, ensure that you entered the full path to the subscriptions.csv file. A common mistake is providing the folder path instead of the file path.
Permission Errors: If you get a permission error, make sure the subscriptions.csv file is not open in another program and that you have read permissions for the file.
API Quota Issues: If you have a very large number of subscriptions, you may encounter API quota limitations. If this happens, you will need to wait a while, and run the program again.
Read the README: If you encounter any problems, please read the included README.txt file for more detailed instructions and troubleshooting tips.
# Credits
Google Gemini for writing the code and for writing the how to guide
