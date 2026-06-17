"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    import matplotlib.pyplot as plt
    import pandas as pd

    plt.Figure()

    colors = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey',
    }

    zorder = {
        'Television': 1, # mientras mas alto el numero, mas arriba se dibuja la linea
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }

    linewidths = {
        'Television': 2, # mientras mas alto el numero, mas gruesa se dibuja la linea
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2,
    }

    df = pd.read_csv("files/input/news.csv", index_col=0, sep=",") 

    for col in df.columns:
        plt.plot(df[col], label=col, color=colors[col], zorder=zorder[col], linewidth=linewidths[col])

    plt.title("How people get their news", fontsize=16)
    # gca se utiliza para obtener el objeto de los ejes actuales, y luego se puede modificar su apariencia
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(x=first_year, y=df[col][first_year], color=colors[col], zorder=zorder[col], s=100) # s es el tamaño del punto
        plt.text(first_year - 0.2,df[col][first_year],col + '' + str(df[col][first_year]) + "%",ha='right',va='center',color=colors[col]) 

        last_year = df.index[-1]
        plt.scatter(x=last_year, y=df[col][last_year], color=colors[col], zorder=zorder[col], s=100)
        plt.text(last_year + 0.2,df[col][last_year],col + '' + str(df[col][last_year]) + "%",ha='left',va='center',color=colors[col])

    plt.xticks(df.index, labels=df.index, ha='center')
    plt.show()
    plt.tight_layout()
    """
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    df = pd.read_csv('files/input/news.csv', index_col=0)

    plt.Figure()

    colors = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey',
    }

    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }

    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2,
    }

    for col in df.columns:
        plt.plot(
            df[col],
            color=colors[col],
            label=col,
            zorder=zorder[col],
            linewidth=linewidths[col]
            )

    plt.title('How people get their news', fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col],
        )


        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + '' + str(df[col][first_year]) + "%",
            ha='right',
            va='center',
            color=colors[col],
        ) 

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
            zorder=zorder[col],
        )

        plt.text(
            last_year + 0.2,
            df[col][last_year],
            col + '' + str(df[col][last_year]) + "%",
            ha='left',
            va='center',
            color=colors[col],
        )
    
    plt.tight_layout()
    os.makedirs('files/plots', exist_ok=True)
    plt.savefig('files/plots/news.png')
    plt.savefig("./files/plots/news.png")

pregunta_01()