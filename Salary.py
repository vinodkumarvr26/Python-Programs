Basicsal = float(input("Enter the basic salary:"))
hra=float(input("Enter the hra:"))
da=float(input("Enter the da:"))
Proftax =200
Grosssal= Basicsal + hra + da
Incometax = 0.01 * Grosssal
Netsal=Grosssal-Proftax-Incometax
print("Gross sal:",Grosssal)
print("Net salary:",Netsal)
