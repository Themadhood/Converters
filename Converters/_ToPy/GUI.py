__Program__     = "Converters._ToPy.GUI"    
__programer__   = "Madison Arndt"
__Date__        = "2/29/2024"
__version__     = "0.0.1"
__update__      = ""
__info__        = ""

_BG = "Black"
_FG = "green"

import Error
os = Error.os

#import tkinter files used
import tkinter  as tk
from tkinter import messagebox
from tkinter import filedialog as fd

try:
    from .PicToPy import PicToPy
    from .Mp3ToPy import Mp3ToPy
except:
    from PicToPy import PicToPy
    from Mp3ToPy import Mp3ToPy


#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")

class PicToPy_GUI(_GUI):
    def __init__(self,**args):
        _GUI.__init__(self,**args)
        self.topyAPI = PicToPy
        self.extentions = [('png files', '*.png'),('jpeg files', '*.jpeg')]

class Mp3ToPy_GUI(_GUI):
    def __init__(self,**args):
        _GUI.__init__(self,**args)
        self.topyAPI = Mp3ToPy
        self.extentions = [('mp3 files', '*.mp3')]




class _GUI(tk.Frame):
    saveFilePath = None
    topyAPI = None
    extentions = None


    def __init__(self,parent,fg=_FG,bg=_BG,error=False,
                 *args,**kw):
        tk.Frame.__init__(self,parent,bg=bg,*args,**kw)
        self._Error = error

        #lst box of paths
        self.lstOfPathsToOpen = []
        self.lstOfPathslst = tk.Listbox(self,bg = bg,fg = fg,
                                     font = ('timesnewroman 9 bold'),
                      #height = _LISTBOXHIGHT,width = _LISTBOXWITH,
                      yscrollcommand = True,selectmode = "BROWSE",
                      selectbackground = bg,
                      highlightbackground=fg,highlightcolor=fg)
        self.lstOfPathslst.grid(row=1,column=1,rowspan=4,sticky="nesw")

        
        #event and binding to def
        self.lstOfPathslst.bind("<Double-Button-1>", self.RemoveSelectedItem)
        self.lstOfPathslst.event_generate("<<ListboxSelect>>")


        #file path btn
        tk.Button(self,bg = fg,fg = bg,text = "select files to open",
                  font = (f'timesnewroman 9 bold'),
                  command=self.SelectFileOpen).grid(row=1,column=2,
                                                    columnspan=2,sticky="we")
        #save path btn
        tk.Button(self,bg = fg,fg = bg,text = "Save as",
                  font = (f'timesnewroman 9 bold'),
                  command=self.SelectFileSave).grid(row=3,column=2,
                                                    columnspan=2,sticky="we")

        #write over file
        tk.Label(self,bg = bg,fg = fg,font=(f'timesnewroman 9 bold'),
              text = "write over .py file").grid(row=2,column=3,sticky="w")

        self.Write = tk.BooleanVar()
        tk.Checkbutton(self,bg=bg,fg=fg,variable=self.Write,onvalue=True,
                    selectcolor=bg,cursor="crosshair",
                    offvalue=False).grid(row = 2,column=2,sticky="we")
        

        """
        Show running text
        way to remove (1 - many) selected paths from lst
        """
##################################################################################
############################### list box defs ####################################
##################################################################################
        
    def RemoveSelectedItem(self, event):
        try:
            item = event.widget.get(event.widget.curselection()[0])
            self.RemoveItem(item)
            self.lstOfPathslst.selection_clear(0, "end")
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([__Program__,__version__,"class","def",
                                        f"mesage",e],"Functions")

    def RemoveItem(self, item):
        try:
            index = self.lstOfPathslst.get(0, "end").index(item)
            self.lstOfPathslst.delete(index)
            self.lstOfPathsToOpen.pop(index)
            self.lstOfPathslst.selection_clear(0, "end")
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([__Program__,__version__,"class","def",
                                        f"mesage",e],"Functions")

    def AddToLst(self,item):
        try:
            self.lstOfPathslst.insert("end", item)
            self.lstOfPathslst.selection_clear(0, "end")
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([__Program__,__version__,"class","def",
                                        f"mesage",e],"Functions")


##################################################################################
##################################################################################
##################################################################################
    
    def PicToPy(self,path=None):
        try:
            #if open path is tuple do all paths
            if path==None:
                while self.lstOfPathsToOpen > []:
                    self.PicToPy(self.lstOfPathsToOpen[0])
                    
                #reset
                self.saveFilePath = None
                self.lstOfPathslst.selection_clear(0, "end")
                messagebox.showwarning('info','Done!')
                return
            
            if self.Write.get():
                write = "w"
            else:
                write = "a"
            
            directoryO, nameO, extentionO = self.SplitFilePath(path)
            directoryS, nameS, extentionS = self.SplitFilePath(self.saveFilePath)
            
            self.topyAPI(fileName=nameO,fileExtention=extentionO,FromPath=directoryO,
                    ToPath=directoryS,toFileName=nameS,VarName=None,cama=False,
                    write=write,dct=False)
            
            self.Write.set(False)
            self.RemoveItem(nameO)
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([__Program__,__version__,"class","def",
                                        f"mesage",e],"Functions")

    def SelectFileOpen(self):
        try:
            openfilePath = fd.askopenfilenames(filetypes=self.extentions)
            if openfilePath == "":
                openfilePath = None
            else:
                if type(openfilePath) == tuple:
                    for path in openfilePath:
                        self.lstOfPathsToOpen.append(path)
                        name = os.path.splitext(os.path.basename(path))[0]
                        self.AddToLst(name)
                else:
                    self.lstOfPathsToOpen.append(openfilePath)
                    name = os.path.splitext(os.path.basename(path))[0]
                    self.AddToLst(name)
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([__Program__,__version__,"class","def",
                                        f"mesage",e],"Functions")
            

    def SelectFileSave(self):
        try:
            if self.lstOfPathsToOpen == []:
                messagebox.showwarning('warning',
                                       'you must select a file to open First')
                return
            
            self.saveFilePath = fd.asksaveasfilename(filetypes=[('Python Files', '*.py')],
                                                     title="Save .py",
                                                     confirmoverwrite=self.Write.get())
            
            self.PicToPy()
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([__Program__,__version__,"class","def",
                                        f"mesage",e],"Functions")

    def SplitFilePath(self,filePath):
        try:
            name, extention = os.path.splitext(os.path.basename(filePath))
            directory = os.path.dirname(filePath)

            return directory, name, extention
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([__Program__,__version__,"class","def",
                                        f"mesage",e],"Functions")



"""
with PicToPy.io.open(f"{_FP}/Graphics.py", "w", encoding='utf-8') as py:
        py.write("Avitar = {")
        py.close()
cama = True
for fileName in graphics:
    if fileName.endswith(fileExtention):
        fileName = fileName.removesuffix(fileExtention)
        print(writetype,fileName)
        #(fileName,fileExtention,FromPath,ToPath=None,toFileName=None,
        #VarName=None,write="a")
        PicToPy.PicToPy(fileName,fileExtention,f"{_FP}/Avitar",_FP,"Graphics",
                        fileName,cama)

with PicToPy.io.open(f"{_FP}/Graphics.py", "a", encoding='utf-8') as py:
        py.write("'':''}")
        py.close()#"""




if __name__ == "__main__":
    root = tk.Tk()
    gui = PicToPy_GUI(root,error=True)
    gui.pack(fill="both",expand=True)
















