import os
print('Exist:', os.access("file:///D:/darhan/George_B_Thomas_Jr_,_Maurice_D_Weir,_Joel_R_Hass_Thomas'_Calculus%20(1).pdf", os.F_OK))
print('Readable:', os.access("file:///D:/darhan/George_B_Thomas_Jr_,_Maurice_D_Weir,_Joel_R_Hass_Thomas'_Calculus%20(1).pdf", os.R_OK))
print('Writable:', os.access("file:///D:/darhan/George_B_Thomas_Jr_,_Maurice_D_Weir,_Joel_R_Hass_Thomas'_Calculus%20(1).pdf", os.W_OK))
print('Executable:', os.access("file:///D:/darhan/George_B_Thomas_Jr_,_Maurice_D_Weir,_Joel_R_Hass_Thomas'_Calculus%20(1).pdf", os.X_OK))
    
