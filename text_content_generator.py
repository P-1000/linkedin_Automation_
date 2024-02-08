from openai import OpenAI

selected_model = "gpt-3.5-turbo"
image_model = "dall-e-2"

client = OpenAI(
    # api_key='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'
    api_key='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'
)
imageclient = OpenAI(
    api_key='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'
)

def openai_generate(user_prompt):
    try:
        chat_completion = client.chat.completions.create(
        messages=[
        {
            "role": "user",
            "content": user_prompt,
        }
    ],
        model=selected_model,
)

        return chat_completion.choices[0].message.content
    except Exception as e:
        # print(f"Error: {str(e)}")
        return "Error generating linkedin content."

# def image_generator(prompt):
#     try:
#         image_completion = imageclient.images.generate(
#         model="dall-e-3",
#         prompt="a white siamese cat",
#         size="1024x1024",
#         quality="standard",
#         n=1,)
#         return image_completion.data[0].url
#     except Exception as e:
#         # print(f"Error: {str(e)}")
#         return "Error generating image."