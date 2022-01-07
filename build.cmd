:: Reset the build folder
if exist build rmdir /s /q build
mkdir build
cd build

:: Run the python build script
python3 -m PyInstaller --name "hotkeypresser" --hidden-import=pkg_resources --onefile --icon ../icons/main.ico ../main.py

:: Exit out of the build dir
cd ../