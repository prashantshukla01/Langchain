from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1️⃣ Hugging Face endpoint (CHAT / conversational model)
llm_endpoint = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",        # 🔥 REQUIRED
    max_new_tokens=256,
    temperature=0.7
)

# 2️⃣ Wrap with ChatHuggingFace (MANDATORY for chat models)
chat_model = ChatHuggingFace(llm=llm_endpoint)

# 3️⃣ Prompt
prompt = PromptTemplate(
    template="Explain {topic} in simple words.",
    input_variables=["topic"]
)

# 4️⃣ Output parser (string)
parser = StrOutputParser()

# 5️⃣ Chain (Prompt → Chat Model → String)
chain = prompt | chat_model | parser

# 6️⃣ Invoke
result = chain.invoke({"topic": "Black Hole"})
print(result)
