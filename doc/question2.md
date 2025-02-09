# Discussão sobre a Questão 2

## Algoritmo genérico

A ideia é combinar até dois valores de requisição por vez se o seu valor combinado for permitido dentro de uma única requisição.
Uma ideia inicial é ordenar os valores antes de combinar.
A partir daí, temos pelo menos duas possibilidades:

- começar a partir do maior valor de todos $X$, combinar com o maior valor encontrado com o qual ele pode ser combinado $Y$ ou enviar $X$ sozinho em uma remessa e seguir para o próximo maior valor; e assim por diante
- começar a partir do maior valor de todos $X$, combinar com o menor valor de todos os restantes $Z$ ou enviar $X$ sozinho em uma remessa e seguir para o próximo maior valor; e assim por diante

## Opção escolhida

Pensando no desempenho do algoritmo, a segunda opção é melhor porque a primeira necessita de uma busca por $Y$, mas na segunda não é necessário fazer uma busca por $Z$, que já é o menor restante ainda não combinado.

## Complexidades

A grosso modo, a complexidade da ordenação da lista é $O(n \log n)$.
Para cada valor vamos tentar combinar ele com o menor valor ainda não combinado.
Essa etapa tem complexidade $O(n)$.
Ou seja:

| Operação                         | Complexidade  |
| -------------------------------- | ------------- |
| ordenação das requisições        | $O(n \log n)$ |
| $n/2$ combinações de requisições | $O(n)$        |
| algoritmo completo               | $O(n \log n)$ |
