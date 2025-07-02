from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    elif length == "Medium":
        return "6 to 10 lines"
    elif length == "Long":
        return "11 to 15 lines"
    return "None"

def get_prompt(length, language, topic):
    length_str = get_length_str(length)

    prompt = f'''
        Generate a linkedIn post using the below parameters, no preamble:
        1) Topic: {topic}
        2) Length: {length_str}
        3) Language: {language}
        Post should be always in english, oriented and topic focused.
        '''

    example = few_shot.get_filtered_post(length, language, topic)

    if len(example) > 0:
        prompt += "Use the writing style as per the following example:\n"
        for i, post in enumerate(example):
            post_text = post['text']
            prompt += f"\n\n Example #{i+1}: {post_text}\n"
            if i == 2:
                break
    return prompt

def generate_post(length, language, topic):
    prompt = get_prompt(length, language, topic)
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    post = generate_post("Long","English", "Job Search")
    print(post)




