import os, pydicom, cv2, dicom2nifti
import nibabel as nib
import numpy as np
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
    def ingresar_paciente(self, carpeta_dicom, nifti):
        if not os.path.isdir(carpeta_dicom):
            print("La carpeta no existe.")
            return None
        lista_dicom = [os.path.join(carpeta_dicom, f) for f in os.listdir(carpeta_dicom) if f.endswith('.dcm')]
        if not lista_dicom:
            print("No se encontraron archivos DICOM en la carpeta.")
            return None
        try:
            ds = pydicom.dcmread(lista_dicom[0])
            nombre = ds.get("PatientName", None)
            edad = ds.get("PatientAge", None)
            id = ds.get("PatientID", None)
            imagen = self.dicom_to_nifti(carpeta_dicom, nifti)
            return nombre, edad, id, imagen, ds
        except FileNotFoundError:
            print("Archivo DICOM no encontrado.")
        except Exception as e:
            print(f"Error al procesar archivos DICOM: {str(e)}")
            
    def dicom_to_nifti(self, dicom, nifti): #dicom y nifti son rutas
        if not os.path.exists(nifti):
            os.makedirs(nifti)
        dicom2nifti.convert_directory(dicom, nifti)
        nifti_file = os.path.join(nifti, os.listdir(nifti)[0])
        nifti_image = nib.load(nifti_file)
        image_array = nifti_image.get_fdata()
        return image_array

    #Parte 2
    def rotar_imagen(self, archivo_dicom, angulo):
        ds = pydicom.dcmread(archivo_dicom)
        imagen_dicom = ds.pixel_array
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

    def imagen_dict(self, ruta_img):
        if os.path.exists(ruta_img):
            img_cell = cv2.imread(ruta_img)
            return img_cell, True
        else:
            print('El archivo no existe.')
            return None, False

    def binarizar_transformar(self, archivo_imagen, umbral, tamano_kernel, ruta):
        if self.imagen_dict(archivo_imagen)[1]: 
            img_cell = cv2.cvtColor(self.imagen_dict(archivo_imagen)[0], cv2.COLOR_BGR2RGB)

            img_cellR = img_cell[:,:,2]
            _, imgB = cv2.threshold(img_cellR, umbral, 255, cv2.THRESH_BINARY)
            kernel = np.ones((tamano_kernel,tamano_kernel), np.uint8)
            kernel1 = np.ones((tamano_kernel,tamano_kernel), np.uint8)
            imaDil = cv2.dilate(imgB, kernel, iterations = 1)
            imaEro = cv2.erode(imaDil,kernel1,iterations = 1)
            texto = f"Imagen binarizada (umbral={umbral}, tamaño kernel={tamano_kernel})"
            imaEro = cv2.putText(imaEro, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            self.guardar_imagen(ruta, imaEro)
            
            return imaEro

        else:
            print('El archivo no existe.')
        
class Paciente(Archivos):
    def __init__(self):
        super().__init__()
        self.__nombre = ""
        self.__edad = 0
        self.__ID = 0
        self.__imagen = None

    def ver_nombre(self):
        return self.__nombre
    def agregar_nombre(self, dicom, nifti):
        self.__nombre = self.ingresar_paciente(dicom, nifti)[0]
    def ver_edad(self):
        return self.__edad
    def agregar_edad(self, dicom, nifti):
        self.__edad = self.ingresar_paciente(dicom, nifti)[1]
    def ver_ID(self):
        return self.__ID
    def agregar_ID(self, dicom, nifti):
        self.__ID = self.ingresar_paciente(dicom, nifti)[2]
    def ver_imagen(self):
        return self.__imagen
    def agregar_imagen(self, dicom, nifti):
        self.__imagen = self.ingresar_paciente(dicom, nifti)[3]

