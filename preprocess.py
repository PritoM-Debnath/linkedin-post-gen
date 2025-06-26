import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm

def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    detailed_posts = []
    with open(raw_file_path, encoding="utf-8") as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post['text'])
            meta_post = metadata | post
            detailed_posts.append(meta_post)

    unified_tags = get_unified_tags(detailed_posts)

    for post in detailed_posts:
        current_tags = post['tags']
        new_tags = {unified_tags[tag] for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(processed_file_path, mode="w", encoding="utf-8") as outfile:
        json.dump(detailed_posts, outfile, indent=4)

#similar tags are generalized
def get_unified_tags(post_metadata):
    unique_tags = set()
    for post in post_metadata:
        unique_tags.update(post['tags'])

    unique_tag_list = ', '.join(unique_tags)

    template = '''I will give you a list of tags. You need to unify tags with the following requirements,
    1. Tags are unified and merged to create a shorter list.
    Example 1: "Jobseekers","job hunting" can be all merged into a single tag "Job search".
    Example 2: "Motivation", "Inspiration", "Drive " can be mapped to "Motivation"
    Example 3: "Personal Growth", "Personal Development", "Self improvement" can be mapped to "Self Improvement".
    Example 4: "Scam Alert", "Job Scam" etc can be mapped to "Scam"
    2. Each tag should follow title case convention. Example: "Motivation", "Job Search".
    3. Output should be a JSON object, No preamble.
    4. Output should have mapping of original tag and the unified tag.
    For example:{{"Jobseekers":"Job Search", "Job Hunt":"Job Search"}}
    
    Here is the list of tags: 
    {tags}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'tags': str(unique_tag_list) })

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Content too big. Unable to parse")
    return res

# Add metadata
def extract_metadata(post):

    template = '''
    You are given a Linkedin post. You need to extract number of lines, language of the post and tags.
    1. Return a valid JSON. No preamble.
    2.JSON object should have exactly three keys: line_count, language, tags.
    3. tags is an array of text tags. Extract maximum two tags.
    4. Language should be English or Bangla.
    Here is the actual post on which you need to perform these task:
    {t_post}
    '''

    pt=PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'t_post': post})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Content too big. Unable to parse")
    return res


if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")