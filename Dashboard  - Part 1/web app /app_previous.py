import pandas as pd
import dash
from dash import html
import plotly.graph_objects as go
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
from dash import Dash, dash_table
from collections import OrderedDict

df = pd.read_csv('Skincare Ratings - SPF.csv')

df[' index'] = range(1, len(df) + 1)

app = Dash(__name__)

PAGE_SIZE=20

    
app.layout = dash_table.DataTable(
    
        id='table-sorting-filtering',

        columns=[
        {'name': i, 'id': i, 'deletable': True} for i in df.columns ],

        #data=df.to_dict('records'),
    
        
        style_cell={
            'fontSize':14,
            'textAlign': 'left',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'maxWidth': 400},


        style_cell_conditional=[
            {'if': {'column_id': 'Ranking'},
             'width': '80px'},
            {'if': {'column_id': 'Market'},
             'width': '80px'} ,   
             {'if': {'column_id': 'Quantity per unit'},
             'width': '80px'},
            {'if': {'column_id': 'Price per unit'},
             'width': '80px'} ,  
             {'if': {'column_id': 'Price per ml'},
             'width': '80px'},
            {'if': {'column_id': 'SPF Strenght'},
             'width': '80px'} ,  
            {'if': {'column_id': 'Alcohol Free'},
             'width': '80px'},
            {'if': {'column_id': 'Fragrance/Essential Oils Free'},
             'width': '80px'} ,   
             {'if': {'column_id': 'Sensitive Skin friendly'},
             'width': '80px'},
            {'if': {'column_id': 'Oily Skin friendly'},
             'width': '80px'} ,  
             {'if': {'column_id': 'Pilling-Off'},
             'width': '80px'},
            {'if': {'column_id': 'SPF Strenght'},
             'width': '80px'} , 
            {'if': {'column_id': 'SPF effectiveness'},
             'width': '80px'},
            {'if': {'column_id': 'Ingredient List '},
             'width': '80px'} ,   
             {'if': {'column_id':'TargetGroup/Use Cases'},
             'width': '80px'},
            {'if': {'column_id': 'Wearability ' },
             'width': '80px'} ,  
             {'if': {'column_id': 'Price point ' },
             'width': '80px'},
            {'if': {'column_id': 'Acessability' },
             'width': '80px'},
            {'if': {'column_id': 'Score ' },
             'width': '80px'} 
            ],

        style_header={
            'backgroundColor': 'rgb(210, 210, 210)',
            'color': 'black',
            'fontWeight': 'bold'},

        style_data={

            #'whiteSpace': 'normal',
            'height': 'auto',
            #'lineHeight': '15px',
            'color': 'black',
            'backgroundColor': 'white'},

         style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(220, 220, 220)',}],
        
        tooltip_header={i: i for i in df.columns},

        tooltip_data=[
            {
                column: {'value': str(value), 'type': 'markdown'}
                for column, value in row.items()
            } for row in df.to_dict('records')],

        tooltip_duration=None,
    
        fixed_rows={'headers': True},
    
        page_current= 0,
        page_size= PAGE_SIZE,
        page_action='custom',

        filter_action='custom',
        filter_query='',

        sort_action='custom',
        sort_mode='multi',
        sort_by=[]
    
        )


operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]


def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                # word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value

    return [None] * 3

@app.callback(
    Output('table-sorting-filtering', 'data'),
    Input('table-sorting-filtering', "page_current"),
    Input('table-sorting-filtering', "page_size"),
    Input('table-sorting-filtering', 'sort_by'),
    Input('table-sorting-filtering', 'filter_query'))
def update_table(page_current, page_size, sort_by, filter):
    filtering_expressions = filter.split(' && ')
    dff = df
    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            # these operators match pandas series operator method names
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff = dff.loc[dff[col_name].str.contains(filter_value)]
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff = dff.loc[dff[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )

    page = page_current
    size = page_size
    return dff.iloc[page * size: (page + 1) * size].to_dict('records')


if __name__ == '__main__':
    
        app.run_server(debug=True, use_reloader=False)
                
