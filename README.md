# Classificador de Câncer de mama

### Atividade desenvolvida para o trabalho final da disciplina de Inteligência Computacional

## Equipe

<table style="text-align: center">
  <tr>
    <td><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/51974850?v=4" width="100px;" alt=""/><br /><sub><b>Adrian Grosch</b></sub></td>
    <td><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/54003782?v=4" width="100px;" alt=""/><br /><sub><b>Matheus Parro de Sousa</b></sub></td>
  </tr>
</table>

## Problema

<p>O problema se trata de uma classificação de nódulos mamários, sendo eles malignos ou benignos, baseado em um dataset que contém suas características</p> 

## Dataset

<p>
O dataset utilizado para o presente classificador é uma cópia dos conjuntos de dados UCI ML Breast Cancer Wisconsin (Diagnostic) disponível em: <a href="https://goo.gl/U2Uwz2">https://goo.gl/U2Uwz2</a>.

As características são computadas através de uma imagem digitalizada da massa do nódulo adquirida através de uma agulha extremamente fina.
</p>

<table>
<tr>
<th colspan="100%">Características do conjunto de dados</th></tr>
<tr><td>Número de Instâncias</td><td>569</td></tr>
<tr><td>Distribuição das classes</td><td>212 - Maligno | 357 - Benigno</td></tr>
<tr><td>Número de Atributos</td><td>30 atributos numéricos preditivos e a classe
</td></tr>
<tr><td>Informação de Atributo</td><td>
<ul>
<li>Raio (média das distâncias do centro aos pontos do perímetro)</li>
<li>Textura (desvio padrão dos valores da escala de cinza)</li>
<li>Perímetro</li>
<li>Área</li>
<li>Suavidade (variação local em comprimentos de raio)</li>
<li>Compacidade (perímetro ^ 2 / área - 1,0)</li>
<li>Concavidade (gravidade das porções côncavas do contorno)</li>
<li>Pontos côncavos (número de porções côncavas do contorno)</li>
<li>Simetria</li>
<li>Dimensão fractal (“aproximação do litoral” - 1)</li>
<li>Classe (Maligno | Benigno)</li>
</ul>
</td></tr>
<tr>
<td colspan="100%">
A média, o erro padrão e o “pior” ou maior (média dos três piores / maiores valores) desses recursos foram calculados para cada imagem, resultando em 30 recursos. Por exemplo, o campo 0 é o raio médio, o campo 10 é o raio SE, o campo 20 é o pior raio.
</td>
</tr>
</table>

## Técnica
<p>Para desenvolver o trabalho, foi utilizada a biblioteca Scikit Learn, que é uma biblioteca de machine learning presente na linguagem Python. A biblioteca foi utilizada pois já fornece nativamente uma grande quantia de datasets prontos para uso e também um módulo que nos permite aplicar a téncica da Árvore de Decisão, um dos métodos mais comuns dentro da aprendizagem de máquina, para realizar a classificação desejada.