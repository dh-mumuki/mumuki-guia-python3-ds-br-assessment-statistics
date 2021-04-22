Implemente a função `expectativa`, que recebe como argumento a _distribuição de probabilidade_ de uma variável aleatória numérica discreta _X_, e retorna seu valor esperado, também conhecido como média ou expectativa.

Por exemplo, se _X_ é o resultado um dado de quatro faces honesto, os resultados 1, 2, 3 e 4 são equiprováveis: 25% cada (o espaço amostral é o conjunto {1,2,3,4}). Nesse caso, a distribuição de probabilidade pode ser representada em Python assim:

```python
distribuicao = [
  (1, 0.25),
  (2, 0.25),
  (3, 0.25),
  (4, 0.25)
]
```

A expectativa é definida assim:

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{200}&space;\text{expectativa}&space;=&space;\sum_i&space;x_i&space;P(x_i)" target="_blank"><img src="https://latex.codecogs.com/png.latex?\dpi{200}&space;\text{expectativa}&space;=&space;\sum_i&space;x_i&space;P(x_i)" title="\text{expectativa} = \sum_i x_i P(x_i)" width="300px" /></a>

onde os _x_ na somatória representam todos os possíveis resultados e _P(x)_ é a probabilidade de _x_ ocorrer.

No exemplo acima, esse cálculo ficaria assim:

```python
>>> 1 * 0.25 + 2 * 0.25 + 3 * 0.25 + 4 * 0.25
2.5
```

Ou seja, sua função deve ser tal que:

```python
>>> expectativa(distribuicao)
2.5
```

Mas sua função deve ser mais versátil que isso, pois estamos interessados em situações mais complexas. Por exemplo, suponha que o resultado 1 seja mais provável que os outros, segundo essa distribuição de probabilidades:

```python
distribuicao_nao_honesta = [
  (1, 0.4),
  (2, 0.2),
  (3, 0.2),
  (4, 0.2)
]
```

Nesse caso teríamos:

```python
>>> expectativa(distribuicao_nao_honesta)
2.2
```

Finalmente, sua função deve ser capaz de se defender de argumentos que não representam uma distribuição de probabilidade. Para isso você deve verificar se a soma das probabilidades (segundo elemento da tupla) é igual a um. Se não for, você deve **lançar uma exceção** do tipo `ValueError`. Por exemplo:

```python
>>> expectativa([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 9, in expectativa
ValueError: Argumento inválido.
```

Você pode fazer isso usando a seguinte instrução em Python (apenas quando notar a condição anômala, claro):

```python
raise ValueError('Argumento inválido.')
```