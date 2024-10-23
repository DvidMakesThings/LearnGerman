[app]

# (str) Title of your application
title = Irregular Verbs

# (str) Package name
package.name = irreg

# (str) Package domain (needed for android/ios packaging)
package.domain = org.irreg

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,json, txt

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

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.gradle_dependencies = com.google.firebase:firebase-ads:21.4.0
android.enable_androidx = True
p4a.branch = master
