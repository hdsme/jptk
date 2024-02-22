# Constants
import unicodedata
import re
from datetime import datetime
from japanera import EraDate


KANJI_NUMBERS = '一|二|三|四|五|六|七|八|九|十'

def convert_japan_date(japan_date_str):
    if not japan_date_str:
        return None

    try:
        japan_date_str =_normalize_date(japan_date_str)
        is_date =_is_valid_date(japan_date_str)

        if not is_date:
            return None

        year, month, day =_split_date(japan_date_str)
        formatYear, formatMonth, formatDay =_get_date_formats(japan_date_str, year, month, day)

        return _format_date(japan_date_str, formatYear, formatMonth, formatDay)

    except ValueError:
        print(f"Error: Input date is not in the expected format ({japan_date_str})")
        return None

def _normalize_date(japan_date_str):
    japan_date_str = unicodedata.normalize('NFKC', japan_date_str)
    return re.sub(' ', '', japan_date_str)

def _is_valid_date(japan_date_str):
    pattern = r'(明示|明治|大正|昭和|平成|令和)?(元|\d{1,4}|' + KANJI_NUMBERS + '{0,3})年(\d{0,2}|' + KANJI_NUMBERS + '{0,3})月(\d{0,2}|' + KANJI_NUMBERS + '{0,3})日'
    return re.search(pattern, japan_date_str)

def _split_date(japan_date_str):
    splitDate = japan_date_str.split("年")
    year = splitDate[0]
    splitDate = splitDate[1].split("月")
    month = splitDate[0]
    splitDate = splitDate[1].split("日")
    day = splitDate[0]
    return year, month, day

def _get_date_formats(japan_date_str, year, month, day):
    formatYear = '%Y' if japan_date_str[:1].isnumeric() and not re.search(KANJI_NUMBERS, year) else '%-n'
    formatMonth = '%m' if not re.search(KANJI_NUMBERS, month) else '%-m'
    formatDay = '%d' if not re.search(KANJI_NUMBERS, day) else '%-d'

    if not japan_date_str[:1].isnumeric():
        formatYear = '%-K' + ('%-n' if re.search(KANJI_NUMBERS, japan_date_str[2]) else '%-y')

    return formatYear, formatMonth, formatDay

def _format_date(japan_date_str, formatYear, formatMonth, formatDay):
    if (formatYear == '%Y' and formatMonth == '%m' and formatDay == '%d'):
        datetime_object = datetime.strptime(japan_date_str, "%Y年%m月%d日")
    else:
        datetime_object = EraDate.strptime(japan_date_str, formatYear + '年' + formatMonth + '月' + formatDay + '日')

    return datetime_object[0].strftime("%Y%m%d")