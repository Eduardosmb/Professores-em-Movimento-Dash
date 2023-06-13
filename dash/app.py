from dash import Dash, html, dcc
import dash

font_awesome = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"
external_stylesheets = [font_awesome]

app = Dash(__name__, use_pages=True, external_stylesheets = external_stylesheets)

app.layout = html.Div([
    html.P([
                dcc.Link(f"", href=page["relative_path"], className="link")
            for page in dash.page_registry.values()], ),
	dash.page_container, 
])

if __name__ == '__main__':
	app.run_server(debug=False)
    
