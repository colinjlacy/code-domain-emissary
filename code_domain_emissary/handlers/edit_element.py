def edit_element(request, responder):
    responder.slots['name'] = request.context.get('name', '')
    responder.slots['element'] = request.context.get('element', '')
    responder.reply(['editing {element} element with name {name}'])
