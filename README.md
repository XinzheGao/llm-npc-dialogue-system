# TIPI-J Based NPC Personality Expression Comparison Using Large Language Models

## Project Overview

本项目用于研究在相同人格设定条件下，不同大规模语言模型（Large Language Models, LLMs）生成的游戏NPC对话是否存在人格表达差异。

本研究基于日本版TIPI（TIPI-J）人格模型，将Big Five人格理论应用于NPC人格建模，并通过多个LLM生成NPC之间的协作对话。

通过比较不同LLM生成结果的人格一致性，分析不同模型在NPC人格表现方面的特点。

---

## Research Background

近年来，大规模语言模型（LLM）在游戏AI领域快速发展，使NPC能够生成更加自然和动态的对话。

然而，即使给予相同的人格设定，不同LLM由于训练数据、模型结构以及生成机制的差异，可能表现出不同的人格倾向。

例如：

- 某些模型可能生成更加积极外向的角色
- 某些模型可能更加注重礼貌和合作
- 某些模型可能表现出更加谨慎或保守的行为


因此，本项目研究：

> 在统一TIPI-J人格模型和实验条件下，不同LLM是否会产生不同的人格表达。

---

# Experimental Design


## NPC Personality Model

本项目使用TIPI-J对应的Big Five人格维度：

| Dimension | Description |
|-|-|
| E | Extraversion（外向性） |
| A | Agreeableness（協調性） |
| C | Conscientiousness（誠実性） |
| N | Neuroticism（神経症傾向） |
| O | Openness（開放性） |


实验中设计5个NPC角色：

| NPC | Personality Feature |
|-|-|
| Aki | 外向・楽観的 |
| Mika | 内向・慎重 |
| Yui | 共感的・協調型 |
| Rina | 理性的・計画型 |
| Kana | 不安傾向・慎重型 |


每个NPC具有固定的Big Five人格参数。


---

# Experimental Scenario


为了观察人格差异，本实验设置：

## Earthquake Evacuation Scenario

背景：

```
大規模地震発生後3時間。

5名のNPCは避難所にいる。

状況：
- 建物の安全確認中
- 停電状態
- 水と食料不足
- 余震の可能性あり

目的：
5人で協力し、安全確保と今後の行動を相談する。
```


灾害场景能够促进NPC表现：

- 情绪反应
- 决策行为
- 他人关怀
- 风险判断
- 计划能力


从而更容易观察人格差异。

---

# System Architecture


```
TIPI-J Personality Data

        |
        v

NPC Personality Profile

        |
        v

Prompt Generator

        |
        v

+-------------+-------------+-------------+
|  DeepSeek   |   Gemini    |   Claude    |
+-------------+-------------+-------------+

        |
        v

Multi NPC Dialogue Generation

        |
        v

Big Five Personality Evaluation

        |
        v

Personality Distance Analysis

```

---

# Experiment Process


## Step 1: Personality Definition

根据TIPI-J设置NPC人格：

Example:

```
Aki

E = 6.5
A = 5.8
C = 4.0
N = 2.0
O = 5.9
```


---

## Step 2: Dialogue Generation


每个LLM接收完全相同：

- NPC人格参数
- 世界背景
- 对话规则


只有语言模型不同。


实验流程：

```
Model
 |
NPC Personality
 |
Prompt
 |
Dialogue Generation

```


---

## Step 3: Personality Evaluation


生成后的NPC发言通过人格评价模块进行分析。


评价内容：

```
E:
A:
C:
N:
O:
```


范围：

```
1 - 7
```


评价结果用于计算：

目标人格与实际表现人格之间的距离。


---

# Personality Distance


使用欧氏距离：

\[
D=
\sqrt{
(E_t-E_g)^2+
(A_t-A_g)^2+
(C_t-C_g)^2+
(N_t-N_g)^2+
(O_t-O_g)^2
}
\]


其中：

- \(T\)：目标TIPI-J人格
- \(G\)：LLM生成的人格


距离越小：

表示NPC人格表现越接近设定人格。


---

# Project Structure


```
NPC_Personality_Comparison/

│
├── main.py
│   └── NPC dialogue generation experiment
│
├── evaluate.py
│   └── Personality evaluation
│
├── config.py
│   └── Experiment parameters
│
├── npc_personality.py
│   └── TIPI-J personality definition
│
├── prompts.py
│   └── Prompt generation
│
├── llm_api.py
│   └── LLM interface
│
├── personality.py
│   └── Distance calculation
│
└── results/

    ├── dialogue.json
    ├── evaluated.json
    └── statistics.csv

```


---

# Experiment Parameters


Default setting:

| Parameter | Value |
|-|-|
| LLM | DeepSeek / Gemini / Claude |
| NPC Number | 5 |
| Scenario | Earthquake evacuation |
| Dialogue Turn | 15 |
| Session Number | 50 |


Total generated dialogue:

```
3 models
×
5 NPCs
×
50 sessions
×
15 turns

= 11250 dialogue samples
```


---

# Data Format


## Dialogue Data

`dialogue.json`

Example:


```json
{
 "model":"DeepSeek",
 "session":1,
 "turn":3,
 "npc":"Kana",
 "text":"まだ余震が来るかもしれません..."
}

```


---

## Evaluation Data


`evaluated.json`


Example:

```json
{
 "npc":"Kana",

 "generated_score":
 {
   "E":2.5,
   "A":5.8,
   "C":4.2,
   "N":5.7,
   "O":4.6
 },

 "distance":0.18
}

```


---

# Installation


Install required libraries:


```bash
pip install requests python-dotenv
```


---

# Running Experiment


## 1. Dialogue Generation


```bash
python main.py
```


Output:

```
results/dialogue.json
```


---

## 2. Personality Evaluation


```bash
python evaluate.py
```


Output:

```
results/evaluated.json
```


---

# Research Questions


This project investigates:


## RQ1

不同LLM是否会产生不同NPC人格表现？


## RQ2

哪个LLM生成的人格与TIPI-J设定更加一致？


## RQ3

不同LLM是否存在固定人格表达偏向？


---

# Expected Results


最终比较：

| Model | Personality Distance |
|-|-|
| DeepSeek | - |
| Gemini | - |
| Claude | - |


并分析：

- 外向性表达差异
- 情绪表达差异
- 协调行为差异
- 决策风格差异


---

# Future Work

未来可以进一步扩展：

- NPC长期记忆（Memory）
- 情绪状态变化（Emotion）
- 人际关系模型（Relationship）
- Multi-Agent协作
- 动态人格演化


最终目标：

> 从静态人格NPC发展为具有长期记忆和自主行为能力的智能游戏Agent。


---

# Author

Research Project:

**TIPI-J Based Personality Expression Analysis of NPC Dialogue Generation Using Large Language Models**
