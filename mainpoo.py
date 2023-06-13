from cosas import Alumno

def main():

    """
    al1= Alumno()
    print(al1)
    al2= Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    #
    print("-------------------")
    al1.facultad="FES Aragón EDOMEX"
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("-----Un vistazo")
    print(vars(al1))
    print(vars(al2))
    print("-----modificar-----")
    al1.edad=999
    print(vars(al1))
    print(vars(al2))
    """
    al1 = Alumno("Diego", "ICO", 19 )
    al2= Alumno("Monse", "Derecho", 12)
    print(vars(al1))
    al1.__edad= 333
    print(al1.__edad)
    print(vars(al1))



main()