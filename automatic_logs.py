import os
from time import sleep

# Ask for the app that the user wants to collect the logs of

appname = input('Enter the app name: ').lower()
print('')

# Define string variables to find the current directory (mainly in case of first time unning the logs of an app), 
# create a variable for the future app name directory and mobileinsight logs directory

current_directory = os.getcwd() # Example: C:\User\path\to\logs
appname_directory = f'{current_directory}/{appname}'

# Ask if it is the first log data collection of this application. In case it isn't, we should avoid conflicts in the
# directory creation, so ask for given path and use it in the log collection

print('Is it the first time running the log of this application? (Y/N) \n')
directory_creation = input().lower()

# Verify inputs of the first time running question

while directory_creation != 'n' and directory_creation != 'y':
    print('\nThe input is invalid, you should respond with "Y" or "y", "N" or "n" \n')
    print('Try again \n ')
    print('Is it the first time running the log of this application? (Y/N) \n')
    directory_creation = input().lower()   

# This gets a bit messy, if the user inputs that it is not the first time of collection, we need to ask the path (and verify if it exists)
# and then ask for the number of the try to index it in the beginning with the new files

if directory_creation == 'n':
    print('\nGive the app name folder path (C:/path/to/folder/of/appname)\n')
    appname_directory = input()
    print('')

    while os.system(f'cd {appname_directory}'):
        print('\nError: Try again')
        print('\nGive the app name folder path (C:/path/to/folder/of/appname)\n')
        appname_directory = input()
        print('')

    print('Which try is this? (Type a number to index the logcat file with [number of try]_[app name]_logcat.txt)\n')
    number_try = input()

    while number_try.isdigit() == False or int(number_try) <= 0:
        print('\n Your input is invalid, please input any integer number >= 1\n')
        number_try = input()
        print('')

# If the user is doing for the first time (most cases), just create the directory of the app and the index will be '1'

elif directory_creation == 'y':
    os.makedirs(appname_directory)
    number_try = '1'

# Defining the last directory after the User's input, the mobileinsight one (although for other applications it may be another name)

mobileinsight_directory = appname_directory + f'/{number_try}_mobileinsight'
recordings_directory = appname_directory + f'/{number_try}_recording'

# 1st Clear logcat, then run logcat in the given time and index it

logcat_clear = f'adb logcat -c'
os.system(logcat_clear)
logcat_command = f'adb logcat -v time > {appname_directory}/{number_try}_{appname}_logcat.txt'
os.system(logcat_command)

# Run adb pull and store it at the new mobileinsight directory

mobileinsight_pull_command = f'adb pull /sdcard/mobileinsight/log/. {mobileinsight_directory}'
os.system(mobileinsight_pull_command)

# Clean the adb pull folder for future logs
adb_pull_clean = f'adb shell "rm -r /sdcard/mobileinsight/log/*"'
os.system(adb_pull_clean)

# Screen Record pull and clean (optional)

sleep(5)

record_pull = f'adb pull /sdcard/Movies/. {recordings_directory}'
os.system(record_pull)

record_clean = f'adb shell "rm -r /sdcard/Movies/*"'
os.system(record_clean)
    