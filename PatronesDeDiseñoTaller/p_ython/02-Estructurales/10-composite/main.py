from leaf import File
from composite import Directory

def main():
    
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    directory1 = Directory("directory1")
    
    directory1.add(file1)
    directory1.add(file2)
    
    directory1.show_details()
    
if __name__ == "__main__":
    main()
    
    
proxy virtual: permite crea objetos costosos por encargo
proxy remoto: proporciona un representante local de un objeto situado en otro espacio de direcciones
proxy de protección: controla el acceso al objeto original
proxy referencia inteligente a un puntero

    
    
    
    
    
    
    
    
    