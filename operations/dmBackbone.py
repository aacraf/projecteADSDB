### Main

from landing.landing import executeLanding
from landing.landing import Wrapper

from formatted.formatted import executeformatted
from formatted.formmated_infodb import describeFormattedDB

from trusted.combine_versions import execute_combine_versions
from trusted.data_quality.missing import executeMissingData
from trusted.data_quality.outliers import execute_outliers
from trusted.data_quality.profiling import execute_profiling
from trusted.trusted_infodb import describeTrustedDB

from explotation.explotation import execute_explotation
from explotation.tablepivoting import execute_tablepivoting
from explotation.dataintegration import execute_dataIntegration
from explotation.explotation_infodb import describeExplotationDB

import os
import shutil
import webbrowser

""" from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
 """
# Landing

""" import tkinter as tk
from tkinter import filedialog
import os
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window 
my_w.title("DMBackbone")  #  title
my_dir='' # string to hold directory path 
def my_fun(): 
    path = filedialog.askdirectory() # select directory 
    l1.config(text=path) # update the text of Label with directory path
    root=next(os.walk(path))[0] # path 
    dirnames=next(os.walk(path))[1] # list of directories 
    files=next(os.walk(path))[2] # list of files 
    print(root) # D:\my_dir\my_dir0
    print(dirnames) # ['my_dir1']
    print(files) # ['my_file0.txt']
    for item in trv.get_children():
        trv.delete(item)
    i=1
    f2i=1 #sub directory id 
    for d in dirnames:
        trv.insert("", 'end',iid=i,values =d)
        path2=path+'/'+d # Path for sub directory 
        #print(path2)
        files2=next(os.walk(path2))[2] # file list of Sub directory 
        for f2 in files2:  # list of files 
            #print(f2)
            trv.insert(i, 'end',iid='sub'+str(f2i),values ="-" + f2)
            f2i=f2i+1
        i=i+1

    for f in files:  # list of files 
        trv.insert("", 'end',iid=i,values =f)
        i=i+1

b1=tk.Button(my_w,text='Select directory',font=22,
    command=lambda:my_fun(),bg='lightgreen')
b1.grid(row=0,column=0,padx=5,pady=10)

l1=tk.Label(my_w,text=my_dir,bg='yellow',font=16)
l1.grid(row=0,column=1,padx=0)

trv=ttk.Treeview(my_w,selectmode='browse',height=9)
trv.grid(row=1,column=0,columnspan=2,padx=10,pady=5)
trv["columns"]=("1")
trv['show']='tree headings'
trv.column("#0", width = 20, anchor ='c')
trv.column("1",width=300,anchor='w')
trv.heading("#0", text ="#")
trv.heading("1",text="Name",anchor='w')

my_w.mainloop()  # Keep the window open """

### Execute

print(r"""\

________          __                 _____                                                      __    
\______ \ _____ _/  |______         /     \ _____    ____ _____     ____   _____   ____   _____/  |_  
 |    |  \\__  \\   __\__  \       /  \ /  \\__  \  /    \\__  \   / ___\ /     \_/ __ \ /    \   __\ 
 |    `   \/ __ \|  |  / __ \_    /    Y    \/ __ \|   |  \/ __ \_/ /_/  >  Y Y  \  ___/|   |  \  |   
/_______  (____  /__| (____  /    \____|__  (____  /___|  (____  /\___  /|__|_|  /\___  >___|  /__|   
        \/     \/          \/             \/     \/     \/     \//_____/       \/     \/     \/       
   __________                __   ___.                                                                
   \______   \_____    ____ |  | _\_ |__   ____   ____   ____                                         
    |    |  _/\__  \ _/ ___\|  |/ /| __ \ /  _ \ /    \_/ __ \                                        
    |    |   \ / __ \\  \___|    < | \_\ (  <_> )   |  \  ___/                                        
    |______  /(____  /\___  >__|_ \|___  /\____/|___|  /\___  >                                       
           \/      \/     \/     \/    \/            \/     \/                                        
                                                                                                      
                                                                             Authors: Achraf Hmimou & 
                                                                                        Aniol Bisquert
                """)

print("Please, select an option:")
print("1. Add new datasource to DMBackbone")
print("2. Execute DMBackbone")
print("3. Get database tables")
print("4. Get profiling reports")
print("5. Reset the DMBackbone")
print("7. Exit")

print("\nSelect a option 1-7: ")

dirname = os.path.dirname(__file__)

option = input()
while int(option) != 7: 
    if int(option) == 1:
        
        print("Please introduce the path of the new datasource (extension .csv): ")
        nds_path = input()
        if os.path.exists(nds_path): 
            wrapper = Wrapper()
            wrapper.addNewDatasource(nds_path)
        else:
            print("Invalid datasource. Please, introduce a valid datasource.")
    elif int(option) == 2:
        
        print("Executing Landing Zone....")
        executeLanding()
        print("Done!")
        #Formatted
        print("Executing Formatted Zone....")
        executeformatted()
        print("Done!")
        #describeFormattedDB()

        # Trusted
        print("Executing Trusted Zone....")
        execute_combine_versions()
        executeMissingData()
        execute_outliers()
        print("Done!")
        #describeTrustedDB()
        #execute_profiling()

        #explotation
        print("Executing Exploitation Zone...")
        execute_explotation()
        execute_tablepivoting()
        execute_dataIntegration()
        print("Done!")
        print("DMBackbone is up to date! :-)")
        #describeExplotationDB()
        
    elif int(option) == 3:
        
        print("Select a zone: ")
        print("1. formatted")
        print("2. trusted")
        print("3. explotation")
        zone = input()
        if int(zone) == 1:
            describeFormattedDB()
        elif int(zone) == 2:
            describeTrustedDB()
        elif int(zone) == 3:
            describeExplotationDB()
        else:
            print("Please indicate a valid zone.")
        
    elif int(option) == 4:
        execute_profiling()
        
        for report in os.listdir(os.path.join(dirname, 'trusted/data_quality/profile_reports')):
            webbrowser.open(os.path.join(dirname, f'trusted/data_quality/profile_reports/{report}'), new=0, autoraise=True)
        
        
    elif int(option) == 5:
        
        print("Cleaning landing zone...")
        if os.path.exists((os.path.join(dirname, 'landing/persistent'))):
            shutil.rmtree((os.path.join(dirname, 'landing/persistent')))
            os.remove((os.path.join(dirname, 'landing/wrapper.json')))
        print("Done!")
        
        print("Cleaning formatted zone...")
        if os.path.exists((os.path.join(dirname, 'formatted/formatted.duckdb'))):
            os.remove((os.path.join(dirname, 'formatted/formatted.duckdb')))
        print("Done!")
        
        print("Cleaning trusted zone...")
        if os.path.exists((os.path.join(dirname, 'trusted/trusted.duckdb'))):
            os.remove((os.path.join(dirname, 'trusted/trusted.duckdb')))
        if os.path.exists((os.path.join(dirname, 'trusted/profile_reports'))):
            shutil.rmtree((os.path.join(dirname, 'trusted/profile_reports')))
        print("Done!")

        print("Cleaning exploitation zone...")
        if os.path.exists((os.path.join(dirname, 'trusted/profile_reports'))):
            os.remove((os.path.join(dirname, 'trusted/profile_reports')))
        
        print("DMBackbone has been cleaned!")

    else:
        print("Please, select a valid option")
    
    print("\n\n\n1. Add new datasource to DMBackbone")
    print("2. Execute DMBackbone")
    print("3. Get database tables")
    print("4. Get profiling reports")
    print("5. Reset the DMBackbone")
    print("7. Exit")
    print("\nSelect a option 1-7: ")
    option = input()

