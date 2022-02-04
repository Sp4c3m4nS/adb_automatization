# Automatization of adb logcat and screenrecord 

This idea was for a personal project, but someone might benefit from it.

It is not that hard to use, but it has a few light bugs for now. Nothing that will interrupt you from using :)

# Installation

Make sure you have a rooted device configured for android debug bridge (adb). Also, we are currently using Mobile Insight application, but you can use another.

Check the retrieving path of the cellular data logs (in this case Mobile Insight), they may be different for you.

First, git clone it:

```
Git clone https://github.com/Y0uk1tsun3/adb_automatization
```

In this case, the logs collected and folders would be stored inside the 'adb_automatization' folder. If you want to change it to another folder, change the 'automatic_logs.py'
file (It is recommended to move all files to the same place to keep track of where they are, but you can just move this one and it should work)

# How to use it

1st. Connect your android rooted device to your computer with an USB cable
2nd. Run the automatics_log.py file, it should prompt you some questions. (If it crashes, there might be something wrong. Try again to see if it works then)
3rd. (Optional) Run the screenrecord
