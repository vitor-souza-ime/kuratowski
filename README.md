
# Teorema de Kuratowski – Visualização Computacional

Este repositório contém uma implementação simples em **Python** para ilustrar o **Teorema de Kuratowski**, utilizando a biblioteca [NetworkX](https://networkx.org/) para construção e análise de grafos e [Matplotlib](https://matplotlib.org/) para visualização.

## 📌 Descrição

O **Teorema de Kuratowski** afirma que um grafo é **não planar** se, e somente se, contém como subgrafo uma subdivisão de:
- **K₃,₃**: grafo bipartido completo com partições de três vértices cada.
- **K₅**: grafo completo de cinco vértices.

Este projeto implementa a construção e verificação de planaridade de dois grafos:
- **K₃,₃** – exemplo de grafo **não planar**.
- **Grade 3x3** – exemplo de grafo **planar**.

A verificação é realizada com o algoritmo de **Boyer–Myrvold** (2004), implementado na biblioteca NetworkX.

## 📂 Estrutura do Projeto

```

kuratowski/
│── main.py        # Código principal para construção e análise dos grafos
│── README.md      # Este arquivo

````

## 🚀 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/vitor-souza-ime/kuratowski.git
cd kuratowski
````

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Se preferir, instale manualmente:

```bash
pip install networkx matplotlib
```

### 4. Execute o código

```bash
python main.py
```

## 📊 Saída Esperada

Ao executar o programa, o console exibirá:

```
K3,3 planar? False
Grafo 3x3 planar? True
```

Além disso, será gerada uma visualização gráfica com dois subplots:

* À esquerda: **K₃,₃** (não planar).
* À direita: **Grade 3x3** (planar).

## 📖 Referências

* Kuratowski, K. (1930). *Sur le problème des courbes gauches en topologie*. Fundamenta Mathematicae, 15, 271–283.
* Boyer, J. M., & Myrvold, W. J. (2004). *On the cutting edge: simplified O(n) planarity by edge addition*. Journal of Graph Algorithms and Applications, 8(3), 241–273.
* NetworkX Documentation: [https://networkx.org/](https://networkx.org/)

