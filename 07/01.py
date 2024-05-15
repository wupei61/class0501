import pygsheets
import pandas as pd

gc = pygsheets.authorize(service_account_file='aa.json')

survey_url = 'https://docs.google.com/spreadsheets/d/1mHMlDNMD7czM91fQaQept0rKo44nXCZ1-JJI8L7mOT4/'


sh = gc.open_by_url(survey_url)

ws = sh.worksheet_by_title('chu')
ws.update_value('A1', '中華大學')
ws.update_value('B1', '影像處理')
df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
ws.set_dataframe(df1, 'A3', copy_index=True, nan='')