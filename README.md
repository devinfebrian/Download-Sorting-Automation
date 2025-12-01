# Download-Sorting-Automation
Day 1 Learning Python by Project

I'm creating automation scripts using Python to sort my download folder.

A simple Python utility that automatically organizes files in your Downloads folder by file type.

## Overview

This script scans your Downloads folder and sorts files into categorized subdirectories based on their file extensions. It helps keep your Downloads folder clean and organized with minimal effort.

## Features

- **Automatic File Sorting** - Categorizes files by type (images, videos, documents, code, etc.)
- **Cross-Platform** - Works on Windows, macOS, and Linux using universal path handling
- **Safe Handling** - Skips existing category folders and provides detailed error reporting
- **Console Feedback** - Shows real-time progress and sorting statistics

## Supported File Categories

The script organizes files into the following categories:

- **_Images** - `.jpg`, `.jpeg`, `.png`
- **_GIF** - `.gif`
- **_Videos** - `.mp4`, `.mkv`, `.avi`, `.mov`
- **_Audios** - `.mp3`, `.m4a`
- **_Docs** - `.pdf`, `.docx`, `.txt`, `.pptx`
- **_ZIPs** - `.zip`, `.rar`, `.7z`
- **_Installer** - `.exe`, `.msi`
- **_Code** - `.py`, `.js`, `.html`, `.css`, `.md`, `.jsx`, `.ipynb`
- **_Data** - `.csv`, `.xlsx`, `.sql`
- **_Design** - `.fig`, `.psd`, `.svg`
- **_Folders** - Existing folders (moved to `_Folders`)
- **_Others** - Unsupported file types

## Usage

1. Clone or download this repository
2. Run executable file (.exe) that i generate using pyinstaller

## How It Works

1. Scans all files in your Downloads folder
2. Ignores existing category folders (those starting with `_`)
3. For each file, determines its category based on file extension
4. Creates category subdirectories as needed
5. Moves files to their corresponding folders
6. Reports results and any errors to the console

## Notes

- Folders in your Downloads directory are moved to the `_Folders` category
- Files with unsupported extensions are placed in `_Others`
- Already-sorted files (in folders starting with `_`) are skipped
- Duplicate file names in destination folders will trigger an error (file will remain in Downloads)

## Contributing

Feel free to modify the `CATEGORIES` dictionary to add support for additional file types or create new sorting categories.
