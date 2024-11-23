import json
import openai
import argparse
from Upholding_test import Upholding_Test


def evaluate_response(guidelines, model_name, openai_key, refusal_match_file):

    with open(refusal_match_file, "r") as json_file:
        data = json.load(json_file)
    refusal_match = data["refusal_match"]
    openai.api_key = openai_key
    guideline_question = Upholding_Test(guidelines, model_name)

    response = openai.ChatCompletion.create(
        model=model_name,
        messages=guideline_question
    )
    response_eval = response['choices'][0]['message']['content'].strip()

    is_adhering = any(refusal in response_eval for refusal in refusal_match)
    result = {
        "guideline": guidelines,
        "model": model_name,
        "question": guideline_question,
        "response": response_eval
    }

    if is_adhering:
        file_path = "question_adhering.json"
    else:
        file_path = "question_violating.json"

    try:
        # Append the result if the file already exists
        with open(file_path, "r") as file:
            existing_data = json.load(file)
        existing_data.append(result)
    except FileNotFoundError:
        existing_data = [result]
    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=4)

    return file_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Generate and evaluate guideline-violating questions based on AI safety guidelines.")
    parser.add_argument("--guidelines", type=str, required=True,
                        help="AI systems should prioritize safety and minimize risks of harm to users.")
    parser.add_argument("--model_name", type=str, default="gpt-4o",
                        help="OpenAI model name to use (default: gpt-4o).")
    parser.add_argument("--openai_key", type=str, required=True,
                        help="OpenAI API key.")
    parser.add_argument("--refusal_match_file", type=str, default="refusal_match.json",
                        help="Path to the refusal_match JSON file.")
    args = parser.parse_args()

    result_file = evaluate_response(args.guidelines, args.model_name, args.openai_key, args.refusal_match_file)
