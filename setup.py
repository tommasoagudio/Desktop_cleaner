from cx_Freeze import setup, Executable

setup(
    name="Desktop cleaner",
    version="0.1",
    description="simple desktop cleaner that moves all files from desktop to a folder with the current date and time",
    executables=[Executable("main.py")]
)