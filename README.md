
<h1 align="center">
Proyecto Individual N°2
</h1>


En los últimos años, el mercado bursátil ha experimentado altibajos debido a una serie de factores que incluyen la volatilidad del mercado global, la incertidumbre política y las tendencias económicas. A partir de 1990, el mercado bursátil ha pasado por varios períodos de crecimiento y recesión.

El mercado bursátil ha experimentado una serie de altibajos en las últimas dos décadas, con varios eventos importantes que han afectado significativamente a los inversores. En el año 2000, el estallido de la burbuja de las empresas de tecnología causó una fuerte caída en los mercados, lo que se conoció como el "crash de las puntocom".

Posteriormente, en 2008, la crisis financiera global tuvo un impacto aún mayor en los mercados de valores, con una caída significativa en los precios de las acciones que afectó a muchos inversores y empresas. Sin embargo, a partir de 2009, el mercado comenzó a recuperarse y ha experimentado un período de crecimiento constante en los últimos años.

En términos de impactos positivos, el mercado bursátil ha ofrecido rendimientos atractivos a los inversores que han invertido en empresas exitosas, lo que les ha permitido obtener beneficios significativos. Además, las empresas han utilizado la bolsa de valores para obtener financiamiento y expandir sus negocios.

En cuanto a las recomendaciones de inversión, se puede considerar invertir en empresas que pertenecen a industrias con perspectivas de crecimiento, como la tecnología, la salud y las energías renovables. Además, es importante tener en cuenta el desempeño histórico de las empresas y sus planes de expansión futuros.

Como experto en datos, también se pueden proporcionar otros datos complementarios, como los indicadores clave del mercado de valores, como el índice S&P 500, el índice Nasdaq, y otros. Además, se pueden proporcionar análisis más detallados de las tendencias y patrones del mercado, y ofrecer perspectivas de inversión específicas en función de las preferencias de la empresa que busca invertir.

<h1>Contexto</h1>
Este estudio se centró en analizar el comportamiento del mercado bursátil en Estados Unidos a través del índice bursátil S&P500. Este índice es una lista de las 500 empresas más grandes del país, compilada por la empresa Standard & Poor's. La selección de estas empresas se basa en su capitalización bursátil, es decir, su valor total en el mercado de valores. Este índice excluye a las empresas más pequeñas y medianas y solo incluye a las más grandes y relevantes en términos económicos. Por lo tanto, este estudio proporciona una visión general del rendimiento de las empresas más importantes en el mercado bursátil estadounidense..<br></br>

Las empresas del "S&P500" se dividen en 10 sectores de la economía:<br>

<p align="center">
<img src="https://www.bespokepremium.com/wp-content/uploads/2016/08/Sector-Pie.png"  height=300>
</p>

El índice bursátil S&P500 es una herramienta útil para los inversores, ya que les permite realizar un seguimiento del rendimiento de las 500 empresas más grandes de Estados Unidos en su conjunto, así como de las empresas individuales dentro de las mismas industrias. Esto significa que los inversores pueden diversificar su cartera de inversión, ya que pueden invertir en empresas de diferentes sectores y reducir el riesgo de perder dinero debido a la fluctuación en un solo sector.

Además, invertir en el índice S&P500 brinda cierta tranquilidad a los inversores, ya que están invirtiendo en empresas representativas de la economía de Estados Unidos, que se considera una de las más fuertes y estables del mundo. Sin embargo, es importante tener en cuenta que incluso con el respaldo del índice, se necesita un análisis detallado para identificar ciertos comportamientos del mercado y decidir cuándo y dónde invertir para obtener mayores rendimientos. En última instancia, la investigación y la planificación cuidadosas son clave para tomar decisiones de inversión informadas y exitosas. </br>

Para la realizacion de este ejercicio, se tomo como referencia la innovacion tecnologica y se hizo mencion a tres grandes industria e historicas de la rama de la tecnologia siendo estas:

* International Business Machines Corporation (IBM)
* Intel Corporation (INTC)
* Microsoft Corporation (MSFT)

<p align="center">
<img src="https://cdn.arstechnica.net/wp-content/uploads/2011/10/ibm_vs_ms-4e89c70-intro.jpg"  height=300>
</p>

<p align="center">
<img src="https://tse1.mm.bing.net/th?id=OIP.qBEuk98ABIV646qcJFx6IwHaEK&pid=Api&P=0"  height=300>
</p>

<p align="center">
<img src="https://tse4.mm.bing.net/th?id=OIP.KXEsmh4_up4hSBqZ3uxWUgHaE8&pid=Api&P=0"  height=300>
</p>

<h1>Análisis Exploratorio de los datos (EDA)</h1>

Para poder analizar el mercado bursátil, utilizamos las siguientes herramientas:

* Yahoo Finance
* wikipedia

Estas permitieron acceder a datos financieros que presentaremos en nuestro archivo realizado en Python*. 

Antes de analizar puntualmente cada empresa, nos parece importante estudiar el comportamiento del índice para conocer su tendencía y saber si vale la pena invertir en cualquiera de las compañías que lo componen por supuesto con su previo análisis.

* Histórico correspondiente al precio de cierre del índice ***S&P500*** (1990 - 2023) 

```shell
empresas = ['GSPC']

recolector =[]
for nemo in empresas:
    ticker =yf.Ticker(nemo)
    px = ticker.history(start="2000-01-01", end="2023-03-27")['Close']
    px.name = nemo

    recolector += [px]

precios = pd.concat(recolector, axis=1)
```
**Nota:** Este código guarda en un Data Frame los precios de cierre para el índice bursátil en un periodo del año 2000 al 2023

<p align="center">
<img src="https://github.com/csantamaria89/Proyecto-Individual-II/blob/main/Im%C3%A1genes/GSPC1.png"  height=500>
</p>

En la imágen anterior, se puede evidenciar la tendencia alsista 📈 del índice *S&P500* a lo largo del tiempo, también se puede observar hitos importantes que describen tiempos de crisis. 

- La recesión económica de 2008, conocida como la Gran Recesión, fue la fuerte caída de la actividad económica que comenzó en diciembre de 2007 y duró hasta junio de 2009.
- Crisis económica por el Corona Virus.
- Repercusión de la Pnademia, Inflación, Guerra.

En general, el comportamiento del índice nos puede suponer una ventaja de inversión si analisamos el entorno y las crisis pues la inversion puede ser en cuanto a tendencias de crecimiento o caidas.


<h1>Grupo Inversión 1</h1>

<p align="center">
<img src="https://github.com/csantamaria89/Proyecto-Individual-II/blob/main/Im%C3%A1genes/analisis1.png"  height=100>
</p>

* Aplicamos el siguiente código para poder visualizar el valor de cierre de cada acción seleccionada durante un periodo establecido:

```shell
empresas = ['AMZN','AAPL','INTC','MSFT','NFLX']

recolector =[]
for nemo in empresas:
    ticker =yf.Ticker(nemo)
    px = ticker.history(start="2000-01-01", end="2023-03-27")['Close']
    px.name = nemo

    recolector += [px]

precios = pd.concat(recolector, axis=1)
```
**Nota:** Este código guarda en un Data Frame los precios de cierre de las diferentes acciones en un periodo del año 2000 al 2023

Con el siguiente código obtenemos el precio de cierre de la acción del día anterior su valor y porcentaje de ganancia.

```shell
import pandas as pd
import requests

# API key de Alpha Vantage
api_key = "YOUR KEY HERE"

# Símbolo de la acción que queremos obtener
symbol = "MCD"

# URL para obtener los datos de la acción
url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"

# Hacemos la petición HTTP GET
response = requests.get(url)

# Obtenemos los datos en formato JSON
data = response.json()

# Creamos un diccionario con los valores que queremos
stock_info = {
    "Last Price": data["Global Quote"]["05. price"],
    "Change": data["Global Quote"]["09. change"],
    "% Change": data["Global Quote"]["10. change percent"]
}

# Creamos el DataFrame
df = pd.DataFrame(stock_info, index=[0])
df.to_csv("Alpha_McDonalds.csv", index=False)
```
**Nota:** El código anterior se basa en la API de Alpha Vantage, para ello directamente en su plataforma se debe crear un Key para que permita el uso del código.

- El análisis de estas acciones corresponde al sector de *Tecnología de la información*, *Consumo ocasional* y *Servicios de comunicación* 
<p align="center">
<img src="https://github.com/csantamaria89/Proyecto-Individual-II/blob/main/Im%C3%A1genes/inversion1.png"  height=500>
</p>

De acuerdo con la imágen anterior podemos concluir que para las empresas analisadas, se evidencia que les afecto las crisis mencionadas anteriormente. Sin embargo, todas han tenido un crecimiento o por lo menos se han logrado estabilizar con las diferentes coyunturas que vive del país.

🚨**Netflix**: Puntualmente vemos un caso de tendencia bajista 📉 a finales del 2021 y 2022.

<p align="center">
<img src="https://github.com/csantamaria89/Proyecto-Individual-II/blob/main/Im%C3%A1genes/Tnetflix.png"  height=300>
</p>

Las acciones de Netflix se desplomaron un 35% después de que la empresa revelara una fuerte caída en los suscriptores, y advirtiera que millones más están listos para abandonar el servicio.
- La compañía perdió más de US$50.000 millones de su valor en el mercado, ya que los expertos indicaron que enfrenta dificultades para volver a la normalidad.
- Netflix afronta una intensa competencia por parte de sus rivales y también se vio afectada después de que subió los precios y se fue de Rusia.
- Impulsar el crecu¿imiento de clientes con nuevo servicio gratuito con publicidad.
- Se estima que más de 100 millones de hogares utilizan su servicio de manera ilegal.</br>
***fuente:***("https://www.bbc.com/mundo/noticias-61182426")

<h1>Grupo Inversión 2</h1>

<p align="center">
<img src="https://github.com/csantamaria89/Proyecto-Individual-II/blob/main/Im%C3%A1genes/analisis2.png"  height=100>
</p>

* Repetimos el proceso del grupo anterior para ver el histórico del precio de cierre para este grupo de compañias.

El análisis de estas acciones corresponde al sector del Consumo Ocasional, Productos básicos de consumo y Salud
<p align="center">
<img src="https://github.com/csantamaria89/Proyecto-Individual-II/blob/main/Im%C3%A1genes/inversion2_1.png"  height=500>
</p>

Con en análisis del gráfico, podemos identificar que a la empresa de Walmart (Productos básicos de consumo) y Moderna (Salud) no fueron afectadas por la pandemia y que por el contrario han tenido una tendencia alsista 📈 lo que representa un muy buen escenario para invertir.

<h1>KPIs Conclusiones</h1>

Con el análisis previo y el perfil de inversion conservador, podemos identificar fácilmente los acciones por las cuales podríamos invertir. A continuación se presentaran los siguientes KPIs para poder conluir que alternativas tenemos para invertir a corto o largo plazo.

<p align="center">
<img src="https://github.com/csantamaria89/Proyecto-Individual-II/blob/main/Im%C3%A1genes/kpis.png"  height=400>
</p>

***KPIs***

1. **Market Cap** (Capitalización del Mercado): Valor total de las acciones en circulación de una empresa. </br>

    Se calcula multiplicando el número de acciones en circulación sw una empresa por el precio actual de la acción. </br>
    
    CAP = Número de Acciones x Precio de la Acción </BR>
    
    El Market cap es un dato importante tanto para conocer el tamaño de la empresa como múltiplo para calcular diferentes ratios financieros. Además, se           utiliza esta cifra para determinar el tamaño de una empresa en lugar de usar el total de las ventas o los activos totales.</BR>
    
2. **Earnings per Share** EPS (Beneficio por Scción): Son los beneficios que le corresponden al accionista por cada acción.

    EPS básico = (Beneficio neto-Dividendos de acciones preferentes)/(Media ponderada del número de acciones ordinarias en circulación)
    
    **Es necesario excluir la parte correspondiente a los accionistas preferentes.
    
3. **Range (52 Week)** Este indicador nos muestra el valor mínimo y el máximo del precio de cierre de la acción durante las últimas 52 semanas. Con este valor podemos compararlo con el precio de cierre actual y tener un indicador que nos alerte si el precio de cierre actual está más cerca del valor negativo o incluso ha sobrepasado ese umbral o viceversa.
