###strings o cadenas de texto

nombre = "Heidy"
apellido = "Leonardi"

print(nombre + "" + apellido)

texto = "Este texto \n tiene salto de línea y \t tabulación"
print(texto)

#Formateo
user, password, email = "hleonardi", 12345, "hleonardi@gmail.com"
print("Su usuario y contraseña son {} {} y su email {} ". format(user, password, email))
print("Su usuario y contraseña son %s %d y su email %s" % (user, password, email))
print("Su usuario y contraseña son " + user + " " + str(password) + "y su email " + email)
print(f"Su usuario y contraseña son {user} {password} y su email {email}")