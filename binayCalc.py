def calcBinary(f_bin,s_bin,ch):
    if ch == 1:
        f_res=bin_dec(f_bin)+bin_dec(s_bin)
    elif ch == 2:
        f_res=bin_dec(f_bin)*bin_dec(s_bin)
    elif ch == 3:
        f_res=bin_dec(f_bin)-bin_dec(s_bin)
    elif ch == 4:
        f_res=int(bin_dec(f_bin)/bin_dec(s_bin))
        s_res=bin_dec(f_bin)%bin_dec(s_bin)
        if s_res != 0:
            return dec_bin(f_res)+" remainder is "+dec_bin(s_res)
    return dec_bin(f_res)

def bin_dec(bin_n):
    dec = 0
    bin_l = len(bin_n)
    f = bin_l-1
    for i in range(bin_l):
        dec+=int(a[f- i]) * (2 ** i)
    return dec

def dec_bin(n):
    if n == 0:
        return "0"
    bin_r=""
    while n > 0:
        bin_r = str(n%2) + bin_r
        n = n // 2
    return bin_r

while(True):
    a = input("enter first binary :")
    b = input("enter second binary :")
    x = int(input(
    """0 to abort
1 for addition, 
2 for multiplication,
3 for subtraction,
4 for division :
"""))
    if x in [1,2,3,4]:
        print("\n")
        print("the result "+calcBinary(a,b,x)+" \n")
    elif x == 0:
        break
    else:
        print("\n")
        print("no valid option\n")