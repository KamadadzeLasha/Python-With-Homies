# Install and Configure Python on Your Laptops/Computers

# setup your git and github accounts for later use.

# Welcome to the first seminar! In this session, we'll guide you through the process of installing and configuring Python on your Windows laptops or computers.

# **For Windows:**

# 1. **Download Python:**
#    - Open your web browser and go to the official Python website (https://www.python.org/).
#    - Navigate to the "Downloads" section.

# 2. **Choose Python Version:**
#    - You'll find the latest stable version prominently displayed. As of now, it might be Python 3.x (e.g., Python 3.9.7).
#    - Click on the download link for this version.

# 3. **Run Installer:**
#    - Once the installer is downloaded, locate the file (usually in your Downloads folder) and run it.
#    - Make sure to check the box that says "Add Python to PATH" during the installation process. This makes it easier to run Python from the command line.

# 4. **Customize Installation (Optional):**
#    - You may choose to customize the installation by clicking on the "Customize installation" button. This allows you to modify the installation path or select additional features.

# 5. **Complete Installation:**
#   - Click on the "Install Now" button to start the installation process.
#   - The installer will copy the necessary files and set up Python on your system.

# 6. **Verification:**
#   - To ensure that Python is installed correctly, open a command prompt or PowerShell window.
#   - Type `python --version` or `python -V` and press Enter. You should see the Python version you just installed.

# 7. **IDE (Integrated Development Environment):**
#   - While Python can be run directly from the command line, many developers prefer using an IDE for a more feature-rich programming experience.
#   - Consider installing an IDE such as VSCode, PyCharm, or Jupyter Notebook for a more convenient development environment.

# 8. **Virtual Environment (Optional):**
#   - It's good practice to work within a virtual environment to manage dependencies for different projects.
#   - To create a virtual environment, open a command prompt and run:
     
#     python -m venv myenv
     
#     Replace `myenv` with the name you want to give to your virtual environment.

# Congratulations! You have successfully installed and configured Python on your Windows machine. In the next seminar, we'll delve into writing your first Python program. If you encounter any issues during this installation process, feel free to reach out to your tutor during the upcoming lab session for assistance.

# Install and Configure Python on Your Laptops/Computers

# Welcome to the first seminar! In this session, we'll guide you through the process of installing and configuring Python on your Linux and macOS laptops or computers.

# **For Linux:**

# 1. **Check Python Version:**
#    - Most Linux distributions come with Python pre-installed. Open a terminal and check the installed version by typing:
#      ```
#      python --version
#      ```
#      If it's not installed, you will need to install it using your package manager.

# 2. **Install Python:**
#    - Use your package manager to install Python. For example, on Debian-based systems (like Ubuntu), you can use:
#      ```
#      sudo apt-get update
#      sudo apt-get install python3
#      ```
#      On Red Hat-based systems (like Fedora), you can use:
#      ```
#      sudo yum install python3
#      ```

# 3. **Verification:**
#    - To ensure that Python is installed correctly, open a terminal and type `python3 --version`. You should see the Python version you just installed.

# 4. **IDE and Virtual Environment (Optional):**
#    - Similar to Windows, you can choose to install an IDE for a better development experience.
#    - Create a virtual environment using:
#      ```
#      python3 -m venv myenv
#      ```
#      Replace `myenv` with the name you want to give to your virtual environment.

# **For macOS:**

# 1. **Install Homebrew (Optional but Recommended):**
#    - Homebrew is a popular package manager for macOS. If you don't have it installed, you can install it by following the instructions on the Homebrew website (https://brew.sh/).

# 2. **Install Python:**
#    - Once Homebrew is installed, open a terminal and run:
#      ```
#      brew install python
#      ```

# 3. **Verification:**
#    - To ensure that Python is installed correctly, type `python3 --version` in the terminal. You should see the Python version you just installed.

# 4. **IDE and Virtual Environment (Optional):**
#    - As with other platforms, consider installing an IDE for a more comfortable coding experience.
#    - Create a virtual environment using:
#      ```
#      python3 -m venv myenv
#      ```
#      Replace `myenv` with the name you want to give to your virtual environment.

# Congratulations! You have successfully installed and configured Python on your Linux or macOS machine. In the next seminar, we'll dive into writing your first Python program. If you encounter any issues during this installation process, feel free to reach out to your tutor during the upcoming lab session for assistance.

print("Hello World! <3")