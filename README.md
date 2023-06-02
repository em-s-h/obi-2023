# Observações

Esses programas foram feitos na linguagem de programação Python, portanto, antes de ler essas
respostas, eu gostaria de fazer algumas observações sobre o Python, para que você possa
entender melhor o código dessas respostas.

## Variáveis

O Python é semelhante ao JavaScript, pois não é necessário especificar o tipo das variáveis,
mas a sintaxe para criar variáveis é muito diferente.

Aqui está um exemplo de como criar uma variável em C#, JavaScript e Python:

```csharp
string nome = "Emilly";
int idade = 16;
```

```javascript
let nome = "Emilly";
let idade = 16;
```

```python
nome = "Emilly"
idade = 16
```

## Blocos de código

Ao contrário de outras linguagens, python não usa colchetes '{}' para indicar onde um bloco de
código é iniciado e finalizado, ao em vez disso, ele usa indentação para indicar se um pedaço
de código é de uma instrução 'if' ou se é uma instrução normal.

Aqui está um exemplo de código escrito em javascript e em python, este código é o mesmo
diferindo apenas na sintaxe:

```javascript
let x = 5;
let y = 5;

if (x == y) {
    console.log(x + y);
}
```

```python
x = 5
y = 5

if (x == y):
    print(x + y)
```

## Loops for

Em Python, os loops 'for' são escritos de maneira diferente de outras linguagens de programação,
aqui está um exemplo comparando JavaScript com Python:

```javascript
for (let i = 0; i <= 2; i++) {
    console.log("Numero do loop: ", i);
}
```

```python
for i in range(0, 3):
    print("Numero do loop: ", i)
```

Saída:
```shell
Numero do loop 0
Numero do loop 1
Numero do loop 2
```

Para ajudá-lo a entender esta forma do loop 'for', leia a sintaxe da seguinte forma:

'   for     i   in    x   '

'para cada item na coleção'

Quanto à função 'range()', ela ajudará o loop 'for' a iterar sobre um único número, o 0 que
passamos para a função indica em qual valor queremos iniciar a variável de iteração 'i' e o 3 é
a quantidade de vezes que desejamos repetir o bloco de código dentro do loop 'for'.

## Vetores e matrizes

Em Python, os vetores são uma coleção de muitos valores que podem ser de qualquer tipo:

```python
nomes = ["Emilly", "Arthur"]
idades = [12, 23, 65]
misturado = [12, "Emilly", True]
```
As matrizes, por outro lado, são vetores que armazenam outros vetores.

```python
armario = [
    ["blusa", "calca"],
    ["sapato", "bota"]
]
```

Em Python também podemos adicionar novos elementos a vetores e matrizes utilizando a função
'append(valor)' que adicionará 'valor' ao final do vetor ou matriz.

# Respostas

1. [Contas](./contas.py)
1. [Leilão](./leilao.py)
1. [Estoque](./estoque.py)
