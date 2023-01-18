import os
import openai
import gradio as gr

#openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: how to remove plagrassim from my assignment\n Plagiarism can be removed from assignments by properly citing sources, rewriting sentences and paragraphs, and using proper paraphrasing techniques. Additionally, there are tools that can help you detect and remove plagiarized material from your assignment.",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)