import obrab as obr
import math

rc = obr.pd.read_csv('data.csv', skiprows=1, header=None)
rc.columns = ['t', 'sa', 'da', 'ibys', 'obys']
rc = rc[obr.np.logical_or(rc.sa == obr.IP_addr, rc.da == obr.IP_addr)]
rc.ibys = rc.ibys.apply(lambda row: int(row) if 'M' not in row else (int(float(row[:-1])*10**6)))
rc.t = rc.t.apply(lambda row: row[10:18])
print(f'Всего соединений с IP {obr.IP_addr}: {rc.shape[0]} шт.\n')

outcoming_traffic = rc[rc.sa == obr.IP_addr].ibys.sum() / 10**3
incoming_traffic =  rc[rc.da == obr.IP_addr].ibys.sum() / 10**3

print(f'Входящий трафик составил {incoming_traffic:0.2f} Кб.')
print(f'Исходящий трафик составил {outcoming_traffic:0.2f} Кб.')

print(f'Счет за входящий трафик: {math.floor(obr.koef * incoming_traffic):0.2f} р.')
print(f'Счет за исходящий трафик: {math.floor(obr.koef * outcoming_traffic):0.2f} р.')
