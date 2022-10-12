# Predictive Analytics
!["Resultado de uma análise preditiva"](./img/Print%20de%20Match%20Table.png)
Originalmente esta é a implementação de uma atividade de Compiladores.
!["Questão 19"](./img/Quest%C3%A3o%2019.png)
Sabendo-se que seria utilizado **Tabela LL(1)** implementada sem auxílio de algoritmo, foi realizada uma adaptação da gramática:

| S | -> | 0A | B |
| - | -- | -- | - |
| A | -> | aA | 1 |
| B | -> | b |

## Uso
1. Defina em [grammar](./grammar.py) sua gramática no formato "Tabela LL(1)";
2. Em [util](./util.py) informe seus símbolos terminais e a entrada para [predictive_analytics](./predictive_analytics.py).
3. Interprete o código:
```
python3 predictive_analytics.py
```
4. Visualize o banco [Match Table](./Match%20Table) da forma que preferir (estou utilizando a extensão [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer) no Visual Studio Code).