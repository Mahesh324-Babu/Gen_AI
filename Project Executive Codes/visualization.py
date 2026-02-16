from gemini_service import model

def create_visualizations(data):
    prompt = f"""
    Based on this financial data {data}, create matplotlib charts for:
    - Revenue trends
    - Profit margins
    - Expense breakdowns

    Return Python matplotlib code.
    """

    response = model.generate_content(prompt)
    return response.text
