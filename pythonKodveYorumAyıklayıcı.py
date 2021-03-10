'''
 Bu program verilen python dosyasından yorum satırlarını başka bir dosyaya, kod 
satırlarını bir başka satıra kaydeder.
'''


if __name__ == "__main__":   
    source = open("test.py", "r", encoding="utf-8")  # Kaynak dosyamız 
    yorum  = open("yorum.py", "a")                  # Yorum satırlarının kaydedileceği dosya
    code   = open( "code.py", "a")                  # Kod satırlarının kaydedileceği dosya
    
    flag_multiline = 0 # Çoklu yorum satırlarının başında mıyız sonunda mıyız diye belirten flag
    flag  = 0                 # Tekli yorum satırında mıyız diye belirten flag
    for line in source:
        for i in range(0, len(line)):
            
            if flag_multiline == 1:
                yorum.write(line[i])
                if line[i] == "'" and line[i+1] == "'" and line[i+2] == "'" and flag_multiline == 1:
                    yorum.write(line[i+1])
                    yorum.write(line[i+2])
                    yorum.write(line[i+3])
                    flag = 0 
                    flag_multiline = 0
                    i += 3
                
            elif line[i] == '#':
                flag = 1
                for j in range(i, len(line)):
                    yorum.write(line[j])
                flag = 0
            
            elif line[i] == "'" and line[i+1] == "'" and line[i+2] == "'" and flag_multiline == 0:
                flag_multilines = 1
                yorum.write(line[i])
                flag = 1
                
# =============================================================================
#             elif flag_multiline != 1 and flag != 1:
#                 code.writelines(line[i])
'''
    Kodları bastırmada sıkıntı var boş bi vaktimde bakıcam
'''
# =============================================================================
     