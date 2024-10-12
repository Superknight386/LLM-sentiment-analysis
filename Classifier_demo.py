from openai import OpenAI
 
client = OpenAI(
    api_key = "sk-nyRPODcrKUikttj2k4XcfJX94hjqmBLuGFQxWprq8luClTmY",
    base_url = "https://api.moonshot.cn/v1",
)
 
completion = client.chat.completions.create(
    model = "moonshot-v1-8k",
    messages = [
        {"role": "system", "content": "请判断以下推文的情感是积极还是消极："},
        {"role": "system", "content": "回答格式为积极或中性或消极"},
        {"role": "user", "content":"喜欢看赛马娘的都是神人了"}
    ],
    temperature = 0,
)

positiveCount=0
negativeCount=0
neutralCount=0

if completion.choices[0].message.content=='积极':
    positiveCount=positiveCount+1
if completion.choices[0].message.content=='中性':
    neutralCount=neutralCount+1
if completion.choices[0].message.content=='消极':
    negativeCount=negativeCount+1

print(positiveCount)
print(neutralCount)
print(negativeCount)
print(completion.choices[0].message.content)
