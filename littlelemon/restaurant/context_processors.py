from datetime import datetime

def date_context(request):
    '''provide the current year to all templates'''
    return {
        'current_year': datetime.now().year
    }