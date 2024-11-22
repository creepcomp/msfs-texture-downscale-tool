# MSFS Texture Downscale Tool (v1.0)

## Overview

The **MSFS Texture Downscale Tool** is a Python-based graphical application designed to simplify the process of downscaling high-resolution `.dds` textures used in Microsoft Flight Simulator (MSFS) addons. This tool automatically detects textures larger than or equal to `8192x8192` resolution and downsizes them to a maximum resolution of `4096x4096` using bilinear resizing.

---

## Features

- **Graphical User Interface (GUI):**
  - User-friendly interface built with Tkinter.
- **Texture Detection:**
  - Automatically scans for `.dds` textures exceeding `8192x8192` in the selected folder.
- **Batch Processing:**
  - Processes multiple textures using multiprocessing for efficiency.
- **Progress Feedback:**
  - Includes a progress bar to show the processing status.
- **Safety:**
  - Skips invalid or corrupted `.dds` files to prevent crashes.

---

## Prerequisites

1. **Python:** Ensure Python 3.8+ is installed.
2. **Dependencies:** Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. **Tkinter:** Comes pre-installed with most Python distributions. If not, install it via your package manager (e.g., `sudo apt-get install python3-tk` on Ubuntu).

---

## Installation

1. Clone or download the repository:
   ```bash
   git clone https://github.com/creepcomp/msfs-texture-downscale-tool.git
   cd msfs-texture-downscale-tool
   ```
2. Install dependencies as listed above.

---

## Build via Nuitka
1. Install required "nuitka" library.
    ```bash
    pip install nuitka
    ```
2. Build it via this command.
    ```bash
    nuitka.exe .\MSFSTextureDownscaleTool.py --windows-icon-from-ico=.\icon.ico --enable-plugin=tk-inter --windows-console-mode=disable --standalone --output-dir=output/v1.0
    ```

---

## Usage

1. Run the tool:
   ```bash
   python MSFSTextureDownscaleTool.py
   ```
2. **Select Folder:**
   - Use the **Browse** button to choose the directory containing `.dds` textures.
3. **Scan for Textures:**
   - Click **Scan for Textures** to list all high-resolution `.dds` textures.
4. **Process Textures:**
   - Click **Process** to begin downscaling. The progress bar will indicate the status.
5. **Completion:**
   - Upon completion, a message box will notify that all textures have been processed.

---

## Notes

- Ensure you have adequate storage and backup for your textures before processing.
- The tool modifies textures in place. If you need original textures, make backups prior to using the tool.

---

## Contribution

If you would like to contribute, feel free to fork the repository and submit a pull request. Suggestions, bug reports, and feature requests are also welcome!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Credits

- **Publisher:** aaMasih
- **Developer:** Creepcomp

Thank you for using the **MSFS Texture Downscale Tool**! 🎉