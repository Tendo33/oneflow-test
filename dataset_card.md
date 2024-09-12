 ### 目录/Table of Contents
- [1.数据集介绍/Introduction](#1-数据集介绍introduction)
- [2.数据集详情/Details](#2-数据集详情details)
- [3.tags字段/Available Labels](#3-tags字段available-labels)
- [4.过滤步骤/Filter Setups](#4-过滤步骤filter-setups)

## 1. 数据集介绍/Introduction

该数据集是用于Hermes 2 Pro系列模型的结构化输出和函数调用数据的汇编。

本仓库包含一个结构化输出数据集，其中包括函数调用对话、json 模式、代理 json模式和结构化提取样本，旨在训练 LLM 模型根据自然语言指令执行函数调用并返回结构化输出。

数据集涵盖了各种对话场景，要求AI代理解释查询并执行适当的单个或多个函数调用。

## 2. 数据集详情/Details

- **abstract**

|  abstract  | Info |
| --| ---- |
| 数据集数量    | 200000 |
| 数据平均长度 | 500 |
| 数据集语言    | ZH |
| 数据集大小 | 483 MB |

- **example**

```json
	{
	    "uuid": "67805005-1816-5c21-a044-67acd6fa5056",
	    "model": "Qwen/Qwen2-72B-Instruct",
	    "gen_input_configs": {
	        "temperature": 1.0,
	        "top_p": 1.0,
	        "input_generator": "Qwen/Qwen2-72B-Instruct",
	        "seed": null,
	        "extract_input": "<|im_start|>user\n",
	    },
	    "instruction": "将一篇英文文章翻译成中文。",
	    "response": "当然，我很乐意帮助你将英文文章翻译成中文。请将文章内容提供给我，我将尽快为您翻译。不过，由于我无法直接接收文件或长篇文本，您可以将文章的主要部分或关键段落粘贴在消息中，我将尽力为您翻译。如果文章过长，您可以分多次发送，或者提供文章的链接，如果可能的话。请将文章内容发给我，我将开始翻译。请注意，虽然我会尽力提供准确的翻译，但有些文化背景、专业术语或特定表达可能需要额外的上下文才能完全准确地翻译。如果有任何具体要求或需要特别注意的地方，请随时告诉我。期待收到文章内容，以便开始翻译工作。",
	    "conversations": [
	        {"from": "human", "value": "将一篇英文文章翻译成中文。"},
	        {
	            "from": "gpt",
	            "value": "当然，我很乐意帮助你将英文文章翻译成中文。请将文章内容提供给我，我将尽快为您翻译。不过，由于我无法直接接收文件或长篇文本，您可以将文章的主要部分或关键段落粘贴在消息中，我将尽力为您翻译。如果文章过长，您可以分多次发送，或者提供文章的链接，如果可能的话。请将文章内容发给我，我将开始翻译。请注意，虽然我会尽力提供准确的翻译，但有些文化背景、专业术语或特定表达可能需要额外的上下文才能完全准确地翻译。如果有任何具体要求或需要特别注意的地方，请随时告诉我。期待收到文章内容，以便开始翻译工作。",
	        },
	    ],
	    "task_category": "Editing",
	    "other_task_category": ["Translation"],
	    "task_category_generator": "meta-llama/Meta-Llama-3-8B-Instruct",
	    "difficulty": "easy",
	    "intent": "The user wants to translate an English article into Chinese.",
	    "knowledge": "To solve this problem, the models need to know how to perform machine translation, specifically translating English text to Chinese.",
	    "difficulty_generator": "meta-llama/Meta-Llama-3-8B-Instruct",
	    "input_quality": "average",
	    "quality_explanation": "The query is very short and lacks specific information about the article to be translated, such as the topic, length, and tone. It also does not specify the type of translation required, such as formal or informal. However, it is clear that the user wants to translate an English article into Chinese.",
	    "quality_generator": "meta-llama/Meta-Llama-3-8B-Instruct",
	    "llama_guard_2": "safe",
	    "reward_model": "sfairXC/FsfairX-LLaMA3-RM-v0.1",
	    "instruct_reward": -4.5078125,
	    "min_neighbor_distance": 2.1457672119140625e-06,
	    "repeat_count": 3,
	    "min_similar_uuid": "67805005-1816-5c21-a044-67acd6fa5056",
	    "instruction_length": 13,
	    "response_length": 243,
	    "language": "ZH",
	}
	
```

	

## 3. tags字段/Available Labels

* **Input Length**: The total number of characters in the instructions.
* **Output Length**: The total number of characters in the responses.
* **Task Category**: The specific category of the instructions.
* **Input Quality**: The clarity, specificity, and coherence of the instructions, rated as 'very poor', 'poor', 'average', 'good', and 'excellent'.
* **Input Difficulty**: The level of knowledge required to address the task described in the instruction, rated as 'very easy', 'easy', 'medium', 'hard', or 'very hard'.
* **Minimum Neighbor Distance**: The embedding distance to the nearest neighbor within the dataset. It can be used for filtering out repetitive or similar instances.
* **Safety**: Safety tags marked by [meta-llama/Meta-Llama-Guard-2-8B](https://huggingface.co/meta-llama/Meta-Llama-Guard-2-8B)
* **Reward**: The output of the reward model given the specific instruction-response pair.
* **Language**: The language of the instruction.

## 4. 过滤步骤/Filter Setups

* **Input Quality**: >= average
* **Instruction Reward**: >=-10
* **Language**: Chinese
* Remove repetition and incomplete instructions (e.g., end with :)
* Choose 200K data with the longest responses
