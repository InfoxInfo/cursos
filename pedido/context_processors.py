def cart_item_count(request):
    carrinho = request.session.get('carrinho', {})
    total_itens = len(carrinho)
    return {'total_itens': total_itens}