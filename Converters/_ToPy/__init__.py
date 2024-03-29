#program:       _ToPy.__init__
#purpose:       turn a dictonary to a .py file
#progamer:      Themadhood Pequot 5/30/2023

_FILE = "Converters._ToPy.__init__"
_VERSION = "0.0.1"

try:
    from .pyFormats import *
    from .GUI import *
except:
    from pyFormats import *
    from GUI import *

def Dct_lst_dctToPy(dct,path,pre=None,post=None,writetype="w"):
    try:
        if not Error.os.path.isfile(f"{path}.py"):
            Error.os.makedirs(Error.os.path.dirname(path), exist_ok=True)
    except:
        pass
    try:
        st = Error.time.time()
        lst=list(dct)
        Error.Log(f"\nwriting: {writetype} to file: {path}.py","Log.txt")
        with io.open(path+".py", writetype, encoding='utf-8') as py:
            if type(pre)==str:
                py.write(f"{pre}\n\n")
            py.write("dct={")
            while lst > []:
                key = lst.pop(0)
                py.write(f"'{key}':[\n")
                keyset = dct[key].copy()
                while keyset > []:
                    py.write(f"{keyset.pop(0)}")
                    if keyset > []:
                        py.write(",\n")
                if lst > []:
                    py.write("],\n")
                else:
                    py.write("]}\n\n")
            if type(post)==str:
                py.write(f"{post}")
            py.close()
        Error.Log(f"runtime: {Error.LenTime(st)}\n","Log.txt")
    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","Dct_lst_dctToPy",
                                    f"filed to write py",e],"Functions")
        Error.Log(f"\nError ocurred: {e}","Log.txt")



if __name__=="__main__":
    dct = {"abc":[{"A":1,"B":2,"C":3},
                  {"A":2,"B":2,"C":3},
                  {"A":3,"B":2,"C":3}],
           "def":[{"d":1,"e":2,"f":3},
                  {"d":2,"e":2,"f":3},
                  {"d":3,"e":2,"f":3}]}



