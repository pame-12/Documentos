
print("<<<<< Pizzeria I love Jissell 😍💖 >>>>>")
canidad_de_dinero = int(input("ingresa tu cantidad de dinero: "));
# ingredientes_extras = [];
print("ELIGE UN TIPO DE PIZZA: ");
print("1:Pizza de peperoni $370 ");
print("2:Pizza de jamon y queso $300 ");
print("3:Pizza del diablo $500 ");
print("4:Salir");
opcion = int(input("elige la opcion: "));

match (opcion):
  case (1):
    print("elejiste la pizza de peperoni")
    canidad_de_dinero = canidad_de_dinero - 370;
    peperoni = ["peperoni", "salsa", "mozarella"]
    extra = input("quieres agregar ingredientes extras (y/n): ")
    if (extra == "y"): 
      cantidad = int(input("ingresa la cantidad: "))
      i = 1
      while (i <= cantidad):
        add =  input("Please enter: ")
        peperoni.append(add)
        canidad_de_dinero = canidad_de_dinero - 25;
        i = i + 1
      print(peperoni)  
      print(canidad_de_dinero)  
    case (2):
         print("elejiste la pizza de jamon y queso")
         canidad_de_dinero = canidad_de_dinero - 300;
        peperoni = ["peperoni", "salsa", "mozarella"]
         extra = input("quieres agregar ingredientes extras (y/n): ")
         if (extra == "y"): 
           cantidad = int(input("ingresa la cantidad: "))
           i = 1
          while (i <= cantidad):
            add =  input("Please enter: ")
            peperoni.append(add)
             i = i + 1
             canidad_de_dinero = canidad_de_dinero - 25;
           print(peperoni)     
   case (3):
     print("elejiste la pizza del diablo")
     canidad_de_dinero = canidad_de_dinero - 500;
     peperoni = ["peperoni", "salsa", "mozarella"]
     extra = input("quieres agregar ingredientes extras (y/n): ")
     if (extra == "y"): 
       cantidad = int(input("ingresa la cantidad: "))
       i = 1
       while (i <= cantidad):
         add =  input("Please enter: ")
         peperoni.append(add)
        i = i + 1
         canidad_de_dinero = canidad_de_dinero - 25;
         print(peperoni)
        
