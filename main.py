print('\033[1;32m')
print('''
  _____ _____     _____      _            _       _             
 |_   _|  __ \   / ____|    | |          | |     | |            
   | | | |__) | | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
   | | |  ___/  | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  _| |_| |      | |___| (_| | | (__| |_| | | (_| | || (_) | |   
 |_____|_|       \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                
                                                                By Rawad Abdallah''')
print('\033[0;36m');

#function to convert a decimal to binary
def convertToBinary(number):
  for i in range(0,4):
    temp = ""
    x = int(number[i])
    for j in range(0,8):
      if x % 2 == 0:
        temp += "0"
      else:
        temp+="1"
      x = int(x/2)
      number[i] = temp[::-1] 
  return number
#end function

#function to convert a binary to a decimal

def convertToDecimal(binary):
  
    for i in range(0,4):
      decimal = 0
      bin = ((str)(binary[i]))[::-1]
      num = 0
      for j in range(0,len(binary[i])):
        if bin[j] == '1':
          decimal += pow(2, num)
        num += 1
      binary[i] = decimal
    return binary

#end function

ipadd = input("Enter the ip address: ")
#converting inputted ip to an list contains each number ex : 192.168.1.1 => [192, 168, 1, 1]
ipadds = ipadd.split(".") 
# getting the subnet mask
answer = int(input("What do you have ? Choose by typing 1 or 2: \n1-Netmask number (i.e. 24). \n2-the Netmask ip Adrress (i.e. 255.255.255.0).\n "))
if(answer == 1):
  num_network = int(input("Enter the NetMask number :"))
  # calculating the subnet mask
  subnet=[]
  for y in range(0,num_network):
    if(num_network != 0):
      if(num_network >= 8):
        num_network -= 8
        subnet.append(255)
      else :
        n = 7
        num_sum = 0
        for x in range(0,num_network):
          num_sum += pow(2, n)
          n -= 1
        subnet.append(num_sum) 
        break
  if len(subnet) < 3: 
    subnet.append(0)
    subnet.append(0)
  elif len(subnet) < 4:
    subnet.append(0)
else: 
  subnet_string = input("Enter the NetMask ip : ")
  subnet = subnet_string.split(".")
#converting subnet to binary
convertToBinary(subnet)
#getting the network ip address

network_ip = []
convertToBinary(ipadds)

for i in range(0,4):
  bin = ""
  for j in range(0,8):
    
    bin += (str)((int)((subnet[i])[j]) * (int)((ipadds[i])[j]))
  network_ip.append(bin)

convertToDecimal(network_ip)
network_ipee = f"{network_ip[0]}.{network_ip[1]}.{network_ip[2]}.{network_ip[3]}"
print("The network ip: ",network_ipee)

#we need to invert the subnet
for i in range(0,4):
  subnet[i] = subnet[i].replace('1','a')
  subnet[i] = subnet[i].replace('0','b')
for i in range(0,4):
  subnet[i] = subnet[i].replace('a','0')
  subnet[i] = subnet[i].replace('b','1')


# Getting the broadcast ip address

broadcast = ['', '', '','']

convertToBinary(network_ip)

for i in range(0,4):
  for j in range(0, 8):
    temp_bin = str(int(network_ip[i][j]) + int(subnet[i][j]))
    if int(temp_bin) > 1:
      temp_bin = "1"
    broadcast[i] += str(temp_bin)

# Now we got the broadcast ip as a Binary we need to convert it to Decimal

convertToDecimal(broadcast)

#printing the broadcast ip

print(f'The broadcast ip: {broadcast[0]}.{broadcast[1]}.{broadcast[2]}.{broadcast[3]}')


