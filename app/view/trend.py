from flask import render_template, request
from flask_login import login_required

from app import trend_crawler as tc

from . import main

@main.route('/trend', methods=['GET', 'POST'])
@login_required
def trend_index():
    df = tc.get_df()

    ttd = tc.get_today_trend_dc(df)

    ytd = tc.get_yesterday_trend_dc(df)

    etd = tc.get_energy_trend_dc(df)

    nd = tc.get_nice_dc(df)

    return render_template(
            'trend.html', data = [ttd, ytd, etd, nd,]            
        )