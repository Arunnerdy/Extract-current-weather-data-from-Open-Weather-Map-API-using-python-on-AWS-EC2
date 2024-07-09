# Extract-current-weather-data-from-Open-Weather-Map-API-using-python-on-AWS-EC2

First create an EC2 instance in the AWS with Linux-Ubuntu as a OS and then Open the VS Code and install the Extension Remote - SSH.
And the go to the view option and click command plate.
Select the configure connection.
And then type the following configurations,
    HOST Hostname(Name of your EC2 Instance)
    HostName (EC2 instance public IPv4 Address)
    User ubuntu
    IdentityFile Path to your key-pair file
After connecting your ec2 instance inn your vs code
Run the following commands in the terminal,
   sudo apt update
   sudo apt install pip
   pip install pandas(Incase it doesnt work use sudo apt install python3-pandas).

Then create a account on openweather and get your API key
And then create the file name main.py on your instance
