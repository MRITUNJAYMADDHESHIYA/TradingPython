from dash import Dash, html
import dash_bootstrap_components as dbc
import random

risk_per_trade = 100
win_rate       = 0.5
rrr            = 2/1
num_trades     = 100
num_lines      = 10

profit_list = []
for i in range(num_trades):
    rand_num = random.random()
    print(i, rand_num)

    if rand_num < win_rate:
        profit = risk_per_trade * rrr
        print('win')
    else:
        profit = risk_per_trade * -1
        print('lose')

    profit_list.append(profit)

print(profit_list)


app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.layout = html.Div([html.H1('Monte Carlo Simulation App')
            
            ],style={'margin-left': '5%', 'margin-right': '5%', 'margin-top': '20px'})

if __name__ == '__main__':
    app.run()