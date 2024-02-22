import regex as re
from jeraconv import jeraconv
from datetime import date

def convert_hiduke_format(jd):
    min_year = 1700
    current_year = int(date.today().year)

    jd = re.sub('[\s]', '', jd)
    if '年' not in jd:
        return ''
    j2w = jeraconv.J2W()
    full_date = jd
    j_year = str(correct_year(jd))
    j_month = correct_month(jd)
    j_day = correct_day(jd)
    d_year = str(digit_year(jd))
    f_year = str(f_digi(jd))
    print(j_year, d_year, f_year, j_month, j_day)
    if (j_year):
        year = j2w.convert(j_year)
        if min_year < int(year) < current_year:
            return str(year) + '年' + j_month + j_day
        return ''
        # return f' {str(j_month)}{str(j_day)}{str(year)} '
    elif (d_year):
        # year = j2w.convert(d_year)
        if min_year < int(d_year.strip('年')) < current_year:
            return f'{str(d_year)}{str(j_month)}{str(j_day)}'
        return ''
    elif f_year:
        if min_year < int(f_year.strip('年')) < current_year:
            return f'{str(f_year)}{str(j_month)}{str(j_day)}'
        return ''
    else:
        return ''
        # if '年' in str(full_date.strip()):
        #     return str(full_date.strip())
        # else:
        #     return ''


def correct_year(jd):
    year = re.search(r'(明示|明治|大正|昭和|平成|令和|大正元|平成元|明治元|大化|白雉|朱鳥|大宝|慶雲|和銅|霊亀|養老|神亀|天平|天平感宝|天平勝宝|天平宝字|天平神護|神護景雲|宝亀|天応|延暦|大同|弘仁|天長|承和|嘉祥|仁寿|斉衡|天安|貞観|元慶|仁和|寛平|昌泰|延喜|延長|承平|天慶|天暦|天徳|応和|康保|安和|天禄|天延|貞元|天元|永観|寛和|永延|永祚|正暦|長徳|長保|寛弘|長和|寛仁|治安|万寿|長元|長暦|長久|寛徳|永承|天喜|康平|治暦|延久|承保|承暦|永保|応徳|寛治|嘉保|永長|承徳|康和|長治|嘉承|天仁|天永|永久|元永|保安|天治|大治|天承|長承|保延|永治|康治|天養|久安|仁平|久寿|保元|平治|永暦|応保|長寛|永万|仁安|嘉応|承安|安元|治承|養和|寿永|元暦|文治|建久|正治|建仁|元久|建永|承元|建暦|建 保|承久|貞応|元仁|嘉禄|安貞|寛喜|貞永|天福|文暦|嘉禎|暦仁|延応|仁治|寛元|宝治|建長|康元|正嘉|正元|文応|弘長|文永|建治|弘安|正応|永仁|正安|乾元|嘉元|徳治|延慶|応長|正和|文保|元応|元亨|正中|嘉暦|元徳|元弘|正慶|建武|延元|興国|正平|建徳|文中|天授|弘和|元中|暦応|康永|貞和|観応|文和|延文|康安|貞治|応安|永和|康暦|永徳|至徳|嘉慶|康応|明徳|応永|正長|永享|嘉吉|文安|宝徳|享徳|康正|長禄|寛正|文正|応仁|文 明|長享|延徳|明応|文亀|永正|大永|享禄|天文|弘治|永禄|元亀|天正|文禄|慶長|元和|寛永|正保|慶安|承応|明暦|万治|寛文|延宝|天和|貞享|元禄|宝永|正徳|享保|元文|寛保|延享|寛延|宝暦|明和|安永|天明|寛政|享和|文化|文政|天保|弘化|嘉永|安政|万延|文久|元治|慶応|明治|大正|昭和|平成|令和|令和元)([0-9]*|[０-９]*)(年)', jd)
    if year:
        year = year.group()
    else:
        year = ''
    return str(year).strip()


def digit_year(jd):
    year = re.search(r'([0-9]{4}|[０-９]{4})[年]', jd)
    if year:
        year = year.group()
    else:
        year = ''
    return str(year).strip()


def f_digi(jd):
    year = re.search(r'([0-9]{4}|[０-９]{4})', jd)

    if year:
        year = year.group() + '年'
    else:
        year = ''
    return str(year).strip()


def correct_month(jd):
    month = re.search(r'([0-9]{1,2}|[０-９]{1,2})[月]', jd)
    if month:
        month = month.group()
    else:
        month = ''
    return str(month).strip()


def correct_day(jd):
    day = re.search(r'([0-9]{1,2}|[０-９]{1,2})[日]', jd)
    if day:
        day = day.group()
    else:
        day = ''
    return str(day).strip()

def split_end_date(colString):
    if '日' in colString:
        colString = re.split('日', colString)[0] + '日'
    elif '月' in colString:
        colString = re.split('月', colString)[0] + '月'
    elif '年' in colString:
        colString = re.split('年', colString)[0] + '年'
    return colString