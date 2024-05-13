import os
import pydicom
import nibabel as nib
import dicom2nifti
import numpy as np

def validacion(mensaje, tipo_dato):
    while True:
        entrada = input(mensaje)
        try:
            valor_validado = tipo_dato(entrada)
            return valor_validado
        except ValueError:
            print(f"Error: Por favor, ingresa un valor válido de tipo {tipo_dato.__name__}.")

class Archivos:
    def __init__(self) -> None:
        pass
    def ingresar_paciente(self, dicom): #dicom es str
        if dicom.endswith('.dcm'):
            ds = pydicom.dcmread(dicom)
            nombre = ds.PatientName
            edad = ds.PatientAge
            id = ds.PatientID
            imagen = self.dicom_to_nifti(dicom)
            return nombre, edad, id, imagen
            
    def dicom_to_nifti(self, dicom):
        nifti_file = dicom.replace('.dcm', '.nii.gz')
        dicom2nifti.convert_dicom.dicom_array_to_nifti([dicom], nifti_file)

        nifti_image = nib.load(nifti_file)
        image_array = nifti_image.get_fdata()
        return image_array
class Paciente(Archivos):
    def __init__(self):
        super().__init__()
        self.__nombre = ""
        self.__edad = 0
        self.__ID = 0
        self.__imagen = None

    def ver_nombre(self):
        return self.__nombre
    def agregar_nombre(self, dicom):
        self.__nombre = self.ingresar_paciente(dicom)[0]
    def ver_edad(self):
        return self.__edad
    def agregar_edad(self, dicom):
        self.__edad = self.ingresar_paciente(dicom)[1]
    def ver_ID(self):
        return self.__ID
    def agregar_ID(self, dicom):
        self.__ID = self.ingresar_paciente(dicom)[2]
    def ver_imagen(self):
        return self.__imagen
    def agregar_imagen(self, dicom):
        self.__imagen = self.ingresar_paciente(dicom)[3]

