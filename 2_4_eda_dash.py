# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 18:22:02 2022

@author: s_eze
"""
# Libraries
import pandas as pd
import numpy as np
# Plotting
import plotly.express as px
from plotly.subplots import make_subplots
# Dashing
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
# displaying html
from IPython.core.display import display, HTML

#Colors
_BRAND__colors_f2 = ['#ffc0cb', '#6f54e8', '#191ffb', '#7b99ed', '#c5c9a3', '#f3ac21', '#ff5d00', '#ff0000']
_BRAND__colors_l = ['#ffc0cb', '#ebb1cf', '#d7a2d3', '#c393d7', '#af84db', '#9b75df', '#8766e3', '#7357e8', '#5f48ec', '#4735f1', '#3326f5', '#1f17f9', '#0b08fd', '#0608fe', '#1419fc', '#212afa', '#2f3af8', '#3f4ff6', '#4d60f4', '#5a71f2', '#6882f0', '#7593ee', '#83a3ec', '#91b4ea', '#9ec5e8', '#aed8e4', '#b4d4d2', '#bbd0c0', '#c1ccae', '#c7c89c', '#cec48a', '#d4c078', '#dbbc66', '#e1b854', '#e9b33e', '#efaf2c', '#f6ab1a', '#fca708', '#ff9e00', '#ff9100', '#ff8400', '#ff7700', '#ff6800', '#ff5b00', '#ff4e00', '#ff4100', '#ff3400', '#ff2700', '#ff1a00', '#ff0d00', '#ff0000']

colors = _BRAND__colors_l 

# get data from folder
df = pd.read_excel('./Encuesta sobre Acufenometría.xlsx')

# -------------------------------- a) DATA CLEANING -------------------------------- 
# a-1) DataFrame con: Nombre y Apellido y Estados_de_USA
# Building dataframe for users
df_users = df[['Nombre y Apellido', 'Estados_de_USA']]
# print('Cantidad de celdas con valores "null":\n ')
df_users.isna().sum()
# Capitalizing first letters of each word.
df_users.loc[:, 'Nombre y Apellido'] = df_users.loc[:, 'Nombre y Apellido'].apply(lambda x: x.lower().title())
df_users.loc[:, 'Estados_de_USA'] = df_users.loc[:, 'Estados_de_USA'].apply(lambda x: x.lower().title())
# Removing spaces and other extra characters to standarize 'Estados_de_USA' data.
df_users['Estados_de_USA'].unique()
string = df_users['Estados_de_USA'].unique()[0]
for item in df_users['Estados_de_USA'].unique():
    df_users['Estados_de_USA'] = df_users['Estados_de_USA'].apply(lambda x: item if (item in x) and (len(item)<len(x)) else x)
# Cantidad de celdas duplicadas eliminadas:
df_users_with_duplicates = df_users
df_users = df_users.drop_duplicates()
# print('Cantidad de celdas duplicadas eliminadas: ' + str(len(df)-len(df_users)))
# df_users.head(5)

# a-2) DataFrame con: Nombre y Apellido, Estados_de_USA y las respuestas y ¿En que área principalmente desarrollas tu profesión?(Si quieres ingresar más de una opción por favor ingresa las opciones en el campo "Otros").¶
# Building dataframe for sectors
df_sector = df_users_with_duplicates[['Nombre y Apellido', 'Estados_de_USA']]
df_sector['sector'] = df[['¿En que área principalmente desarrollas tu profesión? (Si quieres ingresar más de una opción por favor ingresa las opciones en el campo "Otros")']]
# print('Cantidad de celdas con valores "null":\n ')
df_sector.isna().sum()
df_sector = df_sector.drop_duplicates()
len(df)-len(df_sector)
# print('Cantidad de celdas duplicadas eliminadas: ' + str(len(df)-len(df_sector)))
# Original options in the survey.
list_sector= ['Medicina Laboral',
              'Tratamiento del lenguaje en niños',
              'Tratamiento del lenguaje en adultos',
              'Audiología en adultos',
              'Audiología en niños',
              'Adaptación de prótesis auditivas']
# 'Docencia' is added after analyzing the data
list_sector.append('Docencia')
df_sector[list_sector] = 0

for i,item in enumerate(df_sector['sector']):
    string = item.lower()
    string = string.replace(' en',' ').replace(' del',' ').replace(' de',' ').replace(' y',',').replace('  ',' ')
    
    # When 'Laboral' is mentioned (i.e. Laboral , rehabilitación niños y adulto , audífonos , Audiología	)
    if 'medicina laboral' in string or 'laboral' in string:
        df_sector['Medicina Laboral'].iloc[i]=1
    # When 'Prótesis' is mentioned (i.e. Audiología y adaptación de prótesis auditivas	)
    if 'prót' in string or 'prot' in string or 'audífono' in string or 'audifono' in string:
        df_sector['Adaptación de prótesis auditivas'].iloc[i]=1
    # When 'Docencia' is in mentioned(i.e. Audiologia clinica en adultos, niños y protesis auditivas y docencia en la universodad catolica de salta en la materia terapeutica audiologica	)
    if 'docencia' in string:
        df_sector['Docencia'].iloc[i]=1
    # When 'niño' is mentioned, it is parsed to understand if it is connected to 'Audiología' or 'Tratamiento del lenguaje' (i.e.'Audiología en niños'; 'Audiologia adultos, niños, laboral y tratamiento delLenguaje adultos y niños')
    if 'ños' in string:
        if 'trat' in string.split('ños')[0] or 'rehab' in string.split('ños')[0] or 'leng' in string.split('ños')[0]:
            df_sector['Tratamiento del lenguaje en niños'].iloc[i]=1
        elif len(string.split('ños'))>2:
            if 'trat' in string.split('ños')[1] or 'rehab' in string.split('ños')[1] or 'leng' in string.split('ños')[1]:
                df_sector['Tratamiento del lenguaje en niños'].iloc[i]=1
        if 'audiología' in string.split('ños')[0] or 'audiologia' in string.split('ños')[0] or 'audio ' in string.split('ños')[0]:
            df_sector['Audiología en niños'].iloc[i]=1
        elif len(string.split('ños'))>2:
            if 'audiología' in string.split('ños')[1] or 'audiologia' in string.split('ños')[1] or 'audio ' in string.split('ños')[1] or 'audiometria' in string.split('ños')[1] or 'audiometría' in string.split('ños')[1]:
                df_sector['Audiología en niños'].iloc[i]=1
        # When it is called 'niños' as area of expertise, but it is not specified whether it corresponds to 'Audiología' or 'Tratamiento del lenguaje'
        if string=='niños':
            df_sector['Tratamiento del lenguaje en niños'].iloc[i]=1
            df_sector['Audiología en niños'].iloc[i]=1
    # When 'adulto' is mentioned, it is parsed to understand if it is connected to 'Audiología' or 'Tratamiento del lenguaje' (i.e.'Audiología en adultos'; 'Audiologia adultos, niños, laboral y tratamiento delLenguaje adultos y niños')
    if 'adult' in string:
        if 'trat' in string.split('adult')[0] or 'rehab' in string.split('adult')[0] or 'leng' in string.split('adult')[0]:
            df_sector['Tratamiento del lenguaje en adultos'].iloc[i]=1
        elif len(string.split('adult'))>2:
            if 'trat' in string.split('adult')[1] or 'rehab' in string.split('adult')[1] or 'leng' in string.split('adult')[1]:
                df_sector['Tratamiento del lenguaje en adultos'].iloc[i]=1
        if 'audiología' in string.split('adult')[0] or 'audiologia' in string.split('adult')[0] or 'audio ' in string.split('adult')[0]:
            df_sector['Audiología en adultos'].iloc[i]=1
        elif len(string.split('adult'))>2:
            if 'audiología' in string.split('adult')[1] or 'audiologia' in string.split('adult')[1] or 'audio ' in string.split('adult')[1]:
                df_sector['Audiología en adultos'].iloc[i]=1
    # When there are 'adulto' or 'niño' mentioned but no for 'AUDIOLOGÍA' that stay not specified (i.e. 'Lenguaje de niños y audiología en todas las edades').
    if 'adult' in string or 'ños' in string: 
        if len(string.split('ños')[len(string.split('ños'))-1]) > len(string.split('adult')[len(string.split('adult'))-1]):
            if 'audiología' in string.split('adult')[len(string.split('adult'))-1] or 'audiologia' in string.split('adult')[len(string.split('adult'))-1] or 'audio ' in string.split('adult')[len(string.split('adult'))-1]:
                df_sector['Audiología en adultos'].iloc[i]=1
                df_sector['Audiología en niños'].iloc[i]=1
        else:
            if 'audiología' in string.split('ños')[len(string.split('ños'))-1] or 'audiologia' in string.split('ños')[len(string.split('ños'))-1] or 'audio ' in string.split('ños')[len(string.split('ños'))-1] or 'audiometria' in string.split('ños')[len(string.split('ños'))-1] or 'audiometría' in string.split('ños')[len(string.split('ños'))-1]:
                df_sector['Audiología en niños'].iloc[i]=1
                df_sector['Audiología en adultos'].iloc[i]=1
    # When there are no 'adulto' or 'niño' mentioned, so 'AUDIOLIGÍA' is not specified(i.e. 'Audiología y adaptación de prótesis auditivas').
    if not('adult' in string) and not('ños' in string): 
        if 'audiología' in string or 'audiologia' in string:
            df_sector['Audiología en adultos'].iloc[i]=1
            df_sector['Audiología en niños'].iloc[i]=1
# Ordenando columnas dummy desde el área de especialización más usual entre los doctores entrevistados
# Sorting the columns from the one with the most "frequency" to the one with the least
list_sect_sorted = pd.DataFrame(df_sector[list_sector].sum().sort_values(ascending=False)).index.tolist()
# Adding first columns
list_sorted = []; list_sorted.extend(list_sect_sorted)
list_sorted.insert(0, 'Estados_de_USA')
list_sorted.insert(0, 'Nombre y Apellido')
df_sector_max_min = df_sector[list_sorted]
# df_sector_max_min.head(5)
# Lista en el orden original
df_sector = df_sector.drop('sector', axis = 1)
# df_sector.head(5)

# a-3) DataFrame con: Nombre y Apellido, Estados_de_USA y las respuestas y Respecto a los estímulos utilizados para COMPARAR el acúfeno, éstos pueden ser...
# Building dataframe for sounds
df_sound = df_users_with_duplicates[['Nombre y Apellido', 'Estados_de_USA']]
df_sound['sound'] = df[['Respecto a los estímulos utilizados para COMPARAR el acúfeno, éstos pueden ser...']]
# print('Cantidad de celdas con valores "null":\n ')
df_sound = df_sound.dropna()
df_sound.isna().sum()
df_sound = df_sound.drop_duplicates()
# len(df)-len(df_sound)
# print('Cantidad de celdas duplicadas eliminadas: ' + str(len(df)-len(df_sound)))
# Original options in the survey.
list_sound=['Tono Puro',
            'Ruido de Banda Estrecha',
            'Ruido Blanco',
            'Ruido Rosa',
            'Ruido de Banda Ancha',
            'Ruido Vocal',
            'Tono Modulado (warble tone)']
# making dommies
for item in list_sound:
    df_sound[item] = df_sound['sound'].apply(lambda x: 1 if item.lower() in x.lower() else 0)
# Ordenando columnas dummy según Estímulos para comparar Acúfenos más usuales entre los doctores entrevistados.
# Sorting the columns from the one with the most "frequency" to the one with the least
list_sound_sorted = pd.DataFrame(df_sound[list_sound].sum().sort_values(ascending=False)).index.tolist()
# Adding first columns
list_sorted = []; list_sorted.extend(list_sound_sorted)

list_sorted.insert(0, 'Estados_de_USA')
list_sorted.insert(0, 'Nombre y Apellido')

df_sound_max_min = df_sound[list_sorted]
# df_sound_max_min.head(5)
df_sound = df_sound.drop('sound', axis = 1 )
# df_sound.head(5)





# -------------------------------- c) DASH -------------------------------- 

# Plots for tab "VISTA GENERAL"-------------------------------- 
df_prof_by_country_perc = (df_sector['Estados_de_USA'].value_counts()/df_sector['Estados_de_USA'].value_counts().sum())

    # Summing the number of "development areas" per row.
df_sector['areas_by_country'] = df_sector[list_sector].sum(axis=1)
    # Summing the number of "development areas" by country. (It is made like this instead of with groupby beacause it is preferred the same sort as the plot aside "professionals by country")
list_areas_by_country = []
for item in df_sector['Estados_de_USA'].value_counts().index:
    list_areas_by_country.append(df_sector[df_sector['Estados_de_USA']==item]['areas_by_country'].sum())
    # Making a df with quantities of "development areas"
df_areas_by_country = pd.DataFrame({'areas_by_country': list_areas_by_country}, index = df_sector['Estados_de_USA'].value_counts().index)
df_sector = df_sector.drop(columns='areas_by_country')
df_areas_by_country_perc =(df_areas_by_country/df_areas_by_country.sum())

df_sound['sound_by_country'] = df_sound[list_sound].sum(axis=1)
    # Summing the number of "development areas" by country.
list_sound_by_country = []
for item in df_sound['Estados_de_USA'].value_counts().index:
    list_sound_by_country.append(df_sound[df_sound['Estados_de_USA']==item]['sound_by_country'].sum())
    # Making a df with quantities of "development areas"
df_sound_by_country = pd.DataFrame({'sound_by_country': list_sound_by_country}, index = df_sound['Estados_de_USA'].value_counts().index)
df_sound = df_sound.drop(columns='sound_by_country')
df_sound_by_country_perc =(df_sound_by_country/df_sound_by_country.sum())
    # Determining a subplot grid.
fig_overview = make_subplots(rows=2, cols=2, specs=[ [{'type':'domain', 'colspan': 2}, None],[{'type':'domain'}, {'type':'domain'}] ], subplot_titles=("Profesionales por Estados_de_USA", "Áreas de desarrollo por Estados_de_USA", "Estímulos en ecufenometría por Estados_de_USA"))
    # Plotting
fig_p_ProfCou = px.pie(df_prof_by_country_perc, values=df_prof_by_country_perc.values, names=df_prof_by_country_perc.index)#, hole=.3)
fig_p_ArCou = px.pie(df_areas_by_country_perc, values=df_areas_by_country_perc.areas_by_country.values, names=df_areas_by_country_perc.index)#, hole=.3)
fig_p_SouCou = px.pie(df_sound_by_country_perc, values=df_sound_by_country_perc.sound_by_country.values, names=df_sound_by_country_perc.index)#, hole=.3)
    # Colors
fig_p_ProfCou.update_traces(textposition='inside', textinfo='percent', pull=[0.06, 0.06, 0.02, 0.02, 0.02, 0.02, 0.02], marker=dict(colors=colors), rotation=0)
fig_p_ArCou.update_traces(textposition='inside', textinfo='percent', pull=[0.06, 0.06, 0.02, 0.02, 0.02, 0.02, 0.02], marker=dict(colors=colors), rotation=0)
fig_p_SouCou.update_traces(textposition='inside', textinfo='percent', pull=[0.06, 0.06, 0.02, 0.02, 0.02, 0.02, 0.02], marker=dict(colors=colors), rotation=0)
        # ['label', 'text', 'value', 'percent'] 
    # Placing plots in the subplot grid
for trace in fig_p_ProfCou.data:
    fig_overview.add_trace(trace, 1, 1)
for trace in fig_p_ArCou.data:
    fig_overview.add_trace(trace, 2, 1)
for trace in fig_p_SouCou.data:
    fig_overview.add_trace(trace, 2, 2)
    # Setting yaxe
fig_overview.update_layout(paper_bgcolor='#F9F9F9', autosize=True,  height=850)#width=1240,



# Plots for tab "ÁREAS DE DESARROLLO POR Estados_de_USA."-------------------------------- 
# Sorting areas from most usual to less.
df_sector_gb = df_sector.groupby("Estados_de_USA").sum()
df_sector_gb_T = df_sector_gb.T
df_sector_gb_T['countries_by_areas'] = df_sector_gb_T[df_sector['Estados_de_USA'].unique()].sum(axis=1)
list_areas = []
list_areas.extend(df_sector_gb_T.sort_values(by='countries_by_areas',ascending=False).index[:])
max_y_val_sector=df_sector_gb_T.sort_values(by='countries_by_areas',ascending=False).max().sort_values(ascending=False)[1]



# Plots for tab "ÁREAS DE DESARROLLO POR Estados_de_USA."-------------------------------- 
df_sound_gb = df_sound.groupby("Estados_de_USA").sum()
# Sorting areas from most usual to less.
df_sound_gb_T = df_sound_gb.T
df_sound_gb_T['countries_by_sound'] = df_sound_gb_T[df_sound['Estados_de_USA'].unique()].sum(axis=1)
list_sound = []
list_sound.extend(df_sound_gb_T.sort_values(by='countries_by_sound',ascending=False).index[:])
max_y_val_sound=df_sound_gb_T.sort_values(by='countries_by_sound',ascending=False).max().sort_values(ascending=False)[1]









# app = JupyterDash(__name__)
app = dash.Dash(__name__, suppress_callback_exceptions=True)


title = {
    'color': '#696969',
    'font': 'morebi'
}
text = {
    'color': '#999999',
    'font': 'MOREBI'
}
body_color = {
    'background': '#ffffff',
}

tab_style = {
    'color': title ['color'],
    'border-radius': '5px',
    'background-color': '#F9F9F9',
    'padding': '15px',
    'position': 'relative',
}

tab_selected_style = {
    'color': title ['color'],
    'fontWeight': 'bold',
    'border-radius': '5px',
    'background-color': 'transparent',
    'padding': '15px',
    'position': 'relative',
}


app.layout = html.Div(style={'backgroundColor': '#F9F9F9'},children=[



    html.Div(id="image" ),
    dcc.Interval(id='interval', interval=5000, n_intervals=0, max_intervals=1),

    html.Div([
        html.Div(children=[dcc.Markdown('&nbsp' )],style={'font-size': '.3rem'}),

        html.Div(
            [
            html.Img(src="https://lh3.googleusercontent.com/8fYOMwmNy96LCbxvQK0cKDbHXEXr81F1z_9GUBOqOUfOJLmnHe5SRu7POY77PV195fuutoCVwoT1qkT_Dq51CsMXDwMcyfTv11SJx3STyNSACIibWKv5GTgxjDRE3YPT71-7iZ1tJdThT880t2C3a27EBrPpYlNstX0S0u07KrJhoYZI7PJmtWCNAeaX5As3BMv6p_w0CAUlsblmTRIspTWbK8C2yJU4F5gZP_Do9EGu_VE9VCrPIoZ_2zEQvHxennVF7Nx0_y3ObXXv3C8vwiy5OEU-DNGHeRsQm-ZJT0lTC0HnYZwfK74D-eFG9YAbSuraXnAtK2DO7plMgh0Ws4XArBAQvdAwYEacPwSHCrcf_3x474J9zLN61vMKaMJJ-WLx9w6E6rU6oKGdUWV01V1NOnoYZD_XZIoDTmnS-5yweQvAF0NgNhi3Gz9QpzL70L0eHENEvJjfSuVE3sxX--wB2WTExF2ipc0wdI2i-RP0TlogbO4r93MEsRDm4j5WQdcYy_ox5ixSH58Mmz0H5LfK_COypXe7n14-yrRa3tMmCcODj9ENn8j6E6dg9suCCgJC2g434Ik30GEGh3ulZ-p_Gk0KKuZVhROdA3h3b8IeQ8B1WuI6vXvhtLsvAqakYMBzIsi89E2Mym3X3e90zuKPwKKxUHyxJxX0nJKr2MHNpiBB4olRZ1IJJJpMXk3ZWhYJ0yGji-baVz4NHBr6FEPiZw=w941-h659-no?authuser=0",
                     style={'width': 'auto', 'height': '80px', 'float': 'left'}
                     ),
            html.A(
                [html.Button(
                    "Learn More",
                    id="learnMore",
                    style={'width': '16.25%', 'transform': 'translate(0%, 50%)', 'float': 'right', 'height': '38px', 'padding': '0 30px', 'color': '#555', 'text-align': 'center', 'font-size': '11px', 'font-weight': '600', 'line-height': '38px', 'letter-spacing': '.1rem', 'text-transform': 'uppercase', 'text-decoration': 'none', 'white-space': 'nowrap', 'background-color': 'transparent', 'border-radius': '4px', 'border': '1px solid #bbb', 'cursor': 'pointer', 'box-sizing': 'border-box' }
                )],
                href="https://github.com/echestare/Audiometry_challenge_Data_Analyst"
                
            ),
            html.H1(
                children='DASHING STATS', 
                style={'textAlign': 'center', 'color': title ['color'], 'font_family': 'Montserrat-Regular', 'width': '83.5%'} 
                ),
            
            
            ],
            style={
                  'border-radius': '5px',
                  'background-color': '#F9F9F9',
                  'margin': '10px',
                  'padding': '15px',
                  'position': 'relative',
                  'box-shadow': '2px 2px 2px lightgrey'
            }
        ),
        # cards,
        dcc.Tabs(id="tabs_analysis", value='overview', children=[
            dcc.Tab(label='VISTA GENERAL.', value='overview', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='ÁREAS DE DESARROLLO POR Estados_de_USA.', value='areas_by_country', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='ESTÍMULOS EN ACÚFENOS POR Estados_de_USA.', value='sound_by_country', style=tab_style, selected_style=tab_selected_style),
            ]),
        html.Div(id='tabs_content_analysis'),
        

        html.Div(children=[dcc.Markdown( 
        " © 2022 [EcheStare](https://github.com/echestare)  All Rights Reserved.")], style={
                    'textAlign': 'right',
                    'color':'00B0FF',
                    "background": "#c7fff5"}
                )]
                , style={
                    # 'background-image': 'url()',
                    # 'background-image': 'url(/nbextensions/background.jpg)',
                    'height': '100%',
                    'width': '100%',
                    'margin': '0',
                    'background-repeat': 'no-repeat',
                    'background-size': 'cover'
                    }
    )

])


            
            
            


@app.callback(Output('image', 'children'),
              [Input('interval', 'n_intervals')])
def display_image(n):
    if n == 0:
        img = html.Div([
            html.Div(children=[dcc.Markdown('&nbsp' )],style={'font-size': '20rem', 'background-color': '#ffffff'}),
            html.Img(src="https://lh3.googleusercontent.com/8fYOMwmNy96LCbxvQK0cKDbHXEXr81F1z_9GUBOqOUfOJLmnHe5SRu7POY77PV195fuutoCVwoT1qkT_Dq51CsMXDwMcyfTv11SJx3STyNSACIibWKv5GTgxjDRE3YPT71-7iZ1tJdThT880t2C3a27EBrPpYlNstX0S0u07KrJhoYZI7PJmtWCNAeaX5As3BMv6p_w0CAUlsblmTRIspTWbK8C2yJU4F5gZP_Do9EGu_VE9VCrPIoZ_2zEQvHxennVF7Nx0_y3ObXXv3C8vwiy5OEU-DNGHeRsQm-ZJT0lTC0HnYZwfK74D-eFG9YAbSuraXnAtK2DO7plMgh0Ws4XArBAQvdAwYEacPwSHCrcf_3x474J9zLN61vMKaMJJ-WLx9w6E6rU6oKGdUWV01V1NOnoYZD_XZIoDTmnS-5yweQvAF0NgNhi3Gz9QpzL70L0eHENEvJjfSuVE3sxX--wB2WTExF2ipc0wdI2i-RP0TlogbO4r93MEsRDm4j5WQdcYy_ox5ixSH58Mmz0H5LfK_COypXe7n14-yrRa3tMmCcODj9ENn8j6E6dg9suCCgJC2g434Ik30GEGh3ulZ-p_Gk0KKuZVhROdA3h3b8IeQ8B1WuI6vXvhtLsvAqakYMBzIsi89E2Mym3X3e90zuKPwKKxUHyxJxX0nJKr2MHNpiBB4olRZ1IJJJpMXk3ZWhYJ0yGji-baVz4NHBr6FEPiZw=w941-h659-no?authuser=0"
                     , style={'background-color': '#ffffff', 'z-index': '1000', 'position': 'absolute' , 'left': '50%', 'top': '50%', 'transform': 'translate(-45%, -45%)', 'width': '40%', 'height': 'auto'}
                     ),
            html.Div(children=[dcc.Markdown('&nbsp' )],style={'font-size': '20rem', 'background-color': '#ffffff'})
            ])
    else:
         img = ""
    return img


countries = df['Estados_de_USA'].value_counts().index
dict_country = dict(zip(countries, countries))
@app.callback(Output('tabs_content_analysis', 'children'),
              Input('tabs_analysis', 'value'))

def render_content(tab):

    if tab == 'overview':
        return html.Div([
            html.H2('DISTRIBUCIÓN DE PROFESIONALES EN CADA CATEGORÍA',style={'textAlign': 'center', 'color': title ['color'], 'font_family': 'Montserrat-Regular'}),
            dcc.Graph(
                # id='graph-1-tabs',
                style={'transform': 'translate(0%, 0%)', 'width': 'auto', 'height': 'auto','textAlign': 'center', 'color': title ['color'], 'backgroundColor': '#F9F9F9'},
                figure=fig_overview
            )
        ],
        style={
              'border-radius': '5px',
              'background-color': '#F9F9F9',
              'margin': '10px',
              'padding': '15px',
              'position': 'relative',
              'box-shadow': '2px 2px 2px lightgrey'
        })
    elif tab == 'areas_by_country':
        return html.Div([
            html.Div([
                html.H2('Profesionales en cada Estados_de_USA.',style={'textAlign': 'center', 'color': title ['color'], 'font_family': 'Montserrat-Regular'}),
                html.Div([
                    dcc.Dropdown(
                        id='bar_selector',
                        options=dict_country,
                        value=countries[0],
                        # multi=True,
                        placeholder="Seleccione algún Estados_de_USA en el menú desplegable",
                    )
                ], style={ 'margin-left': '33%','margin-right': '33%' }),
                html.Div(id="output_plots")
                # dcc.Graph(id="output_plots")
            ],
            style={
                  'border-radius': '5px',
                  'background-color': '#F9F9F9',
                  'margin': '10px',
                  'padding': '15px',
                  'position': 'relative',
                  'box-shadow': '2px 2px 2px lightgrey'
            }),
            html.Br(),
            html.Div([
            html.H2('Profesionales respecto a cada área de desarrollo.',style={'textAlign': 'center', 'color': title ['color'], 'font_family': 'Montserrat-Regular'}),
            html.Div([
                dcc.Dropdown(
                    id='bar_selector2',
                    options=[
                        {'label': 'Audiología en adultos', 'value': 'Audiología en adultos'},
                        {'label': 'Audiología en niños', 'value': 'Audiología en niños'},
                        {'label': 'Adaptación de prótesis auditivas', 'value': 'Adaptación de prótesis auditivas'},
                        {'label': 'Tratamiento del lenguaje en niños', 'value': 'Tratamiento del lenguaje en niños'},
                        {'label': 'Medicina Laboral', 'value': 'Medicina Laboral'},
                        {'label': 'Tratamiento del lenguaje en adultos', 'value': 'Tratamiento del lenguaje en adultos'},
                        {'label': 'Docencia', 'value': 'Docencia'}
                    ],
                    value='Audiología en adultos',
                    # multi=True,
                    placeholder="Seleccione algún Área de desarrollo en el menú desplegable",
                )
            ], style={ 'margin-left': '33%','margin-right': '33%' }),
            # dcc.Graph(id="output_plots2")
            html.Div(id="output_plots2")
            ],
            style={
                  'border-radius': '5px',
                  'background-color': '#F9F9F9',
                  'margin': '10px',
                  'padding': '15px',
                  'position': 'relative',
                  'box-shadow': '2px 2px 2px lightgrey'
            })
        ])
    
    
    elif tab == 'sound_by_country':
        return html.Div([
            html.Div([
                html.H2('Profesionales en cada Estados_de_USA.',style={'textAlign': 'center', 'color': title ['color'], 'font_family': 'Montserrat-Regular'}),
                html.Div([ 
                    dcc.Dropdown(
                        id='bar_selector3',
                        options=dict_country,
                        value=countries[0],
                        # multi=True,
                        placeholder="Seleccione algún Estados_de_USA en el menú desplegable",
                    ),
                ], style={ 'margin-left': '33%','margin-right': '33%' }),
                # dcc.Graph(id="output_plots3")
                html.Div(id="output_plots3")
            ],
            style={
                  'border-radius': '5px',
                  'background-color': '#F9F9F9',
                  'margin': '10px',
                  'padding': '15px',
                  'position': 'relative',
                  'box-shadow': '2px 2px 2px lightgrey'
            }),
            html.Br(),
            html.Div([
                html.H2('Profesionales respecto a los Estímulos para acúfenos usados.',style={'textAlign': 'center', 'color': title ['color'], 'font_family': 'Montserrat-Regular'}),
                html.Div([ 
                    dcc.Dropdown(
                        id='bar_selector4',
                        options=[
                            {'label': 'Tono Puro', 'value': 'Tono Puro'},
                            {'label': 'Ruido de Banda Estrecha', 'value': 'Ruido de Banda Estrecha'},
                            {'label': 'Ruido Blanco', 'value': 'Ruido Blanco'},
                            {'label': 'Ruido Rosa', 'value': 'Ruido Rosa'},
                            {'label': 'Ruido de Banda Ancha', 'value': 'Ruido de Banda Ancha'},
                            {'label': 'Tono Modulado (warble tone)', 'value': 'Tono Modulado (warble tone)'},
                            {'label': 'Ruido Vocal', 'value': 'Ruido Vocal'}
                        ],
                        value='Tono Puro',
                        # multi=True,
                        placeholder="Seleccione algún Estímulo para Acúfeno en el menú desplegable",
                    ),
                ], style={ 'margin-left': '33%','margin-right': '33%' }),
                # dcc.Graph(id="output_plots4")
                html.Div(id="output_plots4")
            ],
            style={
                  'border-radius': '5px',
                  'background-color': '#F9F9F9',
                  'margin': '10px',
                  'padding': '15px',
                  'position': 'relative',
                  'box-shadow': '2px 2px 2px lightgrey'
            })
        ])
    




@app.callback(Output("output_plots", "children"),
              Input("bar_selector", "value"))
def update_bar_selector(value):

    # Countries ordered by which is the one with more professionals surveyed to one with the less
    # for item in df_sector['Estados_de_USA'].value_counts().index:

    item = value
    # removing empty columns for each country.
    list_tmp=[]
    for i,item2 in enumerate(df_sector[df_sector['Estados_de_USA']==item][list_sector].sum()):
        if item2>0:
            list_tmp.append(df_sector[df_sector['Estados_de_USA']==item][list_sector].sum().index[i])

    # list to use explode in pieplot
    list_pie_portion=[0.08]+[0]*(len(list_tmp)-1)

    # df to plot
    cat_num = df_sector[df_sector['Estados_de_USA']==item][list_tmp].sum().sort_values(ascending=False)
    # stats by country
    tot_am = int(df_sector[df_sector['Estados_de_USA']==item][list_sector].sum().values.sum())
    docs1 = int(df_sector[df_sector['Estados_de_USA']==item]['Estados_de_USA'].value_counts())

    # Titles
    # title = """<html><h1 align="center" style="font-family:Cambria"><u>{item}</u></h1></html>""".format(item=item.upper())
    # display(HTML(title))   
    # print("Cantidad total de Doctores entrevistados: \x1b[1;4;35m %d \x1b[0m \nÁreas de desarrollo pertinentes = %d \nCantidad total de Áreas de Desarrollo atendidas: \x1b[1;4;35m %d " % (docs, len(cat_num),tot_am))
    ####
    # Determining a subplot grid.
    fig_areas_by_country = make_subplots(rows=5, cols=3,specs=[ [{},  {'type':'domain','colspan': 2, 'rowspan': 5}, None],[{'rowspan': 3}, {}, {}],[{}, {}, {}],[{}, {}, {}],[{}, {}, {}] ])#, subplot_titles=("Áreas de desarrollo por Estados_de_USA", "Profesionales por Estados_de_USA"))
    # Plotting
    fig1 = px.bar(cat_num, x=cat_num.index, y=cat_num.values, text=cat_num.values)
    fig2 = px.pie(cat_num, values=cat_num.values, names=cat_num.index)
    # Colors
    fig1.update_traces(marker_color=colors,textposition='outside')
    fig2.update_traces(textposition='inside', textinfo='percent', pull=[0.1, 0.06, 0.02, 0.02, 0.02, 0.02, 0.02], marker=dict(colors=colors), rotation=0)

    # Placing plots in the subplot grid
    for trace in fig1.data:
        fig_areas_by_country.add_trace(trace, 2, 1)
    for trace in fig2.data:
        fig_areas_by_country.add_trace(trace, 1, 2)
    # Labelling axis
    fig_areas_by_country['layout']['yaxis2']['title']='Frecuencias Absolutas'
    fig_areas_by_country.update_layout()
    # Setting yaxe
    fig_areas_by_country.update_yaxes(range=[0, (df_sector.groupby("Estados_de_USA").sum().max().sort_values(ascending=False)[0]+3)])
    fig_areas_by_country.update_layout(paper_bgcolor='#F9F9F9')
    
    len_cat_num = len(cat_num)
    
    # return fig_areas_by_country
    return html.Div([
        html.P(children=["Cantidad total de Doctores entrevistados:  ", docs1]),
        html.P(children=["Áreas de desarrollo pertinentes: ", len_cat_num]),
        html.P(children=["Cantidad total de Áreas de Desarrollo atendidas: ", tot_am]),
        dcc.Graph(figure=fig_areas_by_country)
        ])

@app.callback(Output("output_plots2", "children"),
              Input("bar_selector2", "value"))
def update_bar_selector(value):
    
    item = value
    
    # df
    to_plot = df_sector_gb[item].sort_values(ascending=False)
    list_tmp=[]
    for i,item2 in enumerate(to_plot):
        if item2>0:
            list_tmp.append(to_plot.index[i])
    # list to use explode in pieplot
    list_pie_portion=[0.08]+[0]*(len(list_tmp)-1)
    # stats by country
    docs2 = df_sector_gb_T.at[item,'countries_by_areas']



    # Determining a subplot grid.
    fig_country_by_area = make_subplots(rows=5, cols=3,specs=[ [{},  {'type':'domain','colspan': 2, 'rowspan': 5}, None],[{'rowspan': 3}, {}, {}],[{}, {}, {}],[{}, {}, {}],[{}, {}, {}] ])#, subplot_titles=("Áreas de desarrollo por Estados_de_USA", "Profesionales por Estados_de_USA"))
    # Plotting
    fig1 = px.bar(to_plot, x=to_plot[list_tmp].index, y=to_plot[list_tmp].values, text=to_plot[list_tmp].values)
    fig2 = px.pie(to_plot, values=to_plot[list_tmp].values, names=to_plot[list_tmp].index)#, hole=.3)
    # Colors
    # colors = _BRAND__colors_l if len(df_areas_by_country.index)>len(_BRAND__colors_f2) else _BRAND__colors_l[10:-4] #_BRAND__colors_f2[3:]
    # colors = [_BRAND__colors_l[i] for i,item in enumerate(_BRAND__colors_l) if i%2 == 0][3:]
    fig1.update_traces(marker_color=colors,textposition='outside')
    fig2.update_traces(textposition='inside', textinfo='percent', pull=[0.1, 0.06, 0.02, 0.02, 0.02, 0.02, 0.02], marker=dict(colors=colors), rotation=0)

    # Placing plots in the subplot grid
    for trace in fig1.data:
        fig_country_by_area.add_trace(trace, 2, 1)
    for trace in fig2.data:
        fig_country_by_area.add_trace(trace, 1, 2)
    # Labeling axis
    fig_country_by_area['layout']['yaxis2']['title']='Frecuencias Absolutas'
    fig_country_by_area.update_layout()
    # Setting yaxe
    fig_country_by_area.update_yaxes(range=[0, max_y_val_sector+5])
    fig_country_by_area.update_layout(paper_bgcolor='#F9F9F9')
    
    len_list_tmp = len(list_tmp)

    # return fig_country_by_area
    return html.Div([
        html.P(children=["Cantidad de PAÍCES donde lo hacen: ", len_list_tmp]),
        html.P(children=["Cantidad de DOCTORES que lo hacen: ", docs2]),
        dcc.Graph(figure=fig_country_by_area)
        ])


@app.callback(Output("output_plots3", "children"),
              Input("bar_selector3", "value"))
def update_bar_selector(value):

    # Countries ordered by which is the one with more professionals surveyed to one with the less
    # for item in df_sector['Estados_de_USA'].value_counts().index:

    item = value
    # removing empty columns for each country.
    list_tmp=[]
    for i,item2 in enumerate(df_sound[df_sound['Estados_de_USA']==item][list_sound].sum()):
        if item2>0:
            list_tmp.append(df_sound[df_sound['Estados_de_USA']==item][list_sound].sum().index[i])

    # list to use explode in pieplot
    list_pie_portion=[0.08]+[0]*(len(list_tmp)-1)
    
    # df to plot
    cat_num = df_sound[df_sound['Estados_de_USA']==item][list_tmp].sum().sort_values(ascending=False)
    # stats by country
    tot_am = int(df_sound[df_sound['Estados_de_USA']==item][list_sound].sum().values.sum())
    docs3 = int(df_sound[df_sound['Estados_de_USA']==item]['Estados_de_USA'].value_counts())
    ####
    # Determining a subplot grid.
    fig_sound_by_country = make_subplots(rows=5, cols=3,specs=[ [{},  {'type':'domain','colspan': 2, 'rowspan': 5}, None],[{'rowspan': 3}, {}, {}],[{}, {}, {}],[{}, {}, {}],[{}, {}, {}] ])#, subplot_titles=("Áreas de desarrollo por Estados_de_USA", "Profesionales por Estados_de_USA"))
    # Plotting
    fig1 = px.bar(cat_num, x=cat_num.index, y=cat_num.values, text=cat_num.values)
    fig2 = px.pie(cat_num, values=cat_num.values, names=cat_num.index)
    # Colors
    fig1.update_traces(marker_color=colors,textposition='outside')
    fig2.update_traces(textposition='inside', textinfo='percent', pull=[0.1, 0.06, 0.02, 0.02, 0.02, 0.02, 0.02], marker=dict(colors=colors), rotation=0)

    # Placing plots in the subplot grid
    for trace in fig1.data:
        fig_sound_by_country.add_trace(trace, 2, 1)
    for trace in fig2.data:
        fig_sound_by_country.add_trace(trace, 1, 2)
    # Labelling axis
    fig_sound_by_country['layout']['yaxis2']['title']='Frecuencias Absolutas'
    fig_sound_by_country.update_layout()
    # Setting yaxe
    fig_sound_by_country.update_yaxes(range=[0, (df_sound.groupby("Estados_de_USA").sum().max().sort_values(ascending=False)[0]+3)])
    fig_sound_by_country.update_layout(paper_bgcolor='#F9F9F9')
    
    len_cat_num = len(cat_num)
    
    # return fig_sound_by_country
    return html.Div([
        html.P(children=["Cantidad total de Doctores entrevistados:  ", docs3]),
        html.P(children=["Estímulos para comparar Acúfenos pertinentes: ", len_cat_num]),
        html.P(children=["Cantidad total de Estímulos para comparar Acúfenos usados: ", tot_am]),
        dcc.Graph(figure=fig_sound_by_country)
        ])    



@app.callback(Output("output_plots4", "children"),
              Input("bar_selector4", "value"))
def update_bar_selector(value):
    
    item = value
    # df
    to_plot = df_sound_gb[item].sort_values(ascending=False)
    list_tmp=[]
    for i,item2 in enumerate(to_plot):
        if item2>0:
            list_tmp.append(to_plot.index[i])
    # list to use explode in pieplot
    list_pie_portion=[0.08]+[0]*(len(list_tmp)-1)
    # stats by country
    docs4 = int(df_sound_gb_T.at[item,'countries_by_sound'])


    # Determining a subplot grid.
    fig_country_by_sound = make_subplots(rows=5, cols=3,specs=[ [{},  {'type':'domain','colspan': 2, 'rowspan': 5}, None],[{'rowspan': 3}, {}, {}],[{}, {}, {}],[{}, {}, {}],[{}, {}, {}] ])
    # Plotting
    fig1 = px.bar(to_plot, x=to_plot[list_tmp].index, y=to_plot[list_tmp].values, text=to_plot[list_tmp].values)
    fig2 = px.pie(to_plot, values=to_plot[list_tmp].values, names=to_plot[list_tmp].index)
    # Colors
    fig1.update_traces(marker_color=colors,textposition='outside')
    fig2.update_traces(textposition='inside', textinfo='percent', pull=[0.1, 0.06, 0.02, 0.02, 0.02, 0.02, 0.02], marker=dict(colors=colors), rotation=0)

    # Placing plots in the subplot grid
    for trace in fig1.data:
        fig_country_by_sound.add_trace(trace, 2, 1)
    for trace in fig2.data:
        fig_country_by_sound.add_trace(trace, 1, 2)
    # Labeling axis
    fig_country_by_sound['layout']['yaxis2']['title']='Frecuencias Absolutas'
    fig_country_by_sound.update_layout()
    # Setting yaxe
    fig_country_by_sound.update_yaxes(range=[0, max_y_val_sound+5])
    fig_country_by_sound.update_layout(paper_bgcolor='#F9F9F9')

    len_list_tmp = len(list_tmp)

    return html.Div([
        html.P(children=["Cantidad de PAÍCES donde lo hacen: ", len_list_tmp]),
        html.P(children=["Cantidad de DOCTORES que lo hacen: ", docs4]),
        dcc.Graph(figure=fig_country_by_sound)
        ])



if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True, threaded=True)








