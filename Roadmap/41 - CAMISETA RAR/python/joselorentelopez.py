"""
Owner: José Lorente López | joselorente1105@gmail.com | Linkedin: www.linkedin.com/in/josé-lorente-lópez-0121b7148

Description: Program capable of compressing a file to .zip format

Coding: UTF-8
"""

import os
import zipfile

class FileCompression():
    def __init__(self) -> None:
        """
        Initializes the FileCompression class, which is the parent class of the other
        compression classes. 

        Args:
            None

        Returns:
            None
        """
        pass

class ZipCompression(FileCompression):
    def __init__(self, file_path: str):
        """
        Initializes the ZipCompression class with the path of the file to be compressed.

        Args:
            file_path (str): The path to the file that needs to be compressed
        """

        super().__init__()
        self.file_path = file_path
    
    def compress_to_zip(self):
        """
        Compresses the specified file to a .zip archive.

        This method uses the zipfile.ZipFile class to create a .zip archive
        with the name of the file, and adds the file to the archive.

        Args:
            None

        Returns:
            None
        """
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError

            file_dir = os.path.dirname(self.file_path)
            filename_ext = os.path.basename(self.file_path)
            filename = os.path.splitext(os.path.basename(self.file_path))[0]

            zip_path = os.path.join(file_dir, f"{filename}.zip")

            with zipfile.ZipFile(zip_path, "a") as zip_file:
                zip_file.write(self.file_path, arcname=filename_ext) 
        
        except FileNotFoundError:
            print(f"The specified path does not exist.")

def main():
    """
    Runs the main function of the project.
    """

    file_path = input("Introduce the path of the file to compress into a .zip format: ")
    ZipCompression(file_path=file_path).compress_to_zip()

if __name__ == "__main__":
    main()