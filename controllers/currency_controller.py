
def convert_from_to(frm, to, amount, currencies):
    # verifica se a moeoda de origem existe
    from_value = [x for x in currencies if x.code == frm].pop()
    if not from_value:
        return 'source currency does not exist'

    # verifica se a moeoda de destino existe
    to_value = [x for x in currencies if x.code == to].pop()
    if not to_value:
        return 'destination currency does not exist'

    # monta resposta com o quantidade ,moeda de origem ,moeda de destino e valor
    return {'amount': amount,
            'from': from_value.name,
            'destination currency': to_value.name,
            'destination value': format(((amount / float(from_value.value_in_dollar)) *
                                         float(to_value.value_in_dollar)), '.2f')}
