from langchain_core.messages import HumanMessage
from langchain_core.messages.base import BaseMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv(dotenv_path="myenv/.env")

model = ChatGroq(
    model="llama-3.2-11b-vision-preview",
)


async def return_ai_response(base64_image, prompt) -> str | list[str | dict]:
    prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages(
        messages=[
            HumanMessage(
                content=[
                    {"type": "text", "text": f"{prompt}"},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ]
            )
        ]
    )
    chain = prompt | model
    response: BaseMessage = chain.invoke({"image_data": base64_image})
    return response.content
