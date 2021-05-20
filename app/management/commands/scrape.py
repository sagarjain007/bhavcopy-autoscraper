from django.core.management.base import BaseCommand

from io import BytesIO
from datetime import date, datetime
from zipfile import ZipFile
from urllib.request import urlopen, Request
import pandas as pd

from app.models import StockData, updateLogs

class Command(BaseCommand):
    help = "Get Stock Data"

    def handle(self, *args, **options):
        d = datetime.today()
        scrape = True

        if(d.weekday() == 5 or d.weekday() == 6):
            scrape = False

        if(scrape):
            url = 'https://www.bseindia.com/download/BhavCopy/Equity/EQ'+d.strftime('%d%m%y')+'_CSV.ZIP'
            #url = 'https://www.bseindia.com/download/BhavCopy/Equity/EQ120521_CSV.ZIP'
            try:
                req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
                web_byte = urlopen(req)
                zipfile = ZipFile(BytesIO(web_byte.read()))

                df = pd.read_csv(zipfile.open(zipfile.namelist()[0]))
                df.drop(columns=['SC_GROUP','SC_TYPE','LAST', 'PREVCLOSE', 'NO_TRADES', 'NO_OF_SHRS', 'NET_TURNOV', 'TDCLOINDI'],inplace=True)
                try:
                    if StockData.objects.all().count() > 0:
                        StockData.objects.all().delete()
                    for ind,row in df.iterrows():
                        StockData.objects.update_or_create(code=row['SC_CODE'],name=row['SC_NAME'],open_price=row['OPEN'],high_price=row['HIGH'],low_price=row['LOW'],close_price=row['CLOSE'])
                        updateLogs.objects.create(update_date = d.date())
                    print("BHAVCOPY ADDED TO DB")
                except Exception as e:
                    pass
            except:
                print('Data is alredy up to date')
                pass        
