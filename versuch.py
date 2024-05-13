import pydicom

dicom = 'Sarcoma/img1/1-01.dcm'

ds = pydicom.dcmread(dicom)
print(ds)
nombre = ds.PatientName
edad = ds.get("PatientAge", None)
id = ds.get("PatientID", None)

print(nombre)
print(edad)
print(id)