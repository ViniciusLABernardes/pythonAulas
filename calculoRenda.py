# def dinheiro_ganho(views):
#     valor = 0
#     for 1000 in views:
#         valor += 0.70
    

#     print(valor)


def dinheiro_ganho(views):
    valor_por_view = 0.7010
    incremento = 1000
    valor_total = (views // incremento) * valor_por_view
    
    print(f"Total recebido: R${valor_total:.2f}")

# Exemplo de uso
views = int(input("Digite o número de visualizações: "))
dinheiro_ganho(views)