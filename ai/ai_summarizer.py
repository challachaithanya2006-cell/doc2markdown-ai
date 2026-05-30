from openai import OpenAI
import os
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text):
    r=client.chat.completions.create(model="gpt-4o-mini",messages=[{"role":"user","content":f"Summarize:\n{text}"}])
    return r.choices[0].message.content
