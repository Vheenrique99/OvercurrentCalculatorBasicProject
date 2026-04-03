

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
        if num > pickup*1.1:
            return num
        else:
            return None 

    except ValueError:

        return None

def calcula_tempo(curva, pickup, dial,corrente, modelo_curva):

    if modelo_curva == "IEC":

        if curva == 'Normal inverse':
            
            return 0.14/(pow((corrente/pickup),0.02)-1)*dial
        
        elif curva == 'Very Inverse':

            return 13.5/(pow((corrente/pickup), 1)-1)*dial
        
        elif curva == 'Extremely inverse':

            return 80/(pow((corrente/pickup),2)-1)*dial
        
        elif curva == 'Long Time inverse':

            return 120/(pow((corrente/pickup), 1)-1)*dial
        
        else:

            return 0.05/(pow((corrente/pickup), 0.04)-1)*dial
    
    elif modelo_curva == "ANSI/IEE":

        if curva == 'Inverse':
            
            return ((44.6705/(pow((corrente/pickup),2.0938)-1))+0.8983)*dial
        
        elif curva == 'Short Inverse':

            return ((1.3315/(pow((corrente/pickup),1.2969)-1))+0.16965)*dial
        
        elif curva == 'Long Inverse':

            return ((28.0715/(pow((corrente/pickup),1)-1))+10.9269)*dial
        
        elif curva == 'Moderately Inverse':

            return ((0.0515/(pow((corrente/pickup),0.02)-1))+0.114)*dial
        
        elif curva == 'Very Inverse':

            return ((19.61/(pow((corrente/pickup),2)-1))+0.491)*dial

        elif curva == 'Extremely Inverse':

            return ((28.2/(pow((corrente/pickup),2)-1))+0.1217)*dial
        
        else:

            return ((2.3985/(pow((corrente/pickup),1.5625)-1))+1.06795)*dial
    
    else:

        if curva == 'US Moderately Inverse':
            
            return ((0.0104/(pow((corrente/pickup),0.02)-1))+0.0226)*dial
        
        elif curva == 'US Inverse':

            return ((5.95/(pow((corrente/pickup),2)-1))+0.18)*dial
        
        elif curva == 'US Very inverse':

            return ((3.88/(pow((corrente/pickup),2)-1))+0.0963)*dial
        
        elif curva == 'US Extremely Inverse':

            return ((5.67/(pow((corrente/pickup),2)-1))+0.0352)*dial
        
        else:

            return ((0.00342/(pow((corrente/pickup),0.02)-1))+0.00262)*dial


