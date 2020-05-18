class mascota:
    __id_mascota: int
    __nombre_mascota : str
    __especie_mascota : str
    __tipo_mascota : str
    __peso_mascota : float
    __id_cliente : int
    
    def set_id_mascota(self, id):
        self.__id_mascota = id
        
    def get_id_mascota(self):
        return self.__id_mascota
    
    def set_nombre(self, nombre):
        self.__nombre_mascota = nombre
    
    def get_nombre(self):
        return self.__nombre_mascota
        
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
        
    def get_id_cliente(self):
        return self.__id_cliente
        
    def set_id_cliente(self, id):
        self.__id_cliente = id
        
    def to_string(self):
        cad = ("nombre: "+str(self.get_nombre())+" especie: "+str(self.get_especie())+" tipo: "+str(self.get_tipo())+" peso: "+str(self.get_peso())+" cliente: "+str(self.get_id_cliente()))
        return cad
