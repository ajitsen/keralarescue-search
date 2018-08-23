from io import StringIO
import pandas as pd

from common.logger import log
from common.utils import get_data_from_url

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def pandas_read_tsv_str(csv_str):
    return pd.read_csv(StringIO(csv_str), sep="\t")


def load_sheet_tsv_as_panda_df(sheet_url, cache):
    tsv_str = get_data_from_url(sheet_url, cache=cache)
    dataf = pandas_read_tsv_str(tsv_str)
    log("Loaded data from ")
    log(dataf.shape)
    log(dataf.columns)
    return dataf


def show_all_in_print():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', -1)
