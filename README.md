<a href="https://www.linkedin.com/in/ezequiel-nicolás-starecinch" target="_blank"><img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>

<h1 align="center"> DESAFÍO DATA ANALYST and Data Science</h1>
<h3 align="center"> Data cleaning, EDAs, Data Science, SQL querys y Plotly DASH.</h3>

<p align="center"><img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/brand.jpg" alt="drawing" width="800"/></p>

<!-- TABLE OF CONTENTS -->
## Índice
<details open="open">
  <summary>Tabla de contenidos: </summary>
  <ol>
    <li>
      <a href="#about-the-project">Sobre el proyecto.</a>
      <ul>
        <li><a href="#project-overview">Resumen del proyecto.</a></li>
        <li><a href="#built-with">Desarrollado con.</a></li>
      </ul>
    </li>
    <li>
      <a href="#installation">Instalación.</a></li>
    </li>
    <li>
      <a href="#stages-overview">Partes del proyecto.</a>
      <ul>
        <li><a href="#2-1">2_1_Manipulando_bases_de_datos</a></li>
        <li><a href="#2-2">2_2_Manejo_de_bases_de_datos_con_SQL</a></li>
        <li><a href="#2-3">2_3_Análisis_Exploratorio_de_los_Datos___EDA</a></li>
        <li><a href="#2-4">2_4_eda_dash</a></li>
        <li><a href="#2-5">2_5_Consulta_y_análisis_usando_APIs</a></li>
      </ul>
    </li>
    <li>
      <a href="#productionization">Productividad.</a>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## Sobre el proyecto:
<!-- PROJECT OVERVIEW -->
### Resumen del proyecto:
Este proyecto nace de la conjunción de algunas pruebas para entrevistas de trabajo encontradas en internet. He conservado algunos enunciados y exigencias, agregado algunos y  modificando los datos originales y cualquier referencia a las empresas.

En cada parte fue necesario hacer una limpieza de datos (más o menos significativo según el caso) y, al menos, un EDA.
Se compone de 5 partes:
- 2_1_Manipulando_bases_de_datos: `DATA SCIENCE`.
- 2_2_Manejo_de_bases_de_datos_con_SQL: `SQL QUERIES`.
- 2_3_Análisis_Exploratorio_de_los_Datos___EDA: `DATA ANLYSIS`.
- 2_4_eda_dash: `INTERACTIVE DASHBOARD`
- 2_5_Consulta_y_análisis_usando_APIs: `DATA ANLYSIS` (criterio).







<!-- BUILT WITH -->
### Desarrollado con:
* **Versión de Python**: 3.8.8
* **Framework**: Colaboratory de Google, Spyder IDE, Opera.
* **Packages**:
    - 2_1_Manipulando_bases_de_datos: pandas, numpy, seaborn, matplotlib, plotly, IPython y `sklearn`.
    - 2_2_Manejo_de_bases_de_datos_con_SQL: pandas y `sqlite3`.
    - 2_3_Análisis_Exploratorio_de_los_Datos___EDA: pandas, numpy, IPython, seaborn y `plotly`.
    - 2_4_eda_dash: pandas, numpy, IPython, `Plotly`, `Dash` y `JupyterDash`.
    - 2_5_Consulta_y_análisis_usando_APIs: pandas, matplotlib, `Plotly` y `requests`.



<!-- INSTALLATION -->
## Instalación 
Clonando el repo
   ```sh
   git clone https://github.com/echestare/Audiometry_challenge_Data_Analyst.git
   ```
En google  colab:
- Primero ir a la dirección del notebook que quiere ejecutar. Por ejemplo:
```sh
   https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/2_1_Manipulando_bases_de_datos.ipynb
   ```
   Y se reemplaza, en la dirección, `github.com` por `githubtocolab.com`. Como a continuación:
```sh
   https://githubtocolab.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/2_1_Manipulando_bases_de_datos.ipynb
   ```
- Luego ejecutar en la primera celda (para que se agreguen los archivos extras):

>Este paso no es necesario, ya que todos los archivos del repo usan los datasets e imágenes subidos Google Drive (por lo que no necesita tenerlos localmente).

   ```sh
   !git clone https://github.com/echestare/Audiometry_challenge_Data_Analyst
   ```

<!-- stages overview -->
## Partes del Proyecto:
A continuación se presentan los links hacia los códigos funcionando en Colaboratory de Google:

<!-- 2 1 -->
### [2_1_Manipulando_bases_de_datos.ipynb](https://colab.research.google.com/drive/1Ddi5edhWpAqIJ2Cd5CAN_ooC2VXb0QLU?usp=sharing)

- Dataset: llamadas al 911 en USA entre el 2015 y 2016 (más de 600K líneas). 

    - Este archivo no se pudo subir en github por el límite de tamaño (pesa 117 MB), pero acá dejo el [link de Kaggle](https://www.kaggle.com/mchirico/montcoalert).

    - De todos modos, el código usa el dataset almacenado en Drive. Si se abre con colab, la carga de los datos es muy rápida.

- EDA simple.

- Comparación de **modelos de algoritmos para predecir** la relación el `Código Postal` a partir de la `latitud y longitud`: Correlación de Pearson, Regresión Lineal, k-means, Hierarchical clustering, `Árbol de regresión (99%)`.

<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_1_data.jpg" alt="drawing" widtht ="800"/>

||||
|----------------|-------------------------------|-----------------------------|
|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_1_regression_tree.jpg" alt="drawing" width="350"/>|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_1_kmean.jpg" alt="drawing" width="350"/>|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_1_Hierarchical_clustering.jpg" alt="drawing" width="350"/>|
||||

    
<!-- 2 2 -->
### [2_2_Manejo_de_bases_de_datos_con_SQL.ipynb](https://colab.research.google.com/drive/1mA8LLd-Mkw7vmdCMQHAHdXCeI7itMC6Q?usp=sharing)

- Dataset: encuesta a doctores sobre uso de audiómetro \_BRAND\_, datos personales y experiencia profesional.

- **SQL Queries**
<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_2_data.jpg" alt="drawing" width="800"/>

|||
|-------------------------------|-----------------------------|
|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_2_data_contacto.jpg" alt="drawing" width="400"/>|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_2_data_acuf.jpg" alt="drawing" width="400"/>|
|||

<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_2_query.jpg" alt="drawing" width="800"/>

<!-- 2 3 -->
### [2_3_Análisis_Exploratorio_de_los_Datos___EDA.ipynb](https://colab.research.google.com/drive/1vVpQnQCKTf9rGFMGKVL2OCRXrmlauS2r?usp=sharing)

- Dataset: encuesta a doctores sobre experiencia profesional haciendo acufenometrías (audiometría tinitumetría), experiencia, áreas de especialización, estímulos usados, datos personales y más (el dataset original tenía más datos, pero no eran pertinentes al trabajo y fueron eliminados).

- **Análisis de Datos** de situaciones de interés específicas.

<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_3_data.jpg" alt="drawing" width="800"/>

<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_3_data_area.jpg" alt="drawing" width="800"/>

|||
|-------------------------------|-----------------------------|
|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_3_area_country.jpg" alt="drawing" width="400"/>|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_3_country_area.jpg" alt="drawing" width="400"/>|
|||

<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_3_data_sound.jpg" alt="drawing" width="800"/>

|||
|-------------------------------|-----------------------------|
|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_3_sound_country.jpg" alt="drawing" width="400"/>|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_3_country_sound.jpg" alt="drawing" width="400"/>|
|||

<!-- 2 4 -->
### [2_4_eda_dash](https://colab.research.google.com/drive/1pnU1HQUgxqFsDqoKf6ZI8Q9R-P2j9D-T?usp=sharing)
>Este link tiene modificaciones respecto del código en el repositorio para poder funcionar correctamente en un Notebook de `Colaboratory de Google`. La modificación más importante es que usa una librería vieja de Dash y de Jupyter-Dash (precisamente para poder funcionar en colab).

>Así mismo, el link lleva a un archivo ".ipynb", mientras que en el repo se trata de un archivo ".py".

- **Dashboard** funcional del análisis del punto anterior.
    
||||
|----------------|-------------------------------|-----------------------------|
|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_4_overview.png" alt="drawing" width="350"/>|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_4_area.png" alt="drawing" width="350"/>|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_4_sound.png" alt="drawing" width="350"/>|
||||
    
<!-- 2 5 -->
### [2_5_Consulta_y_análisis_usando_APIs.ipynb](https://colab.research.google.com/drive/12tZH4r0_urV8jo8gFXuhoYkUhZ1GnOa1?usp=sharing)

- Dataset: datos obtenidos de la app del audiómetro \_BRAND\_. Este dataset consta de dos tablas relacionadas por la columna "id".

- **Análisis de Datos** de situaciones de interés específicas.

<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_5_data1.jpg" alt="drawing" width="800"/>

<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_5_data2.jpg" alt="drawing" width="800"/>

|||
|-------------------------------|-----------------------------|
|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_5_freqs.jpg" alt="drawing" width="400"/>|<img src="https://github.com/echestare/Audiometry_challenge_Data_Analyst/blob/main/Snapshots/2_5_intencities.jpg" alt="drawing" width="400"/>|
|||



<!-- productionization -->
## Productividad:

- 2_1_Manipulando_bases_de_datos: Tal vez, sea interesante probar un método de Vectorización clasificatorio, sin embargo, es indiscutible que el resultado del Árbol de Regresión es muy bueno.
- 2_2_Manejo_de_bases_de_datos_con_SQL: La librería SQLite3 es excelente para hacer SQL Querys usando python; los resultados son más que satisfactorios.
- 2_3_Análisis_Exploratorio_de_los_Datos___EDA: Este análisis muestra claramente cómo en ciertos países es más fuerte la presencia de Audiometristas mientras que en otros pueden ser irrisoria su presencia. Así como ciertas áreas de especialización dentro de la rama de la medicina tienen más alcance. Finalmente, la distribución de la utilización de los distintos estímulos para detectar acúfenos es relativamente similar para cada estado.
- 2_4_eda_dash: El Dashboard es minimalista y aún así tiene toda la información significativa distribuida de forma tal que con la interactividad ofrecida se puede explorar convenientemente.
- 2_5_Consulta_y_análisis_usando_APIs: La librería `requests` es simple y potente para la exploración de APIs. Durante la limpieza de datos se encontró que el dataset tiene una notable baja calidad. El análisis se terminó haciendo sobre menos datos de lo conveniente, pero pueden dar resultados útiles para tomar decisiones respecto al método para verificar la calidad del estudio.
