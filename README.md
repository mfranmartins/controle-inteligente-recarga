# Controle Inteligente de Sessão de Recarga

Projeto desenvolvido para a **Sprint 3 — Controle Inteligente de Sessão de Recarga**, utilizando **Raspberry Pi Pico**, **MicroPython** e **Wokwi**.

O protótipo simula um controlador inteligente de energia capaz de analisar a relação entre **geração** e **consumo** e determinar se uma sessão de recarga pode ser autorizada, reduzida ou bloqueada.

## Objetivo

Desenvolver um protótipo funcional que demonstre:

* Leitura de dados por meio de entradas;
* Processamento dos dados pelo Raspberry Pi Pico;
* Cálculo da energia disponível;
* Tomada de decisão baseada nos valores obtidos;
* Indicação do estado da recarga por LEDs;
* Representação de dados nos sistemas decimal, binário e hexadecimal;
* Aplicação de conceitos de **Arquitetura de Computadores**.

## Funcionamento

O sistema utiliza dois potenciômetros para simular:

* **Potenciômetro 1:** geração de energia;
* **Potenciômetro 2:** consumo de energia.

Os valores lidos pelo ADC do Raspberry Pi Pico são convertidos para uma faixa de **0 a 5000 W**.

A energia disponível é calculada pela fórmula:

```text
Energia disponível = Geração - Consumo
```

Com base nesse resultado, o sistema define o estado da recarga:

| Energia disponível | Status             | LED         |
| -----------------: | ------------------ | ----------- |
|           ≥ 1000 W | Recarga autorizada | 🟢 Verde    |
|   > 0 W e < 1000 W | Recarga reduzida   | 🟡 Amarelo  |
|              ≤ 0 W | Recarga bloqueada  | 🔴 Vermelho |

O limites foram definidos para fins de simulação do protótipo.

## Componentes

* Raspberry Pi Pico;
* 2 potenciômetros;
* 3 LEDs;
* 3 resistores de 220Ω;
* Protoboard;

## Pinagem

| Componente              | Pino do Raspberry Pi Pico |
| ----------------------- | ------------------------- |
| Potenciômetro — Geração | GP26 / ADC0               |
| Potenciômetro — Consumo | GP27 / ADC1               |
| LED Verde               | GP16                      |
| LED Amarelo             | GP17                      |
| LED Vermelho            | GP18                      |

## Sistemas Numéricos

O sistema apresenta os valores de **geração** e **consumo** em três sistemas numéricos:

* Decimal;
* Binário;
* Hexadecimal.

Exemplo:

```text
Geração em decimal:      4000 W
Geração em binário:     111110100000
Geração em hexadecimal: 0FA0
```

Essa representação demonstra como os dados podem ser armazenados e processados em diferentes sistemas numéricos utilizados na computação.

## Arquitetura de Computadores

O projeto relaciona diferentes etapas do funcionamento do sistema aos conceitos de Arquitetura de Computadores:

### Entrada

Os potenciômetros fornecem valores analógicos que são lidos pelo **ADC (Conversor Analógico-Digital)** do Raspberry Pi Pico.

### Processamento

O processador do Pico executa:

1. Leitura dos sensores;
2. Conversão dos valores para watts;
3. Cálculo da energia disponível;
4. Comparação com os limites definidos;
5. Definição do estado da recarga.

### Memória

Durante a execução, os valores de geração, consumo, energia disponível e status são armazenados em variáveis na memória do sistema.

### Saída

Os resultados são apresentados por meio de:

* LEDs indicadores;
* Terminal serial.

### Fluxo do sistema

```text
Potenciômetros
      ↓
     ADC
      ↓
Valores digitais
      ↓
   Memória
      ↓
Processamento
      ↓
Geração - Consumo
      ↓
    Decisão
      ↓
 ┌────┴────┐
 ↓         ↓
LEDs    Terminal
```

## Como executar

O projeto pode ser executado diretamente no **Wokwi**.

1. Abra o projeto no Wokwi [clicando aqui](https://wokwi.com/projects/475369911464991745;)
2. Clique em "Start the simulation"
3. Ajuste os dois potenciômetros;
4. Observe a alteração dos valores no terminal;
5. Verifique a mudança dos LEDs de acordo com a energia disponível.

O terminal é atualizado quando os valores de geração ou consumo são alterados.

## Demonstração

Vídeo demonstrando o funcionamento do protótipo: [Vídeo no Youtube](https://youtu.be/NqPcSehrr5E)

## Integrantes

* Ana Berbel - RM: 574176
* Gustavo Piccoli - RM: 569984
* Julian Moncoski - RM: 572603
* Marcelo Martins - RM: 573905
* Maria Medeiros - RM: 574094
* Pietro Lorande - RM: 569125

## Instituição e curso

**FIAP — Faculdade de Informática e Administração Paulista**

**Ciência da Computação**

Projeto desenvolvido para a **Sprint 3 — Controle Inteligente de Sessão de Recarga**.
