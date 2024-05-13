"""Daniel Lozano Simanca
Andrés Camilo Bastidas"""

from clases import *

#DICCIONARIOS
dict_pacientes = dict()
dict_archivos = dict()

def main():
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
            paciente = Paciente()
            dicom = validacion("Ingrese carpeta Dicom: ", str)
            nifti = validacion("Ingrese carpeta NifTi: ", str)
            paciente.ingresar_paciente(dicom, nifti)
            paciente.agregar_nombre(dicom, nifti)
            paciente.agregar_edad(dicom, nifti)
            paciente.agregar_ID(dicom, nifti)
            paciente.agregar_imagen(dicom, nifti)
            dict_pacientes[paciente.ver_ID] = paciente
            dict_archivos[paciente.ver_ID] = paciente.ingresar_paciente(dicom, nifti)[4]
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