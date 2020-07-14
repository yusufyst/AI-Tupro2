import numpy as np

#code ngebaca data csv
file = np.genfromtxt('Datatugas2.csv',delimiter=',')
file = file[1:,1:]

#Fuzzifikasi
#fungsi Pendapatan
def smallsalary(salary):
    if (salary<=5000):
        return 1
    elif (salary<20000):
        return (-(salary-20000)/(20000-5000))
    else:
        return 0

def mediumsalary(salary):
    if (5000<salary<=20000):
        return ((salary-5000)/(20000-5000))
    elif (20000<salary<60000):
        return (-(salary-60000)/(60000-20000))
    else:
        return 0

def largesalary(salary):
    if (salary<=60000):
        return 0
    elif (salary>90000):
        return 1
    else:
        return ((salary-60000)/(90000-60000))

#fungsi Hutang
def smalldebt(debt):
    if (debt<=3):
        return 1
    elif (debt<5):
        return (-(debt-5)/(5-3))
    else:
        return 0

def mediumdebt(debt):
    if (3<debt<=5):
        return ((debt-3)/(5-3))
    elif (5<debt<7):
        return (-(debt-7)/(7-5))
    else:
        return 0

def largedebt(debt):
    if(debt<7):
        return 0
    elif (debt>9):
        return 1
    else:
        return ((debt-9)/(9-7))

calculate = 0
result = []

#fungsi Inferensi yang terpilih
def getintfs(ss, sd, ms, md, ls, ld):
    get = []
    get.append(0)
    if (ms>0 and md>0):
        get.append(min(ms,md))
    if (ms>0 and ld>0):
        get.append(min(ms,ld))
    if (ls>0 and md>0):
        get.append(min(ls,md))
    if (ls>0 and ld>0):
        get.append(min(ls,ld))
    return max(get)

#fungsi Inferensi Tidak Dapat BLT
def notgetintfs(ss, sd, ms, md, ls, ld):
    notget = []
    notget.append(0)
    if (ss>0 and sd>0):
        notget.append(min(ss,sd))
    if (ms>0 and sd>0):
        notget.append(min(ms,sd))
    if (ls>0 and sd>0):
        notget.append(min(ls,sd))
    if (ss>0 and md>0):
        notget.append(min(ss,md))
    if (ss>0 and ld>0):
        notget.append(min(ss,ld))
    return max(notget)



for i in range(len(file)):
    salary = file[i][0]
    debt = file[i][1]
    get = []
    notget =[]

    ss = smallsalary(salary)
    ms = mediumsalary(salary)
    ls = largesalary(salary)
    sd = smalldebt(debt)
    md = mediumdebt(debt)
    ld = largedebt(debt)

    get = getintfs(ss,sd,ms,md,ls,ld)
    notget = notgetintfs(ss,sd,ms,md,ls,ld)

    #metode sugeno
    #Defuzzifikasi
    receive_help = ((get*100)+(notget*60))/(get+notget) > 73
    if receive_help:
        result.append(i+1)
        print("Dapat BLT, baris ke-" + str(i+1))
        calculate = calculate+1
    else:
        print("Tidak Dapat BLT")
print("maka " + str(calculate) + " orang yang dapat BLT")

#code output data didalam csv
np.savetxt('HasilTupro2.csv',result, delimiter=',', fmt='%s')
