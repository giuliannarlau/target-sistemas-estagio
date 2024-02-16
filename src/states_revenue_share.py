def calculate_state_share_revenue(states_revenue):
    """Calcula a porcentagem de participação de faturamento de cada estado. 
    
    Percorre a lista de dicionários fornecida, calculando, adicionando a participação de faturamento
    e retornando a lista modificada.
    """

    total_revenue = sum(state["revenue"] for state in states_revenue)
    for state in states_revenue:
        state["share"] = "{:.2f}%".format((state["revenue"] / total_revenue * 100))
    return states_revenue

if __name__ == "__main__":
    states_revenue = [
        {"UF": "SP", "revenue": 67836.43},
        {"UF": "RJ", "revenue": 36678.66},
        {"UF": "MG", "revenue": 29229.88},
        {"UF": "ES", "revenue": 27165.48},
        {"UF": "Outros", "revenue": 19849.53}
    ]

    states_revenue = calculate_state_share_revenue(states_revenue)

    for state in states_revenue:
        print(f"{state['UF']}: {state['share']}")