# GUARD: Guideline Upholding Test through Adaptive Role-play Diagnostics for LLMs

### Repository for ICLR 2025 Submission

## Environment Setup

To set up the environment, use Conda to create a new environment with the required dependencies.

### Step 1: Create a Conda Environment
```bash
conda create -n GUARD python=3.10
conda activate GUARD
pip install torch torchvision transformers openai==0.28.0
```

### Step 2: Guideline upholding test
```bash
python upholding_test.py \
--guidelines "AI systems should prioritize safety and minimize risks of harm to users." \
--openai_key YOUR_OPENAI_API_KEY
```

### Step 3: Determine guideline-violating questions or guideline-adhering questions
```bash
python question_eval.py \
  --guidelines "AI systems should prioritize safety and minimize risks of harm to users." \
  --model_name "gpt-4o" \
  --openai_key "your_openai_key" \
  --refusal_match_file "refusal_match.json"
```

### Step 4: Jailbreak diagnostics for LLMs
```bash
python attack.py \
--model_name "gpt-4o" \
--openai_key "your_openai_key" \
--adhering_file "question_adhering.json"
```
## Welcome to join our human evaluation survey on guideline-violating questions
https://docs.google.com/forms/d/e/1FAIpQLSejSEUMY5TJGbqE1fRPdvPhlrs_bU4nMRWzCJwDU7K8cFL0hA/viewform?usp=sf_link

## Welcome to join our human evaluation survey on harmfulness score
https://docs.google.com/forms/d/e/1FAIpQLSc-ULju4oPXUcw_7cow920q-TdoCJNT0dcx8hJ3WYK3N2T_fg/viewform?usp=sf_link

## Ongoing Updates
This project is actively maintained, and the following updates are planned:

- **Support for Additional LLMs**: Extend compatibility to include models like Anthropic Claude and Gemini.
- **Expanded Guidelines**: Incorporate a more diverse set of AI safety and ethical guidelines for broader evaluation.
- **Enhanced Jailbreak Scenarios**: Develop more sophisticated jailbreak attack methods to evaluate model robustness under complex conditions.
- **Pre-built Benchmarks**: Provide ready-to-use benchmarks for evaluating model safety and compliance across different use cases.
- **User-Friendly Tools**: Improve usability by integrating visualization tools and streamlined interfaces.
