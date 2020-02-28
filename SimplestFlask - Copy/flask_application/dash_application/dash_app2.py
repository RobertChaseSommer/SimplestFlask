import dash
import dash_html_components as html

def Add_Dash(server):

    dash_app2 = dash.Dash(server=server, routes_pathname_prefix='/dash_app2/')

    dash_app2.layout = html.Div([
                                html.H1('SECOND APP BRUH'),
                                html.Div([
                                html.P('Dash converts Python classes into HTML'),
                                html.P('This conversion happens behind the scenes')
                                        ])
                                ])

    return dash_app2.server
