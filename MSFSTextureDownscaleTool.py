from tkinter import *
from tkinter import messagebox, filedialog, ttk
from PIL import Image
import os

VERSION = "v1.1"

# Function to find textures from selected directory
def find_textures(folder):
    images = []
    for dir, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".dds"):
                try:
                    filepath = os.path.join(dir, file)
                    with Image.open(filepath) as image:
                        images.append((filepath, image.size))
                except Exception as e:
                    print(f"Error reading {file}: {e}")
    return images

class TextureResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"MSFS Texture Downscale Tool ({VERSION})")
        self.root.geometry("500x405")
        self.root.resizable(False, False)
        
        self.folder_path = StringVar()
        self.textures = []
        
        # Heading labels
        frame = Frame(root)
        frame.pack(pady=10)
        Label(frame, text=f"MSFS Texture Downscale Tool ({VERSION})", font=("Helvetica", 16, "bold")).pack()
        Label(frame, text="Publisher: aaMasih    |    Coded by Creepcomp", font=("Helvetica", 8)).pack()
        
        # Folder selection
        frame = Frame(root)
        frame.pack(pady=(0, 5))
        
        self.folder_entry = Entry(frame, textvariable=self.folder_path, width=40, state="readonly")
        self.folder_entry.pack(side=LEFT, padx=1)
        
        browse_button = Button(frame, text="Browse", command=self.browse_folder)
        browse_button.pack(side=LEFT, padx=1)
        
        scan_button = Button(frame, text="Scan", width=15, command=self.scan_textures)
        scan_button.pack(side=LEFT, padx=1)
        
        clear_button = Button(frame, text="Clear", command=self.clear_textures)
        clear_button.pack(side=LEFT)
        
        # Treeview for textures
        columns = ("Name", "Resolution")
        self.textures_tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
        self.textures_tree.heading("Name", text="Name")
        self.textures_tree.heading("Resolution", text="Resolution")
        self.textures_tree.column("Name", width=300)
        self.textures_tree.column("Resolution", width=150)
        self.textures_tree.pack(pady=(0, 5))
        
        # Progress bar
        self.progress = ttk.Progressbar(root, length=450, mode='determinate')
        self.progress.pack()
        
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
        
        self.textures = find_textures(folder)
        self.textures_tree.delete(*self.textures_tree.get_children())
        
        for index, (filepath, size) in enumerate(self.textures):
            texture_name = os.path.basename(filepath)
            texture_size = f"{size[0]}x{size[1]} ({max(size[0], size[1]) // 1024}K)"
            self.textures_tree.insert("", index, values=(texture_name, texture_size))
    
    def clear_textures(self):
        self.textures = []
        self.textures_tree.delete(*self.textures_tree.get_children())
    
    def process_textures(self):
        if not self.textures:
            messagebox.showwarning("Warning", "No textures to process!")
            return
        
        total_textures = len(self.textures)
        self.progress["value"] = 0
        self.progress["maximum"] = total_textures
        
        textures_tree_items = self.textures_tree.get_children()
        
        for index, (filepath, _) in enumerate(self.textures):
            self.progress["value"] = index
            self.progress.update()
            image = self.downscale_texture(filepath)
            texture_name = os.path.basename(filepath)
            texture_size = f"{image.width}x{image.height} ({max(image.width, image.height) // 1024}K)"
            self.textures_tree.item(textures_tree_items[index], values=(texture_name, texture_size))
        
        messagebox.showinfo("Success", "All textures have been successfully downscaled to 4K.")
    
    @staticmethod
    def downscale_texture(filepath, target_resolution=4096):
        """
        Downscale the texture to a maximum resolution, while preserving important details.
        
        :param filepath: Path to the texture file.
        :param target_resolution: The desired resolution for smaller textures.
                                Larger textures may retain higher resolutions.
        """
        try:
            with Image.open(filepath) as image:
                # Determine the maximum allowable resolution
                max_resolution = max(image.width, image.height)
                min_resolution = target_resolution
                
                # Set adaptive resolution thresholds
                if max_resolution > 32768:  # If 32K or higher, downscale to 16K
                    min_resolution = 16384
                elif max_resolution > 16384:  # If 16K or higher, downscale to 8K
                    min_resolution = 8192
                
                # Gradually downscale the image
                while max(image.width, image.height) > min_resolution:
                    width = round(image.width / 2)
                    height = round(image.height / 2)
                    image = image.resize((width, height))
                
                # Save the updated image
                image.save(filepath)
                return image
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

# Running the Tkinter application
if __name__ == "__main__":
    root = Tk()
    app = TextureResizerApp(root)
    root.mainloop()
