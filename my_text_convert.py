import requests

def converter(file="myrecording.wav"):
    api_key = "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"
    API_URL = "https://api-inference.huggingface.co/models/facebook/wav2vec2-large-xlsr-53"
    headers = {"Authorization": f"Bearer {api_key}"}

    def query(filename):
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()

    result = query(file)
    print(result)
    # print(result["text"])
    # return result["text"]

# Example usage:
converter(file="myrecording.wav")
