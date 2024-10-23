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
    sudo apt-get update
    sudo apt-get install openjdk-8-jdk
    sudo apt-get install unzip
    sudo apt install python3 python3-pip ipython3
    sudo apt install cython
    sudo apt-get install autoconf
    sudo apt install build-essential libltdl-dev libffi-dev libssl-dev python-dev
    sudo pip3 install --upgrade cython
    sudo apt-get install zip
    ```

    Check python version:
    ```bash
    python3 --version
    ```
    
    If python version is lower than 3.8, 
    Install Python 3.8 using the following command
    ```bash
    sudo apt install python3.8
    ```

    Update the alternatives to set Python 3.8 as the default Python version:
    ```bash
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
    ```

    Check the python version again. Now it should be 3.8:
    ```bash
    python3 --version
    ```

4. **Install Buildozer:**
    ```bash
    git clone https://github.com/kivy/buildozer.git
    cd buildozer
    sudo python3 setup.py install
    ```

5. **Initialize Buildozer:**
    ```bash
    cd /mnt/PathToProjectFolder
    buildozer init
    ```

## Building the Project

Navigate to the project directory and build the project:
```bash
cd /mnt/PathToProjectFolder
buildozer -v android debug
```

Follow these steps to set up your environment and build the project successfully.