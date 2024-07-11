__Program__     = "Converters._ToPy.PicToPy"    
__programer__   = "Themadhood Pequot"
__Date__        = "7/26/2023"
__version__     = "0.0.1"
__update__      = ""
__info__        = ""


import io,base64,os


def PicToPy(fileName,fileExtention,FromPath,ToPath=None,toFileName=None,
            VarName=None,cama=False,write="a",dct=True):
    print("read photo and encode")
    print(FromPath)
    with open(f"{FromPath}/{fileName}{fileExtention}", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())

    print("decoding pic")  
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

    print("writeing to py")
    with io.open(f"{ToPath}/{toFileName}.py", write, encoding='utf-8') as py:
        if dct:
            py.write(f"'{VarName}':")
        else:
            py.write(f"{VarName} = ")
        py.write(f"'{my_string}'")
        if cama and dct:
            py.write(f",")
        elif not cama and dct:
            py.write("}")
        py.write(f"\n")
        py.close()

    print("Done")


    
