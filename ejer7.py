from kanren import var, eq, run, Relation, facts

# Definir las relaciones de padres, hermano, tíos y abuelos
padres = Relation()
hermano = Relation()
tios = Relation()
abuelos = Relation()

#mis relaciones de padres
facts(padres, ("Padre1", "Yo"), ("Padre2", "Yo"),("Padre1", "Hermano"), ("Padre2", "Hermano"))
facts(hermano, ("Hermano", "Yo"))
facts(tios, ("Tío1", "Yo"), ("Tío2", "Yo"), ("Tío3", "Yo"),("Tío1", "Hermano"), ("Tío2", "Hermano"), ("Tío3", "Hermano"))

#mis relaciones de abuelos
facts(abuelos, ("Abuelo1","Padre"), ("Abuela1","Padre"), ("Abuela2","Madre"), ("Abuelo2","Madre"))
# Consultas
x = var()  # Defino la variable x

print("Mis padres:")
print(run(2, x, padres(x, "Yo")))

print("Mi hermano:")
print(run(1, x, hermano(x, "Yo")))

print("Mis tíos:")
print(run(3, x, tios(x, "Yo")))

print("Mis abuelos paternos:")
print(run(4, x, abuelos(x, "Padre")))

print("Mis abuelos maternos:")
print(run(4, x, abuelos(x, "Madre")))
