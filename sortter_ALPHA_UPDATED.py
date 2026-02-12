import os
import shutil

# list of the directories needed 
PRIME=["Images","Videos","Audio","Other Media","CAD","Documents","Compressed Files","Scripts","Apps","Config. Files"]

# the types of flie 
IMAGES=[f for f in os.listdir() if f.endswith((".jpg",".JPG",".jpeg",".JPEG",".png",".PNG",".gif",".GIF",".bmp",".BMP",".tiff",".TIFF",".svg",".SVG",".webp",".WEBP"))]
AUDIOS=[f for f in os.listdir() if f.endswith((".mp3",".MP3",".aac",".AAC",".wav",".WAV",".flac",".FLAC",".alac",".ALAC",".ogg",".OGG",".wma",".WMA"))]
VIDEOS=[f for f in os.listdir() if f.endswith((".mp4",".MP4",".avi",".AVI",".mkv",".MKV",".wmv",".WMV",".flv",".FLV",".webm",".WEBM"))]
OTHER_MEDIA=[f for f in os.listdir() if f.endswith((".mov",".MOV"))]
DOCS=[f for f in os.listdir() if f.endswith((".doc",".DOC",".docx",".DOCX",".ppt",".PPT",".pptx",".PPTX",".xls",".XLS",".xlsx",".XLSX",".odt",".ODT",".rtf",".RTF",".txt",".TXT",".pdf",".PDF"))]
COMPRESSED=[f for f in os.listdir() if f.endswith((".zip",".ZIP",".rar",".RAR",".7z",".7Z",".tar",".TAR",".gz",".GZ",".bz2",".BZ2",".xz",".XZ",".iso",".ISO"))]
SCRIPTS=[f for f in os.listdir() if (f.endswith((".py",".PY",".cpp",".CPP",".c",".C",".cs",".CS",".java",".JAVA",".js",".JS",".ts",".TS",".rb",".RB",".php",".PHP",".swift",".SWIFT",".go",".GO",".rs",".RS",".kt",".KT"))) and not f == "sortter_ALPHA.py"]
APPS=[f for f in os.listdir() if f.endswith((".exe",".EXE",".apk",".APK",".xapk",".XAPK",".msi",".MSI",".app",".APP",".bat",".BAT",".com",".COM",".jar",".JAR",".deb",".DEB",".rpm",".RPM"))]
CONFIG=[f for f in os.listdir() if f.endswith((".ini",".INI",".cfg",".CFG",".conf",".CONF",".xml",".XML",".json",".JSON",".yaml",".YAML",".yml",".YML"))]
CAD=[f for f in os.listdir() if f.endswith((".dwg",".DWG",".dxf",".DXF",".dwt",".DWT",".dws",".DWS",".bak",".BAK",".f3d",".F3D",".step",".STEP",".stp",".STP",".igs",".IGS",".obj",".OBJ",".smt",".SMT"))]

# to create the primary directories 
for p in PRIME:
    os.makedirs(p,exist_ok=True)

# shifting each file
for i in IMAGES:
    shutil.move(i,PRIME[0])
for i in AUDIOS:
    shutil.move(i,PRIME[2])
for i in VIDEOS:
    shutil.move(i,PRIME[1])
for i in OTHER_MEDIA:
    shutil.move(i,PRIME[3])
for i in DOCS:
    shutil.move(i,PRIME[5])
for i in COMPRESSED:
    shutil.move(i,PRIME[6])
for i in SCRIPTS:
    shutil.move(i,PRIME[7])
for i in APPS:
    shutil.move(i,PRIME[8])
for i in CONFIG:
    shutil.move(i,PRIME[9])
for i in CAD:
    shutil.move(i,PRIME[4])

