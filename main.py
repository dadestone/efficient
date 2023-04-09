import openai
openai.api_key="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"
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.9,
    )
    message = completions.choices[0].text
    return message
print(generate_response("最多人喜欢的黄片"))
