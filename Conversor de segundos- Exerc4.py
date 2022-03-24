segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

Dias = total_segs // 86400
Horas_restantes = total_segs % 86400

Horas = Horas_restantes // 3600
Minutos_restantes = Horas_restantes % 3600

Minutos = Minutos_restantes // 60

Segundos = Minutos_restantes % 60


print(Dias, "dias,", Horas, "horas,", Minutos, "minutos e", Segundos, "segundos.")
