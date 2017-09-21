# Entrega 1 - Projeto 2 - DTMF

Esta etapa do projeto consiste na construção de um código que gera tons utilizados na telefonia moderna (<i>encoder</i>) e um código que recebe e salva esses tons (<i>decoder</i>), utilizando o sistema <i>Dual-Tone Multi-Frequency</i> (DTMF).

## Descrição da geração e da frequência dos tons

Cada um dos tons correspondentes aos numeros de 0 a 9 é gerado com base em duas frequências, mostradas na tabela a seguir:

|    | <b>1209 Hz</b> | <b>1336 Hz</b> | <b>1477 Hz</b>   | <b>1633 Hz</b>   |
|-------------|--------------------|-------------|--------------------|
| <b>697 Hz</b>|      1         |        2       |        3         |           A      |
| <b>770 Hz</b>|4|5|6|B|
| <b>852 Hz</b>|7|8|9|C|
| <b>941 Hz</b>|<i>*</i>|0|#|D|


| <b>1209 Hz</b> | <b>1336 Hz</b> | <b>1477 Hz</b>   | <b>1633 Hz</b>   |
|-------------|--------------------|
| Hexadecimal |         0x18005    |
| Binária     |  11000000000000101 |
| Polinomial  | x^16+x^15+x^12+x^0 |
