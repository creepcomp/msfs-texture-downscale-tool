# Changelog

## v1.1 (November 2024)

### New Features:
- **Adaptive Resolution Handling:** Textures larger than 32K are now downscaled to 16K, and textures between 16K and 8K are downscaled to 8K before resizing to the target resolution.
- **Clear Button:** Added a button to clear the list of textures and reset the application state.
  
### Improvements:
- **Texture Listing:** The texture list now includes additional details such as the resolution in "width x height" format and approximate file size in KB.
- **UI Enhancements:** Improved the GUI layout for better usability, especially with the treeview and progress bar.
  
### Bug Fixes:
- **Error Handling:** Improved error handling during texture processing. The application will print error messages if it fails to read a texture and proceed without crashing.