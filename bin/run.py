#!/opt/rh/rh-python36/root/usr/bin/python3
# Description: This script can get the IP address in a list.
#              And then use command "ipmitool" to change the BMC admin password.
#
# Author: Richard Tsai
# Date: 2019-03-29
#

import subprocess

IP_LIST_PATH='../conf/IP_List'

def main():
   
    # Get the Server IP address from ../conf/IP_List 
    
    with open(IP_LIST_PATH) as LIST1:
        for line in LIST1:
            fields = line.strip().split()
            print('Device Mac Address : ' + fields[0])

            # call OS level command by "ipmitool" to change the BMC admin password
            subprocess.call('ipmitool -I lanplus -H %s -U admin -P password user set password 2 22044755' % fields[0], shell=True, stderr=subprocess.STDOUT)

if __name__ == '__main__':
    
    main()
    
