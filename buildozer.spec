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
source.include_exts = py,png,jpg,kv,atlas,json

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

# (list) Permissions
android.permissions = INTERNET

# (bool) Enable Android logcat
log_level = 2

# (str) Android entry point, default is ok for Kivy-based apps
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android architecture to use
android.arch = armeabi-v7a

# (str) The format used to package the app for release mode (aab or apk)
android.release_artifact = aab

# (str) Android SDK version to use (if empty, it will be automatically downloaded)
android.sdk = 28

# (str) Android build tools version to use (if empty, it will be automatically downloaded)
android.build_tools = 28.0.3

# (str) Android API level to use (if empty, it will be automatically downloaded)
android.api = 28

# (str) Android NDK version to use (if empty, it will be automatically downloaded)
android.ndk = 19b

# (str) Android NDK API level to use (if empty, it will be automatically downloaded)
android.ndk_api = 21