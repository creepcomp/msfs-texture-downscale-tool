# MSFS Texture Downscale Tool (v1.1)

## Overview

The **MSFS Texture Downscale Tool** is a Python-based graphical user interface (GUI) tool designed to help Microsoft Flight Simulator (MSFS) addon creators and users easily manage and downscale high-resolution `.dds` textures. The tool detects large textures (above 8K resolution) and allows you to resize them to a target resolution (default 4K) for better performance and compatibility with MSFS.

Version: **v1.1**

---

## Features

- **Graphical User Interface (GUI):** Simple and intuitive interface built with Tkinter.
- **Texture Detection & Listing:** Automatically scans selected directories for `.dds` textures and displays them in a table with their name and resolution.
- **Texture Downscaling:** Resizes high-resolution textures to a manageable size (4K or lower) while preserving important details.
- **Adaptive Resolution Handling:** Handles textures above 32K by scaling down to 16K and textures between 16K and 8K by scaling to 8K, before downscaling to 4K.
- **Progress Tracking:** Displays progress via a progress bar during texture processing.
- **Folder Selection & Scanning:** Easy folder selection to locate textures and scan them efficiently.
- **Clear Button:** Clears the list of textures and resets the state.
- **Error Handling:** Handles errors while reading or processing files and shows informative messages.

---

## Prerequisites

1. **Python:** Python 3.8+ is required.
2. **Dependencies:** Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. **Tkinter:** Tkinter is typically included with Python but can be installed separately on some systems (e.g., `sudo apt-get install python3-tk` on Ubuntu).

---

## Installation

1. Clone or download the repository:
   ```bash
   git clone https://github.com/your-username/msfs-texture-downscale-tool.git
   cd msfs-texture-downscale-tool
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the tool:
   ```bash
   python MSFSTextureDownscaleTool.py
   ```

---

## Build via Nuitka
1. Install required "nuitka" library.
    ```bash
    pip install nuitka
    ```
2. Build it via this command.
    ```bash
    nuitka.exe .\MSFSTextureDownscaleTool.py --windows-icon-from-ico=.\icon.ico --enable-plugin=tk-inter --windows-console-mode=disable --standalone --output-dir=output/v1.1
    ```

---

## Usage

1. **Select Folder:** Use the **Browse** button to choose the directory containing your `.dds` textures.
2. **Scan Textures:** Click **Scan** to list all the textures found in the selected folder.
3. **Clear List:** Click **Clear** to remove all the textures from the list.
4. **Process Textures:** Click **Process** to start downscaling. The progress bar will update during processing.
5. **Completion:** Once all textures have been processed, a success message will appear.

---

## Changelog

### v1.1 (Release Date: November 2024)
- **New Feature:** Adaptive downscaling logic for ultra-high-resolution textures (32K and 16K) to 16K and 8K before resizing to 4K.
- **New Feature:** Added a clear button to reset the texture list.
- **Improvement:** Added resolution info in the texture listing, including file size in KB.
- **UI Update:** Improved layout for better user experience.
- **Bug Fix:** Enhanced error handling for reading and processing textures.
- **Other:** Updated to handle larger texture files more efficiently.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Credits

- **Publisher:** aaMasih
- **Developer:** Creepcomp

Thank you for using the **MSFS Texture Downscale Tool**! 🎉

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.