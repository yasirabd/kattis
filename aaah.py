jon = list(input())
doctor = list(input())

if len(doctor) == 1:
    print('go')
elif len(jon[:-1]) >= len(doctor[:-1]):
    print('go')
else:
    print('no')
