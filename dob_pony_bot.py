import csv
from datetime import datetime

# 🎯 Configurable threshold for DOB (Double or Bust)
DOB_THRESHOLD = 0.5  # 50% drop = safe back-to-lay

# 📂 Load data from CSV
DATA_PATH = 'data/historical_races.csv'

def load_data(path):
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def format_row(row):
    horse = row['HorseName']
    race_date = datetime.strptime(row['RaceDate'], '%Y-%m-%d').strftime('%d %b %Y')
    bsp = float(row['BSP'])
    inplay = float(row['InPlayLow'])
    dob_hit = inplay <= bsp * DOB_THRESHOLD
    result_icon = '✅' if dob_hit else '❌'
    percentage = round(100 * (1 - inplay / bsp), 2)

    return f"{result_icon} {horse} ({race_date})\n  - BSP: {bsp} | In-Play Low: {inplay} | Drop: {percentage}%"

def analyze_dob_opportunities():
    races = load_data(DATA_PATH)
    print("\n🏇 BACK-TO-LAY DOB ANALYSIS\n---------------------------")
    for race in races:
        print(format_row(race))

if __name__ == '__main__':
    analyze_dob_opportunities()
