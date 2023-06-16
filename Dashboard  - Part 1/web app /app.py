import pandas as pd
import numpy as np
import dash
from dash import html
import plotly.graph_objects as go
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
from dash import Dash, dash_table
from collections import OrderedDict
import dash_bootstrap_components as dbc

# Import Dash DataTable input Data
table_df = pd.read_csv('dash_table_spf')
table_df.drop(table_df.columns[0], axis=1, inplace=True)
table_df['Price/ml'] = table_df['Price/ml'].map('{:.2f}'.format)
table_df['Price(€)'] = table_df['Price(€)'].map('{:.2f}'.format)
table_df['Quantity(ml)'] = table_df['Quantity(ml)'].map('{:.1f}'.format)

new_table_df = table_df.drop(columns={'Brand'})

# Import Similarity Matrix Results necessary for the recommender engine
sim_matrix = pd.read_csv('similarity_matrix')
sim_matrix.drop(sim_matrix.columns[0], axis=1, inplace=True)

# Import Spider Radar Input Data
score_df = pd.read_csv('ingredient_score')
spider_df = score_df.drop(
    columns=['Category', 'Market', 'ingredient_list', 'cleaned_list'])
spider_df = pd.melt(spider_df, id_vars=['Brand', 'Product'], value_vars=['sunscreen', 'soothing', 'humectants', 'antimicrobial/antibacterial',
                    'skin-identical-ingredient', 'brightening', 'exfoliants', 'emollients', 'cell-communicating-ingredient', 'antioxidant', 'anti-acne'])
spider_df = spider_df.rename(columns={
                             'Brand': 'brand', 'Product': 'product', 'variable': 'benefits', 'value': 'score'})
spider_df['product'] = spider_df['product'].astype(str).str.replace(' ', '')

# Create Spider Radar Default figure
#fig = px.line_polar(spider_df, r='score', theta='benefits', line_close=True)
# fig.update_traces(fill='toself')

fig = go.Figure(
    go.Scatterpolar(
        r=[],
        theta=[],
        mode='lines',
        fill='toself'
    ),
    layout=go.Layout(
        polar=dict(
            radialaxis=dict(showticklabels=False, ticks=''),
            angularaxis=dict(showticklabels=False, ticks='')
        )

    )
)
PAGE_SIZE = 20

app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

app.layout = dbc.Container([

    dbc.Row([dbc.Col(

        html.H1('Skincare Product Analysis Dashboard',
                className='text-center text-primary, p-3'),
        width=12)]),

    dbc.Row([
        dbc.Col([
            html.H6('Please Select a Brand'),
            dcc.Dropdown(id='dropdown_brand',
                         options=table_df['Brand'].unique(),
                         value='',
                         multi=False,
                         clearable=False)
        ]),

        dbc.Col([
            html.H6('Please Select a Product'),
            dcc.Dropdown(id='dropdown_product',
                         options=[],
                         value=[],
                         multi=False)
        ])

    ], className='my-5'),

    dbc.Row([
        dbc.Col([
                html.H4('Active Ingredients Profile'),
                html.Br(),
                html.H6('This chart displays the count of product ingredients based on their roles/benefits, as classified by https://incidecoder.com', id='hover_title_1', style={'width': '85%'}
                        ),
                dcc.Graph(id='spider_radar_result', figure=fig

                          )]),

        dbc.Col([
                html.H4(id='recommender_title'),
                html.Br(),
                html.H6('The Similarity Factor, computed from common active ingredients, indicates the level of likeness with the selected product: higher values imply more actives in common.',
                        id='hover_title_2', style={'width': '85%'}),
                dcc.Graph(id='recommender_result',
                          figure=go.Figure(data=[go.Table(header=dict(values=['Product', 'Similarity Factor']),
                                                          cells=dict(
                                                              values=['NA', 'NA'])
                                                          )
                                                 ]))])

    ]),
    html.H3('Product Comparison Table'),
    html.Br(),
    dash_table.DataTable(

        id='table-sorting-filtering',
        columns=[{'name': i, 'id': i, 'deletable': False}
                 for i in new_table_df.columns],

           data=new_table_df.to_dict('records'),

        style_cell={
            'fontSize': 14,
            # 'textAlign': 'right',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'maxWidth': 180
        },

        style_cell_conditional=[
            {'if': {'column_id': 'Category'},
                'width': '80px', 'textAlign': 'center'},
            {'if': {'column_id': 'Market'}, 'width': '80px', 'textAlign': 'center'},
            # {'if': {'column_id': 'Brand'}, 'width': '80px', 'textAlign': 'left'},
            {'if': {'column_id': 'Product'}, 'width': '80px', 'textAlign': 'left'},
            {'if': {'column_id': 'Quantity(ml)'},
             'width': '80px', 'textAlign': 'right'},
            {'if': {'column_id': 'Price(€)'},
             'width': '80px', 'textAlign': 'right'},
            {'if': {'column_id': 'Price/ml'}, 'width': '80px', 'textAlign': 'right'},
            {'if': {'column_id': 'Full_Ingredient_List'},
                'width': '120px', 'textAlign': 'right'},

        ],

        style_header={
            'backgroundColor': 'rgb(210, 210, 210)',
            'color': 'black',
            'fontWeight': 'bold',
            'textAlign': 'center'
        },

        style_data={

            # 'whiteSpace': 'normal',
            'height': 'auto',
            'lineHeight': '5px',
            'color': 'black',
            'backgroundColor': 'white'

        },

        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(220, 220, 220)', }],

        tooltip_header={i: i for i in table_df.columns},

        css=[{
             'selector': '.dash-table-tooltip',
             'rule': 'max-width: 800px; height: auto; white-space: normal;background-color: white; color: black; font-size: 12px;'
             }],

        tooltip_data=[
            {
                column: {'value': str(value), 'type': 'markdown'}
                for column, value in row.items()
            } for row in table_df.to_dict('records')],


        tooltip_duration=None,
        fixed_rows={'headers': True},
        page_current=0,
        page_size=PAGE_SIZE,
        page_action='custom',
        filter_action='custom',
        filter_query='',
        sort_action='custom',
        sort_mode='multi',
        sort_by=[])
])
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
    Output('dropdown_product', 'options'),
    Input('dropdown_brand', 'value')
)
def select_brand_options(chosen_brand):
    dffd = table_df[table_df['Brand'] == chosen_brand]
    return [{'label': i, 'value': i} for i in sorted(dffd['Product'].unique())]
   # sorted(dffd['Product'].unique())
   # [{'label': c, 'value': c} for c in ]


@app.callback(
    Output('dropdown_product', 'value'),
    Input('dropdown_product', 'options'))
def select_product(available_options):
    # print(available_options)
    return []  # [x['value'] for x in available_options]


@app.callback(
    Output('spider_radar_result', 'figure'),
    Input('dropdown_product', 'value')
)
def update_spider_chart(chosen_product):
    cp = []
    cp = chosen_product

    spider_updated = spider_df[spider_df['product'] == cp]

    fig_new = go.Figure(
        go.Scatterpolar(
            r=spider_updated['score'],
            theta=spider_updated['benefits'],
            mode='lines',
            fill='toself',
            #hovertemplate= "%{theta}: <br>Popularity: %{r}<extra></extra>"
            # hoverinfo='skip'

        )
    )

    fig_new.update_layout(
        polar=dict(
            radialaxis=dict(
                tickmode='array',
                tickvals=list(range(0, 12)),
                tick0=0,    # starting tick value
                dtick=1
                # range=[0, 12]
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color='black'),
                ticklen=16,
                tickwidth=8,)


        )
    )
    #fig_new.update_traces( mode="markers+lines")

    return fig_new


@app.callback(
    Output('recommender_title', 'children'),
    Input('dropdown_product', 'value')

)
def update_recommender_title(product_name):
    return f'Recommending products similar to {product_name}:'


@app.callback(
    Output('recommender_result', 'figure'),
    Input('dropdown_product', 'value')
)
def recommender(product_input):
    idx = table_df[table_df['Product'] == product_input].index[0]
    binary_list = list(sim_matrix.iloc[idx][1:])
    point1 = np.array(binary_list)
    prod_type = table_df.loc[idx, 'Category']
    brand_search = table_df.loc[idx, 'Brand']
    data_by_type = table_df[table_df['Category'] == prod_type].copy()
    cs_list = []

    for j in data_by_type.index:
        binary_list2 = list(sim_matrix.iloc[j][1:])
        point2 = np.array(binary_list2)
        cos_sim = np.dot(point1, point2) / \
            (np.linalg.norm(point1) * np.linalg.norm(point2))
        cs_list.append(cos_sim)

    data_by_type['cos_sim'] = cs_list
    data_by_type.sort_values('cos_sim', ascending=False, inplace=True)
    data_by_type = data_by_type[data_by_type['Product'] != product_input]
    brands = []
    output = []

    for _, row in data_by_type.iterrows():
        brand = row['Brand']
        if brand != brand_search and brands.count(brand) < 2:
            brands.append(brand)
            output.append(row)

    df_output = pd.DataFrame(output)
    df_output['cos_sim'] = df_output['cos_sim'].round(2)
    top_results = df_output[['Product', 'cos_sim']].head(10)
    recommender_fig = go.Figure(data=[go.Table(
        header=dict(values=['Product', 'Similarity Factor'],
                    font=dict(size=13), align='left'),
        cells=dict(values=[top_results.Product, top_results.cos_sim], font=dict(
            size=13),  align='left'),
        columnwidth=[2.5, 1]
    )])

    return recommender_fig


@app.callback(
    Output('table-sorting-filtering', "data"),
    Output('table-sorting-filtering', "tooltip_data"),  # new Output
    Input('table-sorting-filtering', "page_current"),
    Input('table-sorting-filtering', "page_size"),
    Input('table-sorting-filtering', "sort_by"),
    Input('table-sorting-filtering', "filter_query")
)
def update_table(page_current, page_size, sort_by, filter):
    filtering_expressions = filter.split(' && ')
    dff = table_df
    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff = dff.loc[dff[col_name].str.contains(filter_value)]
        elif operator == 'datestartswith':
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
    page = dff.iloc[page_current*page_size:(page_current + 1)*page_size]

    tooltip_data = [
        {
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        } for row in page.to_dict('records')
    ]

    return page.to_dict('records'), tooltip_data


if __name__ == '__main__':

    app.run_server(debug=False, use_reloader=False)
