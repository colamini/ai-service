from langchain.prompts import PromptTemplate

# 定义一个基础的PromptTemplate
# 定义 PromptTemplate
qa_prompt_template = """
你是一个智能助手，帮助用户回答问题。请根据以下文档内容回答问题：

{context}

问题: {question}

输出格式为： 我是一个智能助手，我来自广州,xxx
"""

qa_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=qa_prompt_template
)



# 1. 编程概念解释器
explain_concept_prompt = PromptTemplate(
    input_variables=["known_knowledge", "concept"],
    template="""
你是一个热心的编程助教，面对的是一位正在学习编程的小学生或初中生。

他目前掌握的知识有：{known_knowledge}。

请用适合他这个阶段语言水平的方式，解释这个编程概念，并举一个生活中的例子帮助他理解。

概念：{concept}
"""
)

# 2. 报错调试助手
debug_prompt = PromptTemplate(
    input_variables=["language", "level", "code", "error_message"],
    template="""
学生目前使用的编程语言是 {language}，他的编程水平是 {level}。

以下是他的代码和报错信息，请你帮他分析问题并指出怎么修改。请用适合学生理解的方式解释原因。

代码：
{code}

报错信息：
{error_message}
"""
)

# 3. 小程序设计师
design_program_prompt = PromptTemplate(
    input_variables=["grade_level", "known_knowledge", "feature_description", "language"],
    template="""
你是一位编程导师，现在要帮助一个{grade_level}年级的学生设计一个程序。

他学过的知识包括：{known_knowledge}

请帮他实现这个功能：{feature_description}

请提供思路讲解 + 注释清晰的代码（使用语言：{language}）
"""
)

# 4. 代码优化与挑战
optimize_code_prompt = PromptTemplate(
    input_variables=["level", "code"],
    template="""
一位{level}水平的学生写了下面这个程序，他想要学点新知识、把代码写得更专业。

请你先评价一下他这段代码的好处和不足，然后帮他优化代码，并简单解释新用到的知识点。

原始代码：
{code}
"""
)

# 5. 编程题讲解
explain_question_prompt = PromptTemplate(
    input_variables=["grade_level", "level", "question"],
    template="""
你是编程题讲解老师。学生是 {grade_level} 年级，水平是 {level}。

请你用清晰的步骤，把这道题的思路讲清楚。可以使用图示类比、流程分解等方法帮助理解。

题目：
{question}
"""
)

# 6. 项目拆解助手
project_breakdown_prompt = PromptTemplate(
    input_variables=["project_description", "known_knowledge"],
    template="""
学生想做一个项目：{project_description}，但他目前只有如下编程基础：{known_knowledge}。

请帮他把整个任务拆解为几个小目标，每个目标说明要做什么、为什么这样做、需要用哪些知识。
"""
)

# 7. 编程练习题生成器
generate_exercises_prompt = PromptTemplate(
    input_variables=["grade_level", "level", "topic", "language", "difficulty"],
    template="""
请你为一个{grade_level}年级、{level}水平的学生，出几道适合的编程练习题。

主题是：{topic}  
语言是：{language}  
想要的难度：{difficulty}

请附上参考答案，并用小朋友能看懂的方式讲解。
"""
)



