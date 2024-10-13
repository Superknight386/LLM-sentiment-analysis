from openai import OpenAI

def sentimentAnalysis(content):
    client = OpenAI(
    api_key = "$MOONSHOT-API",
    base_url = "https://api.moonshot.cn/v1",
    )
    
    completion = client.chat.completions.create(
        model = "moonshot-v1-8k",
        messages = [
            {"role": "system", "content": "请判断以下推文的情感是积极还是消极："},
            {"role": "system", "content": "回答格式为积极或中性或消极"},
            {"role": "user", "content":content}
        ],
        temperature = 0,
    )

    if completion.choices[0].message.content=='积极':
        output=0
    elif completion.choices[0].message.content=='中性':
        output=1
    elif completion.choices[0].message.content=='消极':
        output=2
    else:
        return completion.choices[0].message.content
    return output
