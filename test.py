import pandas as pd

level = 0

def zero(operation=None):  
    global level
    level += 1
    if(level != 1 and level != 3):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones numericas en esta parte')
    resOp = ""
    if(level == 1):
        resOp = str(0)
    if(level == 3):
        resOp = str(0)+str(operation)
        level = 0
        
    return int(pd.eval(resOp))
    
def one(operation=None):   
    global level
    level += 1
    if(level != 1 and level != 3):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones numericas en esta parte')
    resOp = ""
    if(level == 1):
        resOp = str(1)
    if(level == 3):
        resOp = str(1)+str(operation)
        level = 0
        
    return int(pd.eval(resOp))
    
def two(operation=None): 
    global level
    level += 1
    if(level != 1 and level != 3):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones numericas en esta parte')
    resOp = ""
    if(level == 1):
        resOp = str(2)
    if(level == 3):
        resOp = str(2)+str(operation)
        level = 0
        
    return int(pd.eval(resOp))
    
def three(operation=None): 
    global level
    level += 1
    if(level != 1 and level != 3):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones numericas en esta parte')
    resOp = ""
    if(level == 1):
        resOp = str(3)
    if(level == 3):
        resOp = str(3)+str(operation)
        level = 0
        
    return int(pd.eval(resOp))
    
def four(operation=None): 
    global level
    level += 1
    if(level != 1 and level != 3):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones numericas en esta parte')
    resOp = ""
    if(level == 1):
        resOp = str(4)
    if(level == 3):
        resOp = str(4)+str(operation)
        level = 0
        
    return int(pd.eval(resOp))
    
def five(operation=None): 
    global level
    level += 1
    if(level != 1 and level != 3):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones numericas en esta parte')
    resOp = ""
    if(level == 1):
        resOp = str(5)
    if(level == 3):
        resOp = str(5)+str(operation)
        level = 0
        
    return int(pd.eval(resOp))
    
def six(operation=None):  
    global level
    level += 1
    if(level != 1 and level != 3):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones numericas en esta parte')
    resOp = ""
    if(level == 1):
        resOp = str(6)
    if(level == 3):
        resOp = str(6)+str(operation)
        level = 0
        
    return int(pd.eval(resOp))
    
def seven(operation=None):  
    global level
    level += 1
    if(level != 1 and level != 3):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones numericas en esta parte')
    resOp = ""
    if(level == 1):
        resOp = str(7)
    if(level == 3):
        resOp = str(7)+str(operation)
        level = 0
        
    return int(pd.eval(resOp))
    
def eight(operation=None): 
    global level
    level += 1
    if(level != 1 and level != 3):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones numericas en esta parte')
    resOp = ""
    if(level == 1):
        resOp = str(8)
    if(level == 3):
        resOp = str(8)+str(operation)
        level = 0
        
    return int(pd.eval(resOp))
    
def nine(operation=None):  
    global level
    level += 1
    if(level != 1 and level != 3):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones numericas en esta parte')
    resOp = ""
    if(level == 1):
        resOp = str(9)
    if(level == 3):
        resOp = str(9)+str(operation)
        level = 0
        
    return int(pd.eval(resOp))
    
def plus(operation=None):
    global level
    level += 1
    if(level != 2):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones de operaciones aritmeticas en esta parte')
    return "+"+str(operation)
    
def minus(operation=None): 
    global level
    level += 1
    if(level != 2):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones de operaciones aritmeticas en esta parte')
    return "-"+str(operation)
    
def times(operation=None): 
    global level
    level += 1
    if(level != 2):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones de operaciones aritmeticas en esta parte')
    return "*"+str(operation)
    
def divided_by(operation=None):   
    global level
    level += 1
    if(level != 2):
        raise Exception('Nivel de operacion incorrecto, solo se aceptan funciones de operaciones aritmeticas en esta parte')
    return "/"+str(operation)
    
print(four(times(five())))
print(one(plus(eight())))
print(seven(minus(three())))
print(nine(divided_by(three())))