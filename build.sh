#!/bin/bash

# Set the path to your Android SDK and NDK
export ANDROIDSDK="C:\Users\sipos\AppData\Local\Android\Sdk"
export ANDROIDNDK="C:\Users\sipos\AppData\Local\Android\Sdk\ndk\28.0.12433566"

# Build the APK
p4a apk --private . --package=org.example.verblearning --name "Verb Learning App" --version 0.1 --bootstrap=sdl2 --requirements=python3,kivy,kivymd,pyjnius --arch=armeabi-v7a