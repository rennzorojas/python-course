cursos=["PYTHON", "JAVA", "NET","EXCEL"]
#cursos.append("EXCEL")
#encontro=0
#lencur=len(cursos)
indice=int(input("Ingrese Curso a Listar:"))
for i in range (len(cursos)):
    if indice == i:
        encontro=1
        print(cursos[i])
        break
if encontro == 0:
    print("No se encontro el curso")