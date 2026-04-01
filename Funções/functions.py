

def float_valor( valor):
    
    try:

        num = float(valor)
        if num > 0:
            return num
        else:
            return None 

    except ValueError:

        return None
    
def verifica_curva(curva):

    if curva == '':
        
        return None
    
    else:

        return True
    
def float_corrente_teste( valor, pickup):
    
    try:
        
        num = float(valor)
        if num > pickup:
            return num
        else:
            return None 

    except ValueError:

        return None

def calcula_tempo(curva, pickup, dial,corrente):


    if curva == 'Normal inverse':
        
        return 0.14/(pow((corrente/pickup),0.02)-1)*dial
    
    elif curva == 'Very Inverse':

        return 13.5/(pow((corrente/pickup), 1)-1)*dial
    
    elif curva == 'Extremely inverse':

        return 80/(pow((corrente/pickup),2)-1)*dial
    
    elif curva == 'Long Time inverse':

        return 120/(pow((corrente/pickup), 1)-1)*dial
    
    elif curva == 'Short-Time Inverse':

        return 0.05/(pow((corrente/pickup), 0.04)-1)*dial