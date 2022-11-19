#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 09:54:45 2022

@author: usuario
"""
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


# df = pd.read_csv(r'/home/usuario/Documentos/victor/github/inv_emissoes/merged_criciuma_morro_kelvin.csv', sep=';')

df_neg = pd.read_csv(
    r'/home/usuario/Documentos/victor/github/inv_emissoes/merged_criciuma_morro_kelvin_neg.csv'
    , sep=','
    )

#removendo colunas extras utlizando drop e indexação do iloc, 
df_colunms=df_neg.drop(
    df_neg.iloc[:,34:]
    ,axis=1) #eixo 0 são as linhas, eixo 1 são as colunas


#
df_geo= gpd.GeoDataFrame(
    df_colunms,geometry=gpd.points_from_xy(df_colunms['Long'],df_colunms['Lat']))

#abrir shapefile utilizando geopandas, baixar shape de alguma fonte

shape_03=gpd.read_file(
    r'/home/usuario/Documentos/victor/github/inv_emissoes/bc25_sc_shapefile_2020-10-01/lml_unidade_federacao_a.shp')
#plotando o shape file de SC
shape_03.plot() #figura do shape

#plotando pontos no shape, executar as linhas abaixo td junto
ax=plt.gca() #criando eixo x utilizando o gca do matplotlib
shape_03.boundary.plot(ax=ax) #apenas perímetro de sc utilizando boundary
df_geo.plot(ax=ax) #




