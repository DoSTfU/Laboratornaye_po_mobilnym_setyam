from fpdf import FPDF
from num2words import num2words
import datetime
import sys
import os

maximun_shirina = 210
Coord = 20

def top_table (pdf: FPDF, **kwargs):
    height = 30
    l_col_w = 95
    m_col_w = 16
    r_col_w = maximun_shirina - Coord * 2 - l_col_w - m_col_w
    pdf.line(Coord, Coord, maximun_shirina - 20, Coord)
    pdf.line(Coord, Coord, Coord, height + Coord)
    pdf.line(maximun_shirina - Coord, Coord, maximun_shirina - Coord, height + Coord)
    pdf.line(Coord, height + Coord, maximun_shirina - Coord, height + Coord)

    pdf.line(Coord, height * 9 / 21 + Coord, maximun_shirina - Coord, height * 9 / 21 + Coord)
    pdf.line(Coord, height * 12 / 21 + Coord, l_col_w + Coord, height * 12 / 21 + Coord)
    pdf.line(l_col_w + Coord, Coord, l_col_w + Coord, height + Coord)
    pdf.line(l_col_w + Coord + m_col_w, Coord, l_col_w + Coord + m_col_w, height + Coord)
    pdf.line(l_col_w + Coord, Coord + height * 3 / 21, l_col_w + m_col_w + Coord, Coord + height * 3 / 21)
    pdf.line(Coord + l_col_w / 2, Coord + height * 9 / 21, Coord + l_col_w / 2, Coord + height * 12 / 21)
    pdf.line(Coord, height + 15, maximun_shirina / 1.81 - 1, height + 15)

    pdf.set_font("TimesNewRoman", size=9)
    pdf.set_y(Coord)
    pdf.cell(10)
    pdf.multi_cell(95, 4, kwargs['bank_name1'])
    pdf.set_y(Coord + 12.5)
    pdf.cell(10)
    pdf.cell(l_col_w / 2, 5, f'ИНН    {kwargs["INN"]}')
    pdf.cell(l_col_w / 2, 5, f'КПП    {kwargs["KPP"]}')
    pdf.set_y(Coord + 17.5)
    pdf.cell(10)
    pdf.multi_cell(95, 4, kwargs['bank_name2'])
    pdf.set_y(Coord)
    pdf.cell(10 + l_col_w)
    pdf.cell(m_col_w, 5, 'БИК')
    pdf.cell(r_col_w, 5, kwargs['BIK'])
    pdf.set_y(Coord + 5)
    pdf.cell(10 + l_col_w)
    pdf.cell(m_col_w, 5, 'Сч. №')
    pdf.cell(r_col_w, 5, kwargs['chknum1'])
    pdf.set_y(Coord + height * 9 / 21)
    pdf.cell(10 + l_col_w)
    pdf.cell(m_col_w, 5, 'Сч. №')
    pdf.cell(r_col_w, 5, kwargs['chknum2'])

    pdf.set_font("TimesNewRoman", size=8)
    pdf.set_y(Coord + height * 6 / 21)
    pdf.cell(10)
    pdf.cell(l_col_w, 4, 'Банк получателя')
    pdf.set_y(Coord + height * 18 / 21)
    pdf.cell(10)
    pdf.cell(l_col_w / 2, 5, f'Получатель    {kwargs["receiver"]}')


    return Coord + height


def title(pdf: FPDF, **kwargs):
    pdf.set_font("TimesNewRomanB", size=13)
    pdf.set_y(kwargs['height'] + 4)
    pdf.cell(10)
    pdf.cell(maximun_shirina - Coord, 9, f'Счет на оплату № {kwargs["paynum"]} от {kwargs["day"]}.{kwargs["mnth"]}.20{kwargs["year"]} г.')
    pdf.set_line_width(0.6)
    pdf.line(Coord, kwargs['height'] + 13.5, maximun_shirina - Coord, kwargs['height'] + 13.5)

    return kwargs['height'] + 14.1

def rekvizits(pdf: FPDF, **kwargs):
    l_col_w = 28
    r_col_w = maximun_shirina - 2 * Coord - l_col_w
    line_height = 5
    pdf.set_font("TimesNewRoman", size=9)
    pdf.set_y(kwargs['height'] + 2)
    pdf.cell(10)
    pdf.multi_cell(l_col_w, line_height, 'Поставщик (Исполнитель):')

    pdf.set_font("TimesNewRomanB", size=9)
    pdf.set_y(kwargs['height'] + 2)
    pdf.cell(10 + l_col_w)
    director = pdf.multi_cell(r_col_w, line_height, kwargs['director'], split_only=True)
    pdf.multi_cell(r_col_w, line_height, kwargs['director'])

    height = kwargs['height'] + 6 + 5 * len(director)
    pdf.set_font("TimesNewRoman", size=9)
    pdf.set_y(height)
    pdf.cell(10)
    pdf.multi_cell(l_col_w, line_height, 'Покупатель (Заказчик):')

    pdf.set_font("TimesNewRomanB", size=9)
    pdf.set_y(height)
    pdf.cell(10 + l_col_w)
    buyer = pdf.multi_cell(r_col_w, line_height, kwargs['consumer'], split_only=True)
    pdf.multi_cell(r_col_w, line_height, kwargs['consumer'])

    height += len(buyer) * 5 + 6
    pdf.set_y(height)
    pdf.cell(10)
    pdf.set_font("TimesNewRoman", size=9)
    pdf.cell(l_col_w, line_height, 'Основание:')
    pdf.set_font("TimesNewRomanB", size=9)
    pdf.cell(r_col_w, line_height, kwargs['osnovanie'])

    return height + line_height

def jobs (pdf: FPDF, goods, **kwargs):
    col1_w = 8
    col3_w = 20
    col4_w = 18
    col5_w = 18
    col2_w = maximun_shirina - 2 * Coord - col1_w - col3_w - col4_w - col5_w
    height = kwargs['height'] + 6
    start = height
    total = 0
    pdf.set_line_width(0.5)
    pdf.line(Coord, height, maximun_shirina - Coord, height)
    pdf.set_line_width(0.2)
    pdf.line(Coord, height + 5, maximun_shirina - Coord, height + 5)

    pdf.set_font("TimesNewRomanB", size=9)
    pdf.set_y(height)
    pdf.cell(10)
    pdf.cell(col1_w, 5, '№', align='C')
    pdf.cell(col2_w, 5, 'Товары (работы, услуги)', align='C')
    pdf.cell(col3_w, 5, 'Кол-во', align='C')
    pdf.cell(col4_w, 5, 'Цена', align='C')
    pdf.cell(col5_w, 5, 'Сумма', align='C')

    pdf.set_font("TimesNewRoman", size=9)
    height += 6
    index = 0
    for id, good in enumerate(goods):
        is_last = id == len(goods) - 1
        index += 1
        pdf.set_y(height)
        pdf.cell(10)
        pdf.cell(col1_w, 5, str(index), align='C')
        pdf.multi_cell(col2_w, 5, good['Job'])
        pdf.set_y(height)
        pdf.cell(10 + col1_w + col2_w)
        pdf.cell(col3_w, 5, f'{good["VSEGO"]}{" " + good["VSEGO_unit"] if "VSEGO_unit" in good else ""}', align='L')
        pdf.cell(col4_w, 5, f'{good["Koef"]} {"p/" + good["VSEGO_unit"] if "VSEGO_unit" in good else "p"}', align='L')
        pdf.cell(col5_w, 5, f'{good["Koef"] * good["VSEGO"]} р', align='R')
        total += good["Koef"] * good["VSEGO"]

        height += 5 * len(pdf.multi_cell(col2_w, 100, good['Job'], split_only=True))
        if not is_last:
            pdf.line(Coord, height + 1, maximun_shirina - Coord, height + 1)
            height += 2
        else:
            height += 1

    pdf.set_line_width(0.5)
    pdf.line(Coord, start, Coord, height)
    pdf.line(Coord, height, maximun_shirina - Coord, height)
    pdf.line(maximun_shirina - Coord, start, maximun_shirina - Coord, height)

    pdf.set_line_width(0.2)
    pdf.line(Coord + col1_w, start, Coord + col1_w, height)
    pdf.line(Coord + col1_w + col2_w, start, Coord + col1_w + col2_w, height)
    pdf.line(Coord + col1_w + col2_w + col3_w, start, Coord + col1_w + col2_w + col3_w, height)
    pdf.line(Coord + col1_w + col2_w + col3_w + col4_w, start, Coord + col1_w + col2_w + col3_w + col4_w, height)
    pdf.line(Coord + col1_w + col2_w + col3_w + col4_w + col5_w, start, Coord + col1_w + col2_w + col3_w + col4_w + col5_w, height)

    height += 5
    pdf.set_font("TimesNewRomanB", size=9)
    pdf.set_y(height)
    total_price = f'{total:,.2f}'.replace(',', ' ')
    NDS = f'{total * 0.167:,.2f}'.replace(',', ' ')
    pdf.multi_cell(10 + maximun_shirina - 2 * Coord, 5, f'Итого: {total_price:>15} р.', align='R')
    pdf.multi_cell(10 + maximun_shirina - 2 * Coord, 5, f'В том числе НДС: {NDS:>15} р.', align='R')
    pdf.multi_cell(10 + maximun_shirina - 2 * Coord, 5, f'Всего к оплате: {total_price:>15} р.', align='R')

    pdf.set_font("TimesNewRoman", size=9)
    pdf.cell(10)
    pdf.multi_cell(maximun_shirina - 2 * Coord, 5, f'Всего наименований {index} на сумму {total_price} руб.')
    pdf.set_font("TimesNewRomanB", size=9)
    pdf.cell(10)
    pdf.multi_cell(maximun_shirina - 2 * Coord, 5, f'{num2words(int(total), lang="ru").capitalize()} рублей '
                                           f'{total_price[-2:].zfill(2)} копеек.')

    return height + 25

def footer(pdf: FPDF, **kwargs):
    def add_text(text, height):
        pdf.cell(10)
        height += 4 * len(pdf.multi_cell(maximun_shirina - 2 * Coord, 4, text, split_only=True))
        pdf.multi_cell(maximun_shirina - 2 * Coord, 4, text)
        return height
    height = kwargs['height'] + 10
    pdf.set_font("TimesNewRoman", size=8)
    pdf.set_y(height)
    height = add_text('Внимание!', height)
    height = add_text('Оплата данного счета означает согласие с условиями поставки товара.', height)
    height = add_text('Уведомление об оплате обязательно, в противном случае не гарантируется наличие товара на складе.', height)
    height = add_text('Товар отпускается по факту прихода денег на р/с Поставщика, самовывозом, при наличии доверенности и паспорта.', height)

    pdf.set_line_width(0.5)
    pdf.line(Coord, height + 4, maximun_shirina - Coord, height + 4)
    height += 10

    pdf.set_y(height)
    pdf.set_font("TimesNewRomanB", size=9)
    pdf.cell(10)
    pdf.cell(30, 5, 'Руководитель')
    pdf.set_font("TimesNewRoman", size=9)
    pdf.cell(60, 5, kwargs['director_name'], align='R')
    pdf.set_font("TimesNewRomanB", size=9)
    pdf.cell(30, 5, 'Бухгалтер', align='C')
    pdf.set_font("TimesNewRoman", size=9)
    pdf.cell(maximun_shirina - 2 * Coord - 120, 5, kwargs['buhgalter'], align='R')

    pdf.set_line_width(0.2)
    pdf.line(Coord + 35, height + 5, Coord + 90, height + 5)
    pdf.line(Coord + 120, height + 5, maximun_shirina - Coord, height + 5)

    return height

