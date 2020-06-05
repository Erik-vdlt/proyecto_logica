class cliente:
    __nombre_cliente : str
    __primer_ap : str
    __segundo_ap : str
    __fecha_nacimiento : str
    __calle : str
    __no_calle : int
    __colonia : str
    __correo: str
    
    def cliente():
        pass
    
    def get_nombre_cliente(self):
        return self.__nombre_cliente
        
    def set_nombre_cliente(self, nombre):
        self.__nombre_cliente = nombre
        
    def get_primer_ap(self):
        return self.__primer_ap
        
    def set_primer_ap(self, primer_ap):
        self.__primer_ap = primer_ap
        
    def get_segundo_ap(self):
        return self.__segundo_ap
        
    def set_segundo_ap(self, segundo_ap):
        self.__segundo_ap = segundo_ap
    
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
        
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento
        
    def get_calle(self):
        return self.__calle
    
    def set_calle(self, calle):
        self.__calle = calle
        
    def get_no_calle(self):
        return self.__no_calle
    
    def set_no_calle(self, noCalle):
        self.__no_calle = noCalle
        
    def get_colonia(self):
        return self.__colonia
        
    def set_colonia(self, colonia):
        self.__colonia = colonia
        
    def get_correo(self):
        return self.__correo
        
    def set_correo(self, correo):
        self.__correo = correo
