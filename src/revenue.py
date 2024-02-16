import json

def load_json(file_path):
    """Carrega o arquivo json."""

    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def max_daily_revenue(data):
    """Calcula o maior faturamento diário."""

    max_revenue = 0.0
    for item in data:
        if item["valor"] > max_revenue:
            max_revenue = item["valor"]
    return max_revenue

def min_daily_revenue(data):
    """Calcula o menor faturamento diário."""

    min_revenue = max_daily_revenue(data)
    for item in data:
        if item["valor"] < min_revenue and item["valor"] > 0:
            min_revenue = item["valor"]
    return min_revenue

def calculate_avg_revenue(data):
    """Calcula a média de faturamento, desconsiderando feriados e finais de semana, que possuem faturamento zerado.
    
    Nota: essa função não foi explicitamente solicitada na questão, desenvolvi para manter um padrão responsabilidade única.
    """

    total_days, total_revenue = 0, 0.0
    for item in data:
        if item["valor"] > 0:
            total_days += 1
        total_revenue += item["valor"]
    return total_revenue / total_days

def days_above_avg_revenue(data):
    """Calcula a quantidade de dias no mês na qual o faturamento diário foi superior à média mensal."""

    days_above_avg = 0
    avg_revenue = calculate_avg_revenue(data)
    for item in data:
        if item["valor"] > avg_revenue:
            days_above_avg += 1
    return days_above_avg

if __name__ == "__main__":
    data = load_json("../data/dados.json")

    print("Menor valor de faturamento ocorrido em um dia do mês: ", min_daily_revenue(data))
    print("Maior valor de faturamento ocorrido em um dia do mês: ", max_daily_revenue(data))
    print("Quantidade de dias no mês na qual o faturamento diário foi superior à média mensal: ", days_above_avg_revenue(data))

