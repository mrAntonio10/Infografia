def get_line(x0, y0, x1, y1):
    '''
    Dibujamos una linea:
        p1(x0,y0)
        p2(x1,y1)  
    '''
    points = [] # lista para almacenar puntos generados
    # 1er paso: dx, dy
    dx = x1 - x0
    dy = y1 - y0
    # variables para iterar xk, yk
    xk = x0
    yk = y0
    y_inc = 1 

    #SI ES NEGATIVO, caso conatrario, sigue sin alterarse
        #en este caso dx negativo REASIGNA TODAS LAS VARIABLES :O
    if dx < 0:
        x0,x1 = x1,x0
        y0,y1 = y1,y0

        dx = -1 * dx
        dy = -1 * dy

        xk=x0
        yk=y0

    if dy < 0:
        dy = -1 * dy
        y_inc = -1
        
   

    # 2do paso: parametro de decision Pk
    Pk = 2 * dy - dx  

    # 3er paso: iterar hasta el punto final:
    while xk <= x1:
        # agregar punto a la lista
        points.append((xk, yk))
        xk += 1
        # decido en base a Pk si y incrementa o no
        if Pk < 0:
            Pk += 2 * dy
            
        else:
            Pk += 2 * dy - 2 * dx
            yk += y_inc
        
    return points

if __name__ == "__main__":
    print(get_line(0, 3, 6, 5))