entrada_d_inicio = input()
entrada_h_inicio = input()
entrada_d_fim = input()
entrada_h_fim = input()

TOTAL_SEGUNDOS_EM_UM_DIA = 24*3600

d_inicio = int(entrada_d_inicio.split(" ")[1])
d_fim = int(entrada_d_fim.split(" ")[1])

h_inicio = int(entrada_h_inicio.split(":")[0].strip())
m_inicio = int(entrada_h_inicio.split(":")[1].strip())
s_inicio = int(entrada_h_inicio.split(":")[2].strip())

h_fim = int(entrada_h_fim.split(":")[0].strip())
m_fim = int(entrada_h_fim.split(":")[1].strip())
s_fim = int(entrada_h_fim.split(":")[2].strip())

total_inicio = h_inicio*3600+m_inicio*60+s_inicio
total_fim = h_fim*3600+m_fim*60+s_fim


r_dias,r_horas,r_min,r_segun = 0,0,0,0
if total_fim == total_inicio:
    r_dias = d_fim - d_inicio
elif total_fim > total_inicio:
    r_dias = d_fim - d_inicio
    dif = total_fim - total_inicio
    r_horas = dif // 3600
    r_min = (dif - r_horas * 3600) // 60
    r_segun = dif - r_horas * 3600 - r_min * 60
else:
    total = TOTAL_SEGUNDOS_EM_UM_DIA - total_inicio + total_fim
    r_horas = total // 3600
    r_min = (total - r_horas * 3600) // 60
    r_segun = total - r_horas * 3600 - r_min * 60

print("{} dia(s)".format(r_dias))
print("{} hora(s)".format(r_horas))
print("{} minuto(s)".format(r_min))
print("{} segundo(s)".format(r_segun))