# VLM-Jailbreking
This repository is the implementation of the paper **Jailbreaking Large Vision Language Models in Intelligent Transportation Systems,** which is accpted in the special session Robustness and Security of Large Language Models (ROSE-LLM) at 25th IEEE International Conference on Machine Learning and Applications (ICMLA-2025).

# Abstract
Large Vision Language Models (LVLMs) demonstrate strong capabilities in multimodal reasoning and many real-world applications, such as visual question answering. However, LVLMs are highly vulnerable to jailbreaking attacks. This paper systematically analyzes the vulnerabilities of LVLMs integrated in Intelligent Transportation Systems (ITS) under carefully crafted jailbreaking attacks. First, we carefully construct a dataset with harmful queries relevant to transportation, following OpenAI's prohibited categories to which the LVLMs should not respond. Second, we introduce a novel jailbreaking attack that exploits the vulnerabilities of LVLMs through image typography manipulation and multi-turn prompting. Third, we propose a multi-layered response filtering defense technique to prevent the model from generating inappropriate responses. We perform extensive experiments with the proposed attack and defense on the state-of-the-art LVLMs (both open-source and closed-source). To evaluate the attack method and defense technique, we use GPT-4's judgment to determine the toxicity score of the generated responses, as well as manual verification. Further, we compare our proposed jailbreaking method with existing jailbreaking techniques and highlight severe security risks involved with jailbreaking attacks with image typography manipulation and multi-turn prompting in the LVLMs integrated in ITS.

# Proposed Method Overview
![CHEESE!](Proposed_method.png)


# How to use the code
For performing the attack, please run the notebooks as per their names on corresponding models.
For performing the defense, please place the defense function from the defense.py before you return the generated response.
