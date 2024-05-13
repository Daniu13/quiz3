import os
import pydicom
import nibabel as nib
import dicom2nifti
import numpy as np
import cv2
import matplotlib.pyplot as plt

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
            return nombre, edad, id, imagen, ds
            
    def dicom_to_nifti(self, dicom):
        nifti_file = dicom.replace('.dcm', '.nii.gz')
        dicom2nifti.convert_dicom.dicom_array_to_nifti([dicom], nifti_file)

        nifti_image = nib.load(nifti_file)
        image_array = nifti_image.get_fdata()
        return image_array

    #Parte 2
    def rotar_imagen(self, dicom, angulo):
        imagen_dicom = cv2.imread(dicom, cv2.IMREAD_GRAYSCALE)
        filas, columnas = np.shape(imagen_dicom)
        center = (columnas/2, filas/2)
        matriz_rot = cv2.getRotationMatrix2D(center, angulo, 1.0)
        imagen_rotada = cv2.warpAffine(imagen_dicom, matriz_rot, (columnas, filas))

        return imagen_dicom, imagen_rotada

    def mostrar_imagenes(self, imagen_dicom, imagen_rotada, titulo='Original', titulo_rot='Rotada'):
        fig = plt.figure(figsize=(10, 5))
        axes = fig.subplots(1, 2)
        axes[0].imshow(imagen_dicom, cmap='gray')
        axes[0].set_title(titulo)
        axes[1].imshow(imagen_rotada, cmap='gray')
        axes[1].set_title(titulo_rot)
        plt.show()
    
    def guardar_imagen(self, ruta, imagen_rotada):
        cv2.imwrite(ruta, imagen_rotada)
        print(f"Imagen guardada en: {ruta}")
        
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

