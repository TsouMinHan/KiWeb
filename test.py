from app.models import NewsDB, GalleryDB, MainDB, LogDB
from app import trend_crawler as tc

if __name__ == '__main__':
    df = tc.get_df()

    ttd = tc.get_today_trend_dc(df)

    ttd = tc.get_yesterday_trend_dc(df)

    ttd = tc.get_energy_trend_dc(df)

    ttd = tc.get_nice_dc(df)

    print(ttd)