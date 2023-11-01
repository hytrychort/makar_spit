def Simple_num(num):
    for i in range(2, num):
        if num%i==0:
            return False
    return True

def Palindrom(str):
    str = str.lower().replace(" ", "")
    for i in range(len(str)//2):
        if str[i]!=str[(i * -1) - 1]:
            return False
    return True

str = input()
print(Palindrom(str))