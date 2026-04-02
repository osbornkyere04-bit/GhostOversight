[app]
# (str) Title of your application
title = Ghost Oversight

# (str) Package name
package.name = ghostovr

# (str) Package domain (needed for android packaging)
package.domain = org.executive

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let's keep it light)
source.include_exts = py,png,jpg,kv,task

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# Optimized for Low-RAM: only include what is strictly necessary
requirements = python3,kivy==2.2.1,numpy,pillow

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions
android.permissions = CAMERA, INTERNET

# (int) Target Android API, use 33 for modern phones
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android logcat filters
android.logcat_filters = *:S python:D

# (str) The Android arch to build for
android.archs = arm64-v8a

# (bool) Use the skip_update for faster builds
buildozer.skip_update = 1