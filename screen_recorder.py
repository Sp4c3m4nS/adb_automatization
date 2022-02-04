import os

print('Press enter to screen record\n')
record_input = input()
print('')

while record_input:
    print('Press enter to screen record\n')
    record_input = input()
    print('')

print('Recording...')

# Maximum 9 minutes of video, 3 min each because of adb limits. Add more if needed

screen_record = 'adb shell "screenrecord /sdcard/Movies/video_1.mp4; screenrecord /sdcard/Movies/video_2.mp4; screenrecord /sdcard/Movies/video_3.mp4;  \
    screenrecord /sdcard/Movies/video_4.mp4; screenrecord /sdcard/Movies/video_5.mp4; screenrecord /sdcard/Movies/video_6.mp4; \
        screenrecord /sdcard/Movies/video_7.mp4; screenrecord /sdcard/Movies/video_8.mp4; screenrecord /sdcard/Movies/video_9.mp4; \
            screenrecord /sdcard/Movies/video_10.mp4" & '
os.system(screen_record)
