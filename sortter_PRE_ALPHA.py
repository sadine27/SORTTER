import os
import shutil

MAIN=["media","setups and apks","documents","additional"]

IMG=[f for f in os.listdir() if f.endswith(('.jpg','.png' ))]
JAR=[f for f in os.listdir() if f.endswith('.jar')]
EXE=[f for f in os.listdir() if f.endswith('.exe')]
PDF=[f for f in os.listdir() if f.endswith(".pdf")]
VID=[f for f in os.listdir() if f.endswith('.mp4')]
EXCEL=[f for f in os.listdir() if f.endswith('.xlsx')]
MSI=[f for f in os.listdir() if f.endswith('.msi')]
APK=[f for f in os.listdir() if f.endswith('.apk')]
ZIP=[f for f in os.listdir() if f.endswith('.zip')]
PPT=[f for f in os.listdir() if f.endswith('.pptx')]


for m in MAIN:
    os.makedirs(m, exist_ok=True)


for i in IMG:
    shutil.move(i,MAIN[0])
for i in JAR:
    shutil.move(i,MAIN[3])
for i in EXE:
    shutil.move(i,MAIN[1])
for i in PDF:
    shutil.move(i,MAIN[2])
for i in VID:
    shutil.move(i,MAIN[0])
for i in EXCEL:
    shutil.move(i,MAIN[2])
for i in MSI:
    shutil.move(i,MAIN[3])
for i in APK:
    shutil.move(i,MAIN[1])
for i in ZIP:
    shutil.move(i,MAIN[2])
for i in PPT:
    shutil.move(i,MAIN[2])