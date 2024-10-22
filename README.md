# LearnGerman

## Project Setup Instructions

This guide will help you set up the necessary environment and tools to build and run the project on a fresh Linux system.

## Prerequisites

1. **Install WSL and Ubuntu 18.04:**
    ```bash
    wsl --install -d Ubuntu-18.04
    ```

2. **Update and upgrade the system:**
    ```bash
    sudo apt update
    sudo apt upgrade
    ```

3. **Install essential packages:**
    ```bash
    sudo apt install python3 python3-pip python3-venv git
    sudo apt install build-essential libssl-dev libffi-dev python3-dev
    sudo apt install python3-kivy
    ```

4. **Install Buildozer:**
    ```bash
    pip3 install --user buildozer
    echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
    source ~/.bashrc
    ```

5. **Initialize Buildozer:**
    ```bash
    cd /mnt/c/Users/sdvid/Documents/Python/LearnGerman
    buildozer init
    ```

6. **Install additional dependencies:**
    ```bash
    sudo apt-get install zlib1g-dev
    pip3 install --user cython
    sudo apt-get install openjdk-8-jdk
    sudo apt-get install unzip
    ```

7. **Configure Android SDK:**
    ```bash
    cd /home/sipos/.buildozer/android/platform/android-sdk
    mkdir -p cmdline-tools/latest
    mv tools/cmdline-tools/* cmdline-tools/latest/
    rm -rf tools/cmdline-tools
    cd cmdline-tools/latest/bin
    yes | ./sdkmanager --licenses
    ./sdkmanager "platform-tools" "platforms;android-28" "build-tools;28.0.3"
    ```

8. **Install additional tools:**
    ```bash
    sudo apt-get install autoconf
    sudo apt-get install libtool
    sudo apt-get install zip
    ```

## Building the Project

Navigate to the project directory and build the project:
```bash
cd /mnt/c/Users/sdvid/Documents/Python/LearnGerman
buildozer -v android debug
```

Follow these steps to set up your environment and build the project successfully.
