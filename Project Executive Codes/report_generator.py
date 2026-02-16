from gemini_service import model

def generate_report(file_content):
    prompt = f"""
    You are a financial data analyst. Analyze this financial dataset:

    {file_content}

    Please provide:
    1. Executive Summary
    2. Revenue Trends
    3. Profitability Analysis
    4. Cost Structure Breakdown
    5. Risk Factors
    6. Recommendations
    """

    response = model.generate_content(prompt)
    return response.text
