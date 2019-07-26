DNI = input("ingresar el DNI:")
dpt = input("ingresar la Dept:")
sue = float(input("ingresar Sueldo:"))
ts = input("ingresar Tiempo de Servicio:")

#float soporta números decimales
# : equivale a ENTONCES
# if = verdadero
# elif = verdadero
# else = falso
# and ambas se deben cumplir
# or una sola se cumple

if dpt == "LOG" and ts>=2:
    bon=sue*0.02
elif dpt == "SIS" and ts>=3:
    bon=sue*0.03
elif dpt == "RH" or dpt == "MK":
    bon=sue*0.05
else:
    bon=sue*0.01

pago = sue + bon

# ,result para llamar al resultado

print("Sueldo a percibir:",pago)

#Run code and Enter Data