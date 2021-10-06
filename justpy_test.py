import justpy as jp


def input_test(request):
    wp = jp.QuasarPage(data={'text': ''})
    c1 = jp.Div(classes='q-pa-md', a=wp)
    c2 = jp.Div(classes='q-gutter-md', style='max-width: 300px', a=c1)
    c3 = jp.QInput(label='Standard', a=c2, model=[wp, 'text'])
    c4 = jp.QInput(filled=True, label='Filled', a=c2, model=[wp, 'text'])
    c5 = jp.QInput(outlined=True, label='Outlined', a=c2, model=[wp, 'text'])
    c6 = jp.QInput(standout=True, label='Standout', a=c2, model=[wp, 'text'])
    c7 = jp.QInput(standout='bg-teal text-white', label='Custom standout', a=c2, model=[wp, 'text'])
    c8 = jp.QInput(borderless=True, label='Borderless', a=c2, model=[wp, 'text'])
    c9 = jp.QInput(rounded=True, filled=True, label='Rounded filled', a=c2, model=[wp, 'text'])
    c10 = jp.QInput(rounded=True, outlined=True, label='Rounded outlined', a=c2, model=[wp, 'text'])
    c11 = jp.QInput(rounded=True, standout=True, label='Rounded standout', a=c2, model=[wp, 'text'])
    c12 = jp.QInput(square=True, filled=True, label='Square filled', hint='This is a hint', a=c2, model=[wp, 'text'])
    c13 = jp.QInput(square=True, outlined=True, label='Square outlined', a=c2, model=[wp, 'text'])
    c14 = jp.QInput(square=True, standout=True, label='Square standout', a=c2, model=[wp, 'text'])
    c15 = jp.QInput(square=True, outlined=True, a=c2, model=[wp, 'text'])
    return wp


jp.justpy(input_test)
