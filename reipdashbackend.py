# Backend Script for v1 REIP Snapshot Dashboard

# packages needed
import pandas as pd
import os
from dotenv import load_dotenv
from fredapi import Fred

load_dotenv()  # load ENV

fred = Fred(api_key="16ddd24c75c3c94d71d755434d87d30a")
df = fred.get_series_all_releases("WPUSI012011")
df.tail()

cppiData = pd.read_excel(
    r"C:\Users\mtanner\OneDrive - King Operating\Documents 1\code\reipdashbackend\data\greenstreet\greenstreetcppiMaster.xlsx")

print("yay")
