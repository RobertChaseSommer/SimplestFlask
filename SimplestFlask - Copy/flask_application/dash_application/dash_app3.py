import dash
import dash_html_components as html

def Add_Dash(server):

    dash_app3 = dash.Dash(server=server, routes_pathname_prefix='/dash_app3/')

    dash_app3.layout = html.Div([
                                html.H1('TREE FIDDY APP BRUH'),
                                html.Div([
                                html.P('Dash converts Python classes into HTML'),
                                html.P('This conversion happens behind the scenes')
                                        ])
                                ])

    return dash_app3.server
