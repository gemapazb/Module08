import tkinter as tk

#creating main window 

window= tk.Tk()
window.title("Locator V1.0")
window.configure(background="dark turquoise")
#creating window for BHV & OV Locations

def open():


    win2 = tk.Toplevel()
    win2_label = tk.Label(win2, text="OV/BHV Available Locations ").pack()
    win2_label = tk.Label(win2, text=" Enter skids to Locate then select stacking").pack()
    win2.geometry("300x300")
    win2.configure(background="pink")

    skids= tk.Entry(win2, width=5)
    skids.pack()

    S_S= tk.Button(win2,text='Single stack')
    S_S.pack(side=tk.TOP)

    D_S= tk.Button(win2,text='Double stack')
    D_S.pack(side=tk.TOP)

    T_S= tk.Button(win2,text='Triple stack')
    T_S.pack(side=tk.TOP)

    #Label Results
    Results= tk.Label(win2,text="you need  ")
    Results.pack()
    #output Results 
    skids= tk.Label(win2)
    skids.pack()


    start_over= tk.Button(win2,text='Start Over', command=window)
    start_over.pack(side=tk.TOP)

    
#adjusting size of main Window
window.geometry("300x300")
#creatring 1st label 
label_1=tk.Label(text="Welcome to Locator 2022")
label_1.pack(padx=60, pady=60)
label_1.pack()

#framing the buttons/menu main window
frame= tk.Frame(window)
frame.pack(side=tk.TOP)
bottom_frame= tk.Frame(window)
bottom_frame.pack(side=tk.TOP)

#creating 1st button /main window
OV_BHVbtn= tk.Button(frame, text='Click to Locate OV/BHV', command=open)
OV_BHVbtn.pack(side=tk.TOP)

#creating 2nd Button/main window
BNC_btn = tk.Button(bottom_frame, text='CLick to locate BNC',command=open)
BNC_btn.pack(side=tk.TOP)



window.mainloop()