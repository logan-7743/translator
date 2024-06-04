import requests

def get_translation(prompt, languge):
    full_promt = f"""Hello, you are part of a translator app. if there is any issue at all
    , such as empty text or anything else, just out put "NA". I need you to transalte 
    given text to {languge}, please ONLY return the transaltion. Again, send nothing 
    back but the transltion The following is to be transalted: {prompt}"""

    
    base_url = "https://api.openai.com/v1/"
    model_name = "gpt-4o"
    endpoint = f"{base_url}chat/completions"
    api_key = "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"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "messages": [
            {"role": "user", "content": full_promt}
        ],
        "model": model_name
    }
    
    response = requests.post(endpoint, headers=headers, json=data).json()
    print("here",response["choices"][0]["message"]["content"])

    return
