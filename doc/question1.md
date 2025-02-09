# Discussão sobre a Questão 1

## Algoritmo genérico

A ideia é buscar os contratos de maior valor que ainda não foram renegociados.
Nesse sentido é preciso fazer duas coisas:
- ordenar os contratos pelo seu valor
- separar os que não foram renegociados

## O que fazer primeiro?

Considerando duas possibilidades do que fazer primeiro, e já com um olho no desempenho, foram feitas as seguintes suposições:
- os valores típicos do número e da proporção de contratos renegociados não são conhecidos
- a quantidade de contratos a ser retornada não é conhecida
- a quantidade de contratos pode ser massiva

Nesse sentido, é melhor ordenar os contratos primeiro, uma vez que podemos verificar se os contratos maiores foram renegociados.
Ou seja, se temos que retornar poucos contratos, podemos fazer poucas buscas nos contratos renegociados.

## Complexidades

A grosso modo, a complexidade da ordenação da lista é $O(n \log n)$.
A complexidade da busca dentro dos contratos renegociados pode ser feita $O(\log n)$, para uma busca binária, desde que a lista de contratos renegociados seja previamente ordenada.
Para cada contrato aberto, é preciso verificar se está entre os renegociados até preencher todos os requeridos.
Supondo que busquemos $m$ contratos vamos ter uma complexidade $O(m \log n)$ nessa etapa, mas assumimos que $m < n$.
Ou seja:

| Operação                    | Complexidade  |
| --------------------------- | ------------- |
| ordenação dos abertos       | $O(n \log n)$ |
| ordenação dos renegociados  | $O(n \log n)$ |
| $m$ buscas nos renegociados | $O(m \log n)$ |
| algoritmo completo, $m< n$  | $O(n \log n)$ |
