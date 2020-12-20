from tkinter import *
from tkinter import filedialog
from tkinter import font


root = Tk()
root.title('Voice Controlled Text Editor')
root.geometry("1200x660")


#inititalising open status name to access when needed
global open_status_name      # last updated on: 5th December by Mahi
open_status_name = FALSE  
    
global selected_text
selected_text = FALSE


#Create NEW FILE function in file menu
def new_file():                      # last updated on: 9th December by Om
    #delete previous text
    my_text.delete("1.0", END)
    root.title("New File - Voice Controlled Text Editor")
    status_bar.config(text = "New File")
    global open_status_name
    open_status_name = FALSE

#Create OPEN_FILE function in file menu
def open_file():                    # last updated on: 9th December by Om
    #delete previous text
    my_text.delete("1.0", END)
    
    # Grab Filename
    text_file = filedialog.askopenfilename(title = "Open File", filetypes = (("Text Files","*txt"),("HTML Files","*.html"),("Äll Files","*.*")) )
    
    # set an open status
    if text_file:
        global open_status_name
        open_status_name = text_file
                
        
    #Update status and tile bars
    name = text_file
    #name.replace
    root.title(f'{name} - Voice context editor')
    status_bar.config(text = f'{name}         ')
    
    #open this file, add content to the workspace, close file
    text_file = open(text_file,'r')
    file_content = text_file.read()
    my_text.insert(END,file_content)
    text_file.close()

#Save As File Function
def save_as_file():               # last updated on: 8th December by Harsh
    
    text_file = filedialog.asksaveasfilename(defaultextension = ".*", initialdir = "C:/Voice Context Editor/", filetypes = (("Text Files",".txt"),("HTML Files",".html"),("Äll Files",".*")))
    
    if text_file:
        #update status and title bars
        name = text_file
        name = name.replace("C:/Voice Context Editor/","")
        root.title(f'{name} - Voice context editor')
        status_bar.config(text = f'Saved: {name}         ')
        
        #Open, Save and Close file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0,END))
        text_file.close()
        
#Save File Function        
def save_file():               # last updated on: 8th December by Harsh
    global open_status_name
    if open_status_name:
        #Open, Save and Close file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0,END))
        text_file.close()
        
        #update status bar
        status_bar.config(text = f'Saved: {open_status_name}         ')
        
    else:
        save_as_file()

#Cut text
def cut_text(t):               # last updated on: 12th December by Mahi
    global selected_text
    
    #Check if keyboard shortcut is used
    if t:
        selected_text = root.clipboard_get()
    else:
        if my_text.selection_get():
            #save selected text into a variable
            selected_text = my_text.selection_get()
            #Delete selected text from the workspace
            my_text.delete("sel.first","sel.last")
            
            #Clear Clipboard then append
            root.clipboard_clear()
            root.clipboard_append(selected_text)
    
#Copy text
def copy_text(t):             # last updated on: 13th December by Mahi
    global selected_text
    
    #Check if keyboard shortcut is used
    if t:
        selected_text = root.clipboard_get()
    
    elif my_text.selection_get():
        #save selected text into a variable
        selected_text = my_text.selection_get()
        
        #Clear Clipboard then append
        root.clipboard_clear()
        root.clipboard_append(selected_text)

#Paste text
def paste_text(t):           # last updated on: 16th December by Om
    global selected_text
    
    #check if clipboard was used
    if t:
        selected_text = root.clipboard_get()
    else:
        if selected_text:
            cursor = my_text.index(INSERT)
            my_text.insert(cursor, selected_text)
            

#Bold it button
def bold_it():               # last updated on: 14th December by Harsh
    #Create our font
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight = "bold")

    #Configure a tag
    my_text.tag_configure("bold", font = bold_font)

    #Define current tag
    current_tags = my_text.tag_names("sel.first")
    
    #If statement to see if text is already bold
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")
    
#Italic button
def italic_it():            # last updated on: 15th December by Harsh
    #Create our font
    italic_font = font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant = "italic")

    #Configure a tag
    my_text.tag_configure("italic", font = italic_font)

    #Define current tag
    current_tags = my_text.tag_names("sel.first")
    
    #If statement to see if text is already bold
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")

#Underline button      
def underline_it():         # last updated on: 16th December by Om
    #Create our font
    underline_font = font.Font(my_text, my_text.cget("font"))
    underline_font.configure(underline = True)

    #Configure a tag
    my_text.tag_configure(True, font = underline_font)

    #Define current tag
    current_tags = my_text.tag_names("sel.first")
    
    #If statement to see if text is already bold
    if True in current_tags:
        my_text.tag_remove(True, "sel.first", "sel.last")
        my_text.tag_add(False, "sel.first", "sel.last")
    else:
        my_text.tag_add(True, "sel.first", "sel.last")
    
#create ToolBar
toolbar_frame = Frame(root)
toolbar_frame.pack(fill = X)
    
#create Mainframe
my_frame = Frame(root)
my_frame.pack(pady=5)

#create scroll bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side = RIGHT, fill = Y)

#create horizontal scroll bar
hor_scroll = Scrollbar(my_frame, orient = 'horizontal')
hor_scroll.pack(side = BOTTOM, fill = X)

#create Text Box
my_text = Text(my_frame, width = 105, height = 50, font = ("Helvetica"),selectbackground = "blue", selectforeground = "black", undo = TRUE, yscrollcommand = text_scroll.set, wrap ="none", xscrollcommand = hor_scroll.set)
my_text.pack()

#configure scrollbar
text_scroll.config(command=my_text.yview)
text_scroll.config(command=my_text.xview)


#create Menu
my_menu = Menu(root)
root.config(menu = my_menu)

#add file menu            # last updated on: 16th December by Om

file_menu = Menu(my_menu,tearoff = FALSE)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = new_file)
file_menu.add_command(label = "Open", command =  open_file)
file_menu.add_command(label = "Save", command = save_file)
file_menu.add_command(label = "Save As", command = save_as_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command=root.quit)


#add edit menu             # last updated on: 16th December by Harsh

edit_menu = Menu(my_menu,tearoff = FALSE)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut", command = lambda:cut_text(FALSE), accelerator = "(Ctrl+x)")
edit_menu.add_command(label = "Copy", command = lambda:copy_text(FALSE), accelerator = "(Ctrl+c)")
edit_menu.add_command(label = "Paste      ", command = lambda:paste_text(FALSE), accelerator = "(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label = "Undo", command = my_text.edit_undo, accelerator = "(Ctrl+z)")
edit_menu.add_command(label = "Redo", command = my_text.edit_redo, accelerator = "(Ctrl+y)")

# add status bar

status_bar = Label(root, text = 'Ready         ', anchor = E)
status_bar.pack(fill = X, side = BOTTOM, ipady = 5)

# edit key bindings
root.bind('<Control-Key-x>',cut_text)
root.bind('<Control-Key-c>',copy_text)
root.bind('<Control-Key-v>',paste_text)

#Adding buttons               # last updated on: 17th December by Mahi

#Bold button
bold_button = Button(toolbar_frame, text = "Bold", command = bold_it)
bold_button.grid(row = 0, column = 0, sticky = W, padx = 5)

#Italics button
italic_button = Button(toolbar_frame, text = "Italic", command = italic_it)
italic_button.grid(row = 0, column = 1, padx = 5)

#Underline button
underline_button = Button(toolbar_frame, text = "Underline", command = underline_it)
underline_button.grid(row = 0, column = 2,  padx = 5)

#Undo button
undo_button = Button(toolbar_frame, text = "Undo", command = my_text.edit_undo)
undo_button.grid(row = 0, column = 3, padx = 5)

#Redo button
redo_button = Button(toolbar_frame, text = "Redo", command = my_text.edit_redo)
redo_button.grid(row = 0, column = 4, padx = 5)


root.mainloop()
