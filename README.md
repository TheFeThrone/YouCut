# YouCut
Youtube video cutter accompanied with prompts

### Installation (can be skipped - will run in main files)
- Open folder (un-)install
- Run install.bat
  - this will install (if not present) Python 3.10+, pytube library, ffmpeg-python library and FFmpeg
    - it uses winget and pip install

### Function
- Run YouCut.bat or YouCut.py

  <table style="border-collapse: collapse;">
    <tr>
    <td style="padding: 10px; border: none; text-align: center;">1: <img src="https://user-images.githubusercontent.com/117587855/226498974-5f807841-82bf-461e-97aa-0a8739321f8a.png" alt="Step 1: Youtube URL"></td>
  </tr>
  <tr>
    <td style="padding: 10px; border: none; text-align: center;">2: <img src="https://user-images.githubusercontent.com/117587855/226499079-c5a8edd8-eb4d-49e5-b5eb-11aebb393900.png" alt="Step 2: Destination Folder"></td>
  </tr>
  <tr>
    <td style="padding: 10px; border: none; text-align: center;">3: <img src="https://user-images.githubusercontent.com/117587855/226499145-352be18f-2b21-40d8-a065-7036191a64c7.png" alt="Step 3: Output Name"></td>
  </tr>
  <tr>
    <td style="padding: 10px; border: none; text-align: center;">4: <img src="https://user-images.githubusercontent.com/117587855/226499184-fe0cc890-862f-4aab-b752-bd6e147e2677.png" alt="Step 4: Cuts"></td>
  </tr>
  <tr>    
    <td style="padding: 10px; border: none; text-align: center;">5: <img src="https://user-images.githubusercontent.com/117587855/226499565-30c3115e-c65e-47b1-b5dc-780f2a852504.png" alt="Finished"></td>
  </tr>
  </table>

# Bug fix (if it doesnt work)
- Open folder pytube_fix
- Run fix.bat
  - this will replace the original cipher.py file in the pytube library installation folder with the one in the pytube_fix folder
    - it basically replaces line 411 in the file
    - before: ```transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)```
    - new: ```transform_plan_raw = js```
    - thanks to @MikeCVermeer for the temporary fix
