#program:       pyFormats
#purpose:       
#progamer:      Themadhood Pequot 10/23/2023

_FILE = "Converters._ToPy.pyFormats"
_VERSION = "0.0.1"

import io
import Error

def pyFormats(data,path,var,writetype="w"):
    st = Error.time.time()
    Error.Log(f"\nwriting usable py","Log.txt")
    try:
        if not Error.os.path.isfile(f"{path}.py"):
            Error.os.makedirs(Error.os.path.dirname(path), exist_ok=True)
    except:
        pass
    try:
        with io.open(path+".py", writetype, encoding='utf-8') as py:
            py.write(f"{var} = ")
            if type(data) == dict:
                Error.Log(f"\nformating dict","Log.txt")
                py.write(py_dct(data,1))
            elif type(data) == list:
                Error.Log(f"\nformating list","Log.txt")
                py.write(py_lst(data,1))
            elif type(data) == tuple:
                Error.Log(f"\nformating object","Log.txt")
                py.write(py_obj(data,1))
            elif type(data) == str:
                Error.Log(f"\nformating str","Log.txt")
                py.write(py_str(data))
            else:
                Error.Log(f"\nformating other","Log.txt")
                py.write(str(data))
            py.write(f"\n\n")
            py.close()
            
        Error.Log(f"writing usable py runtime: {Error.LenTime(st)}\n","Log.txt")
    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","pyFormats",
                           f"failed to format and write py",e],"Functions")
        Error.Log(f"\nError ocured: {e}","Log.txt")

def Tabs(num=0):
    t = ""
    try:
        for i in range(0,num):
            t += "    "
    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","Tabs",
                           f"filed to add {num} tabs",e],"Functions")
    return t

def py_lst(lst,lvl=0):
    try:
        st = "["
        t = Tabs(lvl) 
        for o in lst:
            if type(o) == dict:
                Error.Log(f"{t}formating dict","Log.txt")
                st += f"\n{t}"
                st += py_dct(o,lvl+1)
            elif type(o) == list:
                Error.Log(f"{t}formating list","Log.txt")
                st += f"\n{t}"
                st += py_lst(o,lvl+1)
            elif type(o) == tuple:
                Error.Log(f"{t}formating object","Log.txt")
                st += f"\n{t}"
                st += py_obj(o,lvl+1)
            elif type(o) == str:
                Error.Log(f"{t}formating str","Log.txt")
                st += py_str(o)
            else:
                Error.Log(f"{t}formating other","Log.txt")
                st += str(o)
            st += ","
            
        if st[-1] != "[":
            st = st[:-1]
        st += "]"
        return st
    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","py_lst",
                           f"filed to format to list",e],"Functions")

def py_dct(dct,lvl=0):
    try:
        st = "{"
        t = Tabs(lvl)
        keys = list(dct)
        for k in keys:
            if type(dct[k]) == dict:
                Error.Log(f"{t}formating dict","Log.txt")
                st += f"{py_str(k)}:"
                st += py_dct(dct[k],lvl+1)
            elif type(dct[k]) == list:
                Error.Log(f"{t}formating list","Log.txt")
                st += f"{py_str(k)}:"
                st += py_lst(dct[k],lvl+1)
            elif type(dct[k]) == tuple:
                Error.Log(f"{t}formating object","Log.txt")
                st += f"{py_str(k)}:"
                st += py_obj(dct[k],lvl+1)
            elif type(dct[k]) == str:
                Error.Log(f"{t}formating str","Log.txt")
                st += f"{py_str(k)}:"
                st += py_str(dct[k])
            else:
                Error.Log(f"{t}formating other","Log.txt")
                st += f"{py_str(k)}:"
                st += str(dct[k])
            st += f",\n{t}"
            
        #remove tabs
        while st[-1] == " ":
            st = st[:-1]
        
        st = st[:-2]#remove new line and cama
        st += "}"
        return st
    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","py_dct",
                           f"filed to format to dict",e],"Functions")

def py_obj(obj,lvl=0):
    try:
        st = "("
        t = Tabs(lvl)
        for o in obj:
            if type(o) == dict:
                Error.Log(f"{t}formating dict","Log.txt")
                st += f"\n{t}"
                st += py_dct(o,lvl+1)
            elif type(o) == list:
                Error.Log(f"{t}formating list","Log.txt")
                st += f"\n{t}"
                st += py_lst(o,lvl+1)
            elif type(dct[k]) == tuple:
                Error.Log(f"{t}formating object","Log.txt")
                st += f"\n{t}"
                st += py_obj(o,lvl+1)
            elif type(o) == str:
                Error.Log(f"{t}formating str","Log.txt")
                st += py_str(o)
            else:
                Error.Log(f"{t}formating other","Log.txt")
                st += str(o)
            st += ","
        st = st[:-1]
        st += ")"
        return st
    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","py_obj",
                           f"filed to format to object",e],"Functions")

def py_str(st):
    try:
        return f"'{st}'"
    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","py_str",
                           f"filed to format to string",e],"Functions")





if __name__=="__main__":
    with io.open("test.py", 'w', encoding='utf-8') as py:
         py.write(py_obj(('hima',23,True,{'s':'hima','i':23,'b':True})))
         py.write("\n")
         py.write("\n")
         py.write(py_dct({'s':'hima','i':23,'b':True,'l':[2,{"6":8},5],
                          "o":(9,'g',2)}))
         py.write("\n")
         py.write("\n")
         py.write(py_lst(['hima',23,True,{'s':'hima','i':23,'b':True}]))










