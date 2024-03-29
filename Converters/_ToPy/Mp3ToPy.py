__Program__     = "Converters._ToPy.Mp3ToPy"    
__programer__   = "Themadhood Pequot"
__Date__        = "7/26/2023"
__version__     = "0.0.1"
__update__      = ""
__info__        = ""


import io,base64,os
from pygame import mixer

def _splstr(st,ToPath,toFileName,lvl=1):
    if len(st) > 10000:
        half = len(st)//2
        splstr(st[:half],ToPath,toFileName,lvl+1)
        if lvl == 1:
            print("50%")
        elif lvl == 2:
            print("25%")
        splstr(st[half:],ToPath,toFileName,lvl+2)
        if lvl == 1:
            print("100%")
    else:
        with io.open(f"{ToPath}/{toFileName}.py", 'a', encoding='utf-8') as log:
            log.write(st)
            log.close()

def Mp3ToPy(fileName,FromPath,ToPath=None,toFileName=None,
            VarName=None,cama=False,write="a",dct=True):
    mixer.init()
    print("Load mp3")
    raw = mixer.Sound(f"{FromPath}/{filename}.mp3")
    print("getting raw mp3")
    raw = raw.get_raw()
    print("encoding mp3")
    my_string = base64.b64encode(img_file.read()) 
    print("decoding mp3")    
    my_string = my_string.decode('utf-8')

    #set var saftys
    if ToPath == None:
        ToPath = FromPath
    if toFileName == None:
        toFileName = fileName
    if VarName == None:
        VarName = fileName
    if cama and not dct:
        dct = True

    with io.open(f"{ToPath}/{toFileName}.py", write, encoding='utf-8') as log:
        if dct:
            py.write(f"'{VarName}':")
        else:
            py.write(f"{VarName} = ")
        log.close()

    _splstr()

    with io.open(f"{ToPath}/{toFileName}.py", write, encoding='utf-8') as log:
        if cama and dct:
            py.write(f",")
        elif not cama and dct:
            py.write("}")
        log.write(f"'\n")
        log.close()
        
    print("Done")


    
