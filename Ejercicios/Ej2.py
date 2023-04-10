class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 


yin = Yin() 
yang = Yang() 


#creamos un atributo yang en el objeto yin, y le asigna el valor del omjeto yang
yin.yang = yang 
 
print(yang) 
print(yang is yin.yang) 


#espera a que acabe el programa ya que la variable yang todavía esta en uso, cuando acaba el programa elimina la variable yang, por eso el mensaje sale al final por mucho que este antes llamado el método

yang.__del__()
#llamando al metodo explicitamente podemos hacer que imprima "Yang destruido" antes que "?", eso no quita que al final del programa se vuelva a imrimir, ya que esa es la funcion espedial __del__
#>>>  Yang destruido
#>>>  ?
#>>>  Yang destruido

print("?") 


#otra opcion de hacerlo es primero eliminando la instancia yin, la variable yang no se habra creado 
