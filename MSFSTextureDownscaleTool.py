import os
import multiprocessing
from tkinter import *
from tkinter import messagebox, filedialog, ttk
from PIL import Image

max_processor_count = 5

# Function to get textures from selected directory
def get_textures(folder):
    images = []
    for dir, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".dds"):
                try:
                    with Image.open(f"{dir}/{file}") as image:
                        if image.width >= 8192 or image.height >= 8192:
                            images.append(image.filename)
                except:
                    pass
    return images

# Function to downscale images
def process_image(filepath):
    try:
        with Image.open(filepath) as image:
            while image.width >= 8192 or image.height >= 8192:
                width = round(image.width / 2)
                height = round(image.height / 2)
                image = image.resize((width, height))
            image.save(filepath)
    except:
        pass

class TextureResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MSFS Texture Downscale Tool (v1.0)")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        self.folder_path = StringVar()
        self.textures = []
        
        # Heading label
        Label(root, text="MSFS Texture Downscale Tool", font=("Helvetica", 16, "bold")).pack(pady=10)
        Label(root, text="Publisher: aaMasih    |   Coded by Creepcomp", font=("Helvetica", 8)).pack()
        
        # Folder selection
        frame = Frame(root)
        frame.pack(pady=10)
        
        self.folder_entry = Entry(frame, textvariable=self.folder_path, width=40, state="readonly")
        self.folder_entry.pack(side=LEFT, padx=5)
        
        browse_button = Button(frame, text="Browse", command=self.browse_folder)
        browse_button.pack(side=LEFT)
        
        scan_button = Button(frame, text="Scan for Textures", command=self.scan_textures)
        scan_button.pack(side=LEFT, padx=10)
        
        # Textures listbox
        self.textures_list = Listbox(root, width=80, height=10)
        self.textures_list.pack(padx=10, pady=10)
        
        # Progress bar
        self.progress = ttk.Progressbar(root, length=500, mode='determinate')
        self.progress.pack(pady=10)
        
        # Buttons for processing
        process_button = Button(root, text="Process", command=self.process_textures, width=25)
        process_button.pack(pady=10)
        
    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)
    
    def scan_textures(self):
        folder = self.folder_path.get()
        if not folder:
            messagebox.showwarning("Warning", "Please select a folder first!")
            return
        
        self.textures = get_textures(folder)
        self.textures_list.delete(0, END)
        
        if not self.textures:
            messagebox.showinfo("Info", "No high-resolution textures found.")
        else:
            for texture in self.textures:
                self.textures_list.insert(END, os.path.basename(texture))
    
    def process_textures(self):
        if not self.textures:
            messagebox.showwarning("Warning", "No textures to process!")
            return
        
        total_textures = len(self.textures)
        self.progress["value"] = 0
        self.progress["maximum"] = total_textures
        
        processes = []
        
        # Multiprocessing to process images
        for index, texture in enumerate(self.textures):
            self.progress["value"] = index + 1
            self.progress.update()
            
            process = multiprocessing.Process(target=process_image, args=(texture,))
            process.start()
            processes.append(process)
            
            if len(processes) >= max_processor_count:
                for process in processes:
                    process.join()
                processes = []
        
        for process in processes:
            process.join()
        
        messagebox.showinfo("Success", "All textures have been successfully downscaled to 4K.")

# Running the Tkinter application
if __name__ == "__main__":
    root = Tk()
    app = TextureResizerApp(root)
    root.mainloop()
