"""Daniel Lozano Simanca
Andrés Camilo Bastidas"""

from clases import *

#DICCIONARIOS
dict_pacientes = dict()
dict_archivos = dict()

def main():
    paciente = Paciente()
    while True:
        menu = validacion(
            """\nIngrese una opción: 
                       \n1- Ingresar Paciente 
                       \n2- Ingresar JPG o PNG
                       \n3- Transformación lineal img Dicom 
                       \n4- Gestionar JPG o PNG
                       \n5- Salir 
                       \nUsted ingresó la opción: """,
            int
        )
        if menu == 1:
            dicom = validacion("Ingrese el archivo Dicom: ", str)
            paciente.ingresar_paciente(dicom)
            paciente.agregar_nombre(dicom)
            paciente.agregar_edad(dicom)
            paciente.agregar_ID(dicom)
            paciente.agregar_imagen(dicom)
        elif menu == 2:
            pass
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        elif menu == 5:
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida, intente de nuevo")

if __name__ == "__main__":
    main()