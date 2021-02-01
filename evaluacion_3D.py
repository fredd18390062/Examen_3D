# EXAMEN DE 3D
# 1. Tu determinas el tamaño de la ventana de la figura.
# 2. Pedirle al usuario que proporcione las coordenadas del hit point. 
# 3. Usar colores para mostrar etiquetas de los lados usados para los triángulos de las líneas punteadas.
# 3. Etiqetar cuales son las áreas del A, A1 y A2.
# 4. Que el programa termine hasta que el usuario pulse la tecla “Esc”.
# 5. Documentar adecuadamente y claramente los pasos para hacer los cálculos.
# 6. Usar la formula de Heron para los cálculos.
# 7. Mostrar mensajes de cuando esta fuera del limite y dentro del limite.
# 8. Etiquetar los ejes X, Y, y poner un titulo

import matplotlib.pyplot as plt 
import numpy as np
from math import sqrt 
import keyboard
import sys

# ARRAY
x=[30,40,80,10,40]
y=[10,60,60,10,75]
z=[-10,10,10,0,0]


# FUNCION PARA EL TAMAÑO DEL GRID
def plotPlaneLine(xg,yg,zg,bandera,areaBase,area1,area2):
    plt.title('FREDD SANCHEZ ALCALA')
    plt.axis([0,150,100,0])
    plt.axis('on')
    plt.grid(True)
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')

    # BASE DEL TRIANGULO
    plt.plot([x[0],x[1]],[y[0],y[1]],color='k')
    plt.plot([x[1],x[2]],[y[1],y[2]],color='k')
    plt.plot([x[2],x[0]],[y[2],y[0]],color='k')

    # LADOS DEL TRIANGULO
    plt.plot([x[0],x[3]],[y[0],y[3]],linestyle=':',color='b')
    plt.plot([x[3],x[1]],[y[3],y[1]],linestyle=':',color='b')
    plt.plot([x[3],x[2]],[y[3],y[2]],linestyle=':',color='b')

    # DIBUJO DE LA LINEA DE LA INSERCCION
    plt.plot([x[3],x[4]],[y[3],y[4]],color='r')

    if(bandera==True):
        plt.text(100,60,'hitpoint se encuentra dentro del plano')
    else:
        plt.text(100,60,'hitpoint se encuentra fuera del plano')

    areaBase = int(areaBase)
    area1 = int(area1)
    area2 = int(area2)

    plt.text(100,25,'Area base =')
    plt.text(125,25,areaBase)
    plt.text(100,35,'Area1 =')
    plt.text(120,35,area1)
    plt.text(100,40,'Area2 =')
    plt.text(120,40,area2)
    plt.text(100,50,'Area1+Area2 =')
    plt.text(135,50,area1+area2)
    plt.show()

# BASE TRIANGULO
def hitpoint(x,y,z):
    # DISTANCIA 0 A 1 
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    D01=sqrt(a*a+b*b+c*c) 
    # DISTANCIA 1 A 2
    a=x[2]-x[1]
    b=y[2]-y[1]
    c=z[2]-z[1]
    D12=sqrt(a*a+b*b+c*c) 
    # DISTANCIA 0 A 2
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    D02=sqrt(a*a+b*b+c*c)
    # USAMOS LA FORMULA DE HERON PARA CALCULAR EL AREA
    s=(D01+D12+D02)/2
    areaBase=sqrt(s*(s-D01)*(s-D12)*(s-D02))
        
# TRIANGULO 1
    # DISTANCIA 0 A 1 
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    D01=sqrt(a*a+b*b+c*c) 
    # DISTANCIA 1 A 3 
    a=x[3]-x[1]
    b=y[3]-y[1]
    c=z[3]-z[1]
    D13=sqrt(a*a+b*b+c*c) 
    # DISTANCIA 0 A 3
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    D03=sqrt(a*a+b*b+c*c)
    # USAMOS LA FORMULA DE HERON PARA CALCULAR EL AREA
    s=(D01+D13+D03)/2
    area1=sqrt(s*(s-D01)*(s-D13)*(s-D03))

# TRIANGULO 2
    # DISTANCIA 0 A 2
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    D02=sqrt(a*a+b*b+c*c) 
    # DISTANCIA 2 A 3
    a=x[3]-x[2]
    b=y[3]-y[2]
    c=z[3]-z[2]
    D23=sqrt(a*a+b*b+c*c) 
    # DISTANCIA 0 A 3
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    D03=sqrt(a*a+b*b+c*c)
    # USAMOS LA FORMULA DE HERON PARA CALCULAR EL AREA
    s=(D02+D23+D03)/2
    area2=sqrt(s*(s-D02)*(s-D23)*(s-D03))

    # VERIFICAMOS EL HITPOINT
    sumaAreas = area1+area2
    bandera = True
    if(areaBase>sumaAreas):
        bandera = True
    else:
        bandera = False
    
    # PLOTEAMOS LA FIGURA Y LAS ETIQUETAS 
    plotPlaneLine(x,y,z,bandera,areaBase,area1,area2)

# INSERCCION DE LOS DATOS Y EL HITPOINT 
print("PRESIONA ENTER PARA CONTINUAR O ESC PARA SALIR")
while True:
    
    if keyboard.is_pressed('ESC'):
        sys.exit(0)
    if keyboard.is_pressed('ENTER'):
        tecla=input('-------')
        hx=input("Hitpoint x:")
        hy=input("Hitpoint y:")
        # ASIGAMOS LOS ARREGLOS 
        x[3]=int(hx)
        y[3]=int(hy)
        hitpoint(x,y,z)
        print("PRESIONA ENTER PARA CONTINUAR O ESC PARA SALIR")


