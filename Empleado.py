class empleado:
    #aqui va el codigo 

    '''--------------------------------------------
    # Atributos 
    --------------------------------------------'''

    nombres=''
    apellidos=''
    '''--------------------------------------------
    # 1 = Masculino 2 = Femenino
    --------------------------------------------'''
    sexo=0
    salario=0
    
    '''------------------------------------------
    
    # Metodos
    
    ------------------------------------------'''

    def cambiarSalario(self, nSalario):
        #aqui va el codigo
        self.salario = nSalario
        return "cambio de salario realizado" + self.salario
        
    def consultarSalario(self):
        #aqui va el codigo
        return self.salario
    
    def AumentoSalario(self):
        #aqui va el codigo
        aumento = self.salario*0.05
        nSalario = self.salario+aumento
        self.salario = nSalario
        return "Su nuevo Salario es: "+ self.salario



