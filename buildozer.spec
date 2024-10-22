[app]

# (str) Title of your application
title = Irregular Verbs

# (str) Package name
package.name = irreg

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,json

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Presplash background color (for new android toolchain)
presplash_color = #FFFFFF

# (str) Android SDK version to use (if empty, it will be automatically downloaded)
android.sdk = 30

# (str) Android build tools version to use (if empty, it will be automatically downloaded)
android.build_tools = 30.0.3

# (str) Android API level to use (if empty, it will be automatically downloaded)
android.api = 30

# (str) Android NDK version to use (if empty, it will be automatically downloaded)
android.ndk = 25b

# (str) Android NDK API level to use (if empty, it will be automatically downloaded)
android.ndk_api = 21

# (str) Icon of the application
icon.filename = icon.png

# (int) Log level (0 = error only, 1 = info, 2 = debug (default), 3 = trace)
log_level = 2