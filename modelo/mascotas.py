class mascota:
    __nombre_mascota
    __especie_mascota
    __tipo_mascota
    __peso_mascota
    
    def set_nombre(self, nombre):
        self.__nombre_mascota = nombre
    
    def get_nombre(self):
        return self.__nombre
        
    def get_especie(self):
        return self.__especie_mascota
        
    def set_especie(self, especie):
        self.__especie_mascota = especie
        
    def get_tipo(self):
        return self.__tipo_mascota
        
    def set_tipo(self, tipo):
        self.__tipo_mascota = tipo
        
    def get_peso(self):
        return self.__peso_mascota
        
    def set_peso(self, peso):
        self.__peso_mascota = peso
