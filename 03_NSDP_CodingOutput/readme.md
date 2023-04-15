# Welcome to the National Security Detection Portal.

### Application Usage

This Application's intent is to provide a portal for the public to report cybersecurity vulnerabilities online. For security purposes and access control, There are 3 types of 
users that can access the application's services:

1. **The public:**
   - Required to sign up and to log-in. An OTP will be sent for authentication.
   - Can Submit Vulnerabilities after log-in. 
   - Can View Vulnerabilities. 
   - Can view own personal data collected by our web application
2. **The Officers:** 
   - Requires a log-in. An OTP will be sent for authentication. 
   - Cannot sign up officer credentials can be added/updated by the admin.
   - can view submitted cases submitted by the public 
   - can send feedback to the public. 
3. **The Admin:**
   - Requires a multi-step OTP Log in 
   - Can view system log 
   - Can view/add/update/remove users 
   

### Secure Software Design Features

Be advised that this software was developed using the STRIDE model to provide secure design solutions using the following tools:

   1. pyOTP
   2. Regex
   3. Google authenticator

Safety features to counter security risks include: 
   - Two-factor authentication 
   - Strong password & OTP
   - Data encryption 
   - Input validation 
   - Security code review

### Launching The NSDP

**To launch the application locally, first navigate to the source code location on our GitHub repo here https://github.com/Rich-Orrell/Main_REV3d. Please download our source code and follow the steps below:**
   1. Download the latest programing language, Python 3.11
      - https://www.python.org/downloads/
    
   2. Download the latest compiler, Pycharm or Vscode.
      - https://www.jetbrains.com/pycharm/
      
   3. Navigate to the downloaded package folder using Pycharm or Vscode. 

   4. Install the Following packages by running the syntax below using Windows powershell or the compiler's terminal window:
        - <code> pip install flask </code>
        - <code> pip install mysql.connector </code>
        - <code> pip install pyotp </code> 
        - <code> pip install pillow </code>
      - <code> pip install -r requirements.txt </code>
    ** Be advice a file named requirments.txt can be run to download all the required packages in order to run the application**

    
   4. Run the **main.py** file and press <code>control + right-click </code> on the local server ip generated in the terminal window.

   5. Navigate to the sign-up button found in the home page, create a new account.
   6. An OTP window with a QR code will appear. Scan the code using your google authenticator application on your mobile device. 
   7. Navigate to the login button on the landing page, to insert your created credentials, you are now allowable to submit a vulnerabilities report.
   8. Submit your vulnerability concerns, you can now follow with the case status in the current vulnerabilities page.

**To launch the application Online, please use ths link https://cybercrime-portal.azurewebsites.net/ and then follow through steps 5 to 8.**





### The Authors of this web application are:

- Elsie Wong 
- Tarek Goda
- Richard Orrell
- Charles Kuyayama


## License

 NSDP Copyright 2032 

