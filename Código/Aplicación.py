from tkinter import *
from turtledemo.minimal_hanoi import play

raiz=Tk()
for i in range(0,70):
    a = Label(raiz,text="",bg="#002D87")
    a.grid(column=0,row=i)
    b = Label(raiz,text="",bg="#002D87")
    b.grid(column=i,row=0)

raiz.config(bg="#002D87")
raiz.title("APP DE BANCA MOVIL")
raiz.geometry("600x500")
raiz.resizable(True, True)
raiz.iconbitmap("icon.ico")
imagen=PhotoImage(file="bcp.png")
fondo=Label(raiz,image=imagen).place(x=150,y=10)
global saldo
saldo=5000
millas = 0


labtexto=Label(raiz, text="Ingrese el numero de su tarjeta: ").place(x=100,y=300)
entry_n= StringVar()  
labcon=Label(raiz, text="Ingrese su clave digital: ").place(x=100,y=360)
cuadronum=Entry(raiz,width=16,font=("arial",20), textvariable = entry_n)
def character_limit(entry_n):                                                                       #Definiendo la funcion para el maximo de caracteres del numero de cuenta
    if len(entry_n.get()) > 0:
        entry_n.set(entry_n.get()[:16])
entry_n.trace("w", lambda *args: character_limit(entry_n))
cuadronum.grid(column=52,row=14)
entry_clave = StringVar()
cuadrocon=Entry(raiz, show="*",width=4,font=("Arial",20),textvariable = entry_clave)  
cuadrocon.grid(column=52,row=16,sticky="W")
def character_limit2(entry_clave):                                                                  #Definiendo la función para el máximo de caracteres de la clave
    if len(entry_clave.get()) > 0:
        entry_clave.set(entry_clave.get()[:4])
entry_clave.trace("w", lambda *args: character_limit2(entry_clave))


def clic0():  
    if len(cuadronum.get()) == 16 and len(cuadrocon.get()) == 4 :
        raiz.withdraw() 
        menu=Tk()
        menu.config(bg="#002D87")
        menu.title("Menu de opciones")
        menu.resizable(False, False)
        menu.geometry("400x550")  
        menu.iconbitmap("icon.ico")          
        label1=Label(menu,text="Bienvenido al menu de opciones",font=("Times New Roman", 14),fg="black").place(x=70,y=10)
        def clic1():
            global saldo
            menu.withdraw()
            menu2=Tk()
            menu2.config(bg="#002D87")
            menu2.title("Estado de cuenta")
            menu2.resizable(False,False)
            menu2.geometry("500x500")
            menu2.iconbitmap("icon.ico")
            text2=Label(menu2,text= f"el saldo de su tarjeta actual es {saldo} soles",font=("Lucida Handwriting",15), bg="gray").place(x=10,y=15)
            def regresar1():
                menu2.withdraw()
                play(clic0())
            bot= Button(menu2,text='Regresar',bg= "#6747c7",font=("Comic Sans MS",13),width=30,fg= "white", command=regresar1).place(x=50, y=100)
            
        
        def clic2():
            menu.withdraw()
            menu3=Tk()
            menu3.config(bg="#002D87")
            menu3.title("Estado de cuenta")
            menu3.resizable(False,False)
            menu3.geometry("700x450")
            menu3.iconbitmap("icon.ico")
            text3=Label(menu3,text="Ingrese el numero de tarjeta a transferir: ",font=("Lucida Handwriting",12), bg="gray").place(x=10,y=40)
            text4=Label(menu3,text="Ingrese el monto a transferir: ",font=("Lucida Handwriting",12), bg="gray")
            text4.grid(column=2,row=5)
            tarjeta=Entry(menu3).place(x=450,y=40)
            for i in range(0,70):
                a = Label(menu3,text="",bg="#002D87")
                a.grid(column=0,row=i)
                b = Label(menu3,text="",bg="#002D87")
                b.grid(column=i,row=0)
            global monto
            monto = 0
            monto=Entry(menu3)
            monto.grid(column=29,row=5)
            
            
           
            def clictrans():      
                global saldo  
                menu3.withdraw()
                menun=Tk()
                menun.config(bg="#002D87")
                menun.title("Confirmacion")
                menun.resizable(False,False)
                menun.geometry("600x400")
                menun.iconbitmap("icon.ico")
                def regresar1():
                    menun.withdraw()
                    play(clic0())
                saldo -= int(monto.get())
                text2=Label(menun,text= "La transeferencia se ha realizado correctamente",font=("Lucida Handwriting",14), bg="pink").place(x=10,y=15)
                text3=Label(menun,text=f" Su saldo actual es de :{saldo} nuevos soles", font=("Algerian",14), bg="pink").place(x=10, y=40)
                bot1= Button(menun,text='Regresar',bg= "#6747c7",font=("Comic Sans MS",13),width=30,fg= "white", command=regresar1).place(x=10, y=100)
                             
        
                
            trans = Button(menu3,text="TRANSFERIR", bg= "skyblue",font=("Comic Sans MS",14),width=40 ,fg= "black", command=clictrans).place(x=150,y=280)
            
                
        
        def clic3():
            menu.withdraw()
            global monto
            menu4=Tk()
            menu4.config(bg="#002D87")
            menu4.title("Estado de cuenta")
            menu4.resizable(False,False)
            menu4.geometry("400x500")
            menu4.iconbitmap("icon.ico")
            def regresar1():
                    menu4.withdraw()
                    play(clic0())
            text5=Label(menu4,text= f"Ha realizado una trasferencia de {monto.get()}" ,font=("Lucida Handwriting",8),bg="gray").place(x=10,y=15)
            bot2= Button(menu4,text='Regresar',bg= "#6747c7",font=("Comic Sans MS",13),width=30,fg= "white", command=regresar1).place(x=10, y=100)                      
        
        def clic4():
            global b
            b = 0
            menu.withdraw()
            menu5=Tk()
            menu5.config(bg="#002D87")
            menu5.title("Realizar pagos")
            menu5.resizable(False,False)
            menu5.geometry("600x400")
            menu5.iconbitmap("icon.ico")
            text6=Label(menu5,text= "Ingrese la empresa a la que desea pagar: " ,font=("Lucida Handwriting",11), bg="gray").place(x=10,y=15)
            for i in range(0,70):
                j = Label(menu5,text="",bg="#002D87")
                j.grid(column=0,row=i)
                k = Label(menu5,text="",bg="#002D87")
                k.grid(column=i,row=0)
            text7=Label(menu5,text= "Ingrese el monto que desea pagar: " ,font=("Lucida Handwriting",11), bg="gray").place(x=10,y=100) 
            a=Entry(menu5).place(x=400,y=16)
            b=Entry(menu5)
            b.grid(column=67,row=5)
            
            
            
            
            def clicpago():
                global saldo 
                menu5.withdraw()
                menun1=Tk()
                menun1.config(bg="#002D87")             
                menun1.title("Validacion del pago")
                menun1.resizable(False,False)
                menun1.geometry("600x400")
                menun1.iconbitmap("icon.ico")
                def regresar1():
                    menun1.withdraw()
                    play(clic0())
                saldo -= int(b.get())
                text2=Label(menun1,text= "La transeferencia se ha realizado correctamente",font=("Lucida Handwriting",14), bg="pink").place(x=10,y=15)
                text3=Label(menun1,text=f" Su saldo actual es de :{saldo}nuevos soles", font=("Algerian",14), bg="pink").place(x=10, y=40)
                
                
                
                bot1= Button(menun1,text=' Regresar',bg= "#6747c7",font=("Comic Sans MS",13),width=30,fg= "white", command=regresar1).place(x=10, y=100)
            
            boto= Button(menu5,text="Pagar",bg= "#6747c7",font=("Comic Sans MS",13),width=30,fg= "white", command=clicpago).place(x=80, y=200)
            
        def clic5():           
                menu.withdraw()
                menu6=Tk()
                menu6.config(bg="#002D87")
                menu6.title("MILLAS GANADAS")
                menu6.resizable(False,False)
                menu6.geometry("600x400")
                menu6.iconbitmap("icon.ico")
                millas = (int(monto.get()) + int(b.get()))/20
                def regresar1():
                    menu6.withdraw()
                    play(clic0())
                text2=Label(menu6,text= f" Millas ganadas hasta ahora es de: {millas}",font=("Lucida Handwriting",14), bg="pink").place(x=10,y=15)                
                bot1= Button(menu6,text=' Regresar',bg= "#6747c7",font=("Comic Sans MS",13),width=30,fg= "white", command=regresar1).place(x=10, y=100)
             
        
        r1 = Button(menu,text='1. CONSULTAR ESTADO DE CUENTA', bg= "#999",font=("Comic Sans MS",10),width=40,fg= "white",command=clic1).place(x=20,y=50)
        r2 = Button(menu,text='2. REALIZAR TRANSFERENCIAS BANCARIAS',bg= "#999",font=("Comic Sans MS",10),width=40,fg= "white", command=clic2).place(x=20,y=150)
        r3 = Button(menu,text='3. VER HISTORIAL DE LA CUENTA',bg= "#999",font=("Comic Sans MS",10),width=40,fg= "white",command=clic3).place(x=20,y=250)
        r4 = Button(menu,text='4. REALIZAR PAGOS',bg= "#999",font=("Comic Sans MS",10),width=40,fg= "white",command=clic4).place(x=20,y=350)
        r5 = Button(menu,text='5. VER MILLAS ACUMULADAS',bg= "#999",font=("Comic Sans MS",10),width=40,fg= "white",command=clic5).place(x=20,y=450)
        
        menu.mainloop()   
            
        def cerrar():
                   
            raiz.destroy()
    else:
        chau=Tk()
        chau.title("ERROR")
        chau.iconbitmap("icon.ico")
        chau.geometry("550x40")
        L1= Label(chau,text="INSERTE CORRECTAMENTE LOS DATOS,POR FAVOR.",font=("Arial",15)).place(x=10,y=5)
        chau.resizable(0,0)

btningresar = Button(raiz,text="INGRESAR",font=("Flexo",10),width=15,command=clic0).place(x=200,y=430)
raiz.mainloop()
