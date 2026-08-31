#leer la nota de un estudiante y decir si aprobo o su aprendizaje inicial. 

from colorama import Fore, Style 

grade = int(input("Ingrese la nota: "))
if grade >=70:
 
 print(Fore.GREEN + "usted ha aprobado.")
else:
 print(Fore.RED + "su aprendizaje es inicial:")
 Style.RESET_All