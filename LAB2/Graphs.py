import obrab as obr
import tarif as trf 

times = obr.np.sort(trf.rc.t.unique())
values = []
for t in times:
    values.append(trf.rc.loc[trf.rc.t == t, ['ibys', 'obys']].sum().sum())

obr.graph(obr.pd.to_datetime(times), values)
