from obrab import *

pdf = FPDF()
pdf.add_page()
pdf.add_font('TimesNewRoman', '', 'fonts/TNR.ttf', uni=True)
pdf.add_font('TimesNewRomanB', '', 'fonts/TNRB.ttf', uni=True)
now = datetime.datetime.today()

height = top_table(pdf,
                         bank_name1 = 'ООО "Cashberry LTD"',
                         INN = '7701017140',
                         KPP = '770101001',
                         bank_name2 = 'ОOО "NL INTERNATIONAL"',
                         BIK = '044525187',
                         chknum1 = '88005553535',
                         chknum2 = '40802810200470000062',
                         receiver = 'ООО Кооператив "Озеро"')

height = title(pdf,
                    paynum = 47,
                    day = now.day,
                    mnth = '{:02d}'.format(now.month),
                    year = 20,
                    height = height)

height = rekvizits(pdf,
                             height=height,
                             director='ОOО "Лайк-Центр", '
                                      'г.Москва, Походный проезд, домовладение 3, стр.2',
                             consumer='ООО Кооператив "Озеро", ИНН 5027242045, КПП 502701001, 188650, '
                                   'РОССИЯ, МОСКОВСКАЯ ОБЛ, ЭЛЕКТРОСТАЛЬ Г, СОВЕТСКАЯ УЛ, 26А',
                             osnovanie='№ 874004961 от 18.03.2018')

height = jobs(pdf, [
    {
        'Job': 'Входящие вызовы',
        'VSEGO': 110.44,
        'VSEGO_unit': 'мин.',
        'Number': '',
        'Koef': 0,
    }, {
        'Job': 'Исходящие вызовы',
        'VSEGO': 83.22,
        'VSEGO_unit': 'мин.',
        'Number': '',
        'Koef': 2,
    }, {
        'Job': 'СМС',
        'VSEGO': 73,
        'VSEGO_unit': 'шт.',
        'Number': '',
        'Koef': 1,
    }, {
        'Job': 'Исходящий трафик',
        'VSEGO': 18.28,
        'VSEGO_unit': 'Kб',
        'Number': '',
        'Koef': 0.5,
    }, {
        'Job': 'Входящий трафик',
        'VSEGO': 39.45,
        'VSEGO_unit': 'Kб',
        'Number': '',
        'Koef': 0.5,
    },
], height=height)

height = footer(pdf,
                     height=height,
                     director_name='Терентьев М.П.',
                     buhgalter='Богомолов А.А.')

pdf.output('Report.pdf')



# context = {  "bank_name2" : "NL INTERNATIONAL" , "reciever" : "ООО Кооператив \" Озеро \"" , "BIK" : "044525187" , "chk_num1" : "88005553535" , "chk_num2" : "40802810200470000062" , "payNum" : "47" , "index" : "188650" , "dir_addr" : "г.Москва, Походный проезд, домовладение 3, стр.2" , "rec_addr" : "РОССИЯ, МОСКОВСКАЯ ОБЛ, ЭЛЕКТРОСТАЛЬ Г, СОВЕТСКАЯ УЛ, 26А" , "point" : "№ 20022016 от 12.02.2016" , "director_name" : "М.П. Терентьев" , "buhgalter" : "А.А. Богомолов"}