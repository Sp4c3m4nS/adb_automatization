import os
from time import sleep

# Just a kill switch button for the adb logcat shell and screenrecord, since I did not find a way of doing it in the same code :)

def kill_switch():
    kill_input = ''
    command_kill_logcat = 'adb shell killall -2 logcat'
    command_kill_screen = 'adb shell killall -2 screenrecord'
    while kill_input != 'k':
        kill_input = input('Press "k" to kill the logcat and screen recording processes: ').lower()

    os.system(command_kill_logcat)

# Since you may need more than one screenrecord process, it is good to keep a while loop to kill all until it has finished
    
    while not os.system(command_kill_screen):
        sleep(0.2)
        os.system(command_kill_screen)

kill_switch()
