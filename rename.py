import os
mp3_path = 'ENTER PATH OF MP3 FILES HERE'
text_path = 'ENTER PATH OF TEXT FILE HERE'





os.chdir(mp3_path)

with open(text_path) as txt:
    for line in txt:
        for f in os.listdir():
            file_name, file_ext = os.path.splitext(f)
            if file_name in line:
               os.rename(f,line+'.mp3')
            
            
            
            
            
            
            
            
            
            
            
            
