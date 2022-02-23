from datetime import datetime, timedelta

diaInicio1,diaInicio2 = input().split("Dia ")
diaInicio = int(diaInicio2)
hInicio_,mInicio_,sInicio_ = input().split(":")
diaFim1,diaFim2 = input().split("Dia ")
diaFim = int(diaFim2)
hFim_,mFim_,sFim_ = input().split(":")

hInicio = int(hInicio_) 
mInicio = int(mInicio_)
sInicio = int(sInicio_)
hFim = int(hFim_) 
mFim = int(mFim_)
sFim = int(sFim_)

a = datetime(year = 2020,month = 4 ,day = diaInicio,hour = hInicio,minute = mInicio,second = sInicio)
b = datetime(year = 2020,month = 4 ,day = diaFim,hour = hFim,minute = mFim, second = sFim)

dias = (b-a).days
segundos = (b-a).seconds
horas = segundos // 3600
segundos %= 3600
minutos = segundos//60
segundos %= 60
segundos = segundos//1

print("%i dia(s)"%(dias))
print("%i hora(s)"%(horas))
print("%i minuto(s)"%(minutos))
print("%i segundo(s)"%(segundos))
