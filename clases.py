"""Daniel Lozano Simanca
Andrés Camilo Bastidas"""

import os
import pydicom
import nibabel as nib
import dicom2nifti
import numpy as np

#DICCIONARIOS
dict_pacientes = dict()
dict_archivos = dict()

class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__edad = 0
        self.__ID = None

    def ver_nombre(self):
        return self.__nombre
    def agregar_nombre(self, nombre):
        self.__nombre = nombre
    def ver_edad(self):
        return self.__edad
    def agregar_edad(self, edad):
        self.__edad = edad
    def ver_ID(self):
        return self.__ID
    def agregar_ID(self, ID):
        self.__ID = ID
    def ver_imagen(self):
        return self.__imagen
    def agregar_imagen(self, imagen):
        self.__imagen = imagen

class Archivo:
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