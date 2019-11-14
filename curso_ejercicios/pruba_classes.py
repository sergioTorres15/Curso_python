from datetime import datetime

class contacto:
    def __init__(self, nombre, apellido,numero,email,fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.email = email
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")

    def get_full_name(self):
        return self.nombre +" "+self.apellido
    def get_age(self):
        today = datetime.today()
        return today.year - self.fecha_nacimiento.year - \
               ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
contacto = contacto(nombre="sergio", apellido="Torres", numero="7442273725", email="sergio@gmail.com",
                    fecha_nacimiento="12/05/1999")

print(contacto.nombre)
print(contacto.get_full_name())
print(contacto.get_age())