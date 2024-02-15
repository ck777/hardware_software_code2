globalvar = 42

def my_address (str, var):
    print ("\t\t\t\{1} address: {0}\n\t\t\t{1} value:  {2}".format(id(var), str,var))

def ask_me (*num): # Ask the user for a number
    if num[0] == 1:
        ans = int(input("please provide a number:"))
        return ans
    elif num[0] == 2:
         print("what do you think you will get.")
         print("when you add globalvar + num1?")
         input('globalvar = {} and num = {} ". format(num)[1], num[-1]))
else:
    print("globalvar = {} and num = {}  ".format(num[1], num [-1]))

def add(num1):
    globalvar = num1
    my_address('3. add globalvar', globalvar )
    globalvar = globalvar + num1
    print('in add function globalvar + num1 = {}'.format(global var))
    return globalvar

def global_add(num1):
    glonal globalvar
    my_address('globalvar address, globalvar')
    globalvar = globalvar + num1
    print ('in global_add globalvar + num1 ='{}'.format(globalvar))
    return globalvar
def main():
    my_address ('main globalvar, globalvar')
    num1 = ask_me (1)
    my_address('main num1, num1')
    ask_me(3, globalvar, num1)
    sum = add(num1)
    ask_me(3,globalvar, sum)

if__name__== "__main__":

  main()
def clear_screen():
    my_address('1. main globalvar, globalvar)
    if name == "nt":
    _  = system("cls")
else:
    _ = systen("clear")
