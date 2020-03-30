import obrab as obr

Ph_num = 933156729
In_koef = 4
Out_koef = 2
SMS_koef = 5

in_call = obr.int_r(obr.sum_Tel(In_koef, obr.obrab[obr.obrab.msisdn_dest == Ph_num].call_duration.values[0]))

out_call = obr.int_r(obr.sum_Tel(Out_koef, obr.obrab[obr.obrab.msisdn_origin == Ph_num].call_duration.values[0]))
if out_call > 20.0:
	out_call = 20

sms = obr.int_r(obr.sum_sms(SMS_koef, obr.obrab[obr.obrab.msisdn_origin == Ph_num].sms_number.values[0] - 10))

print(f'Стоимость входящих звонков: {in_call}')
print(f'Стоимость исходящих звонков: {out_call}')
print(f'Стоимость СМС: {sms}')
print(f'Общая стоимость: {sms + in_call + out_call}')