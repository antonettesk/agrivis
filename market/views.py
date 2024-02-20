from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from market.libs.faostatpackage.faostat import get_data_df

def home(request):
    return HttpResponse("Welcome to AgriVis!")

def home(request):
    return render(request, 'market/home.html')

# Creating views for relevant datasets forming the tracker(QCL, QV, PP, FBS, TI)

def qcl_data_view(request):
    params = {
        'area': [114, 32, 59, 20, 159, 202],
        'element': '2510',
        'item': ['15', '56', '27', '866', '486', '116'],
        'year': ['2019', '2020', '2021']
    }
    qcl_data = get_data_df('QCL', pars=params)
    return JsonResponse({'qcl_data': qcl_data.to_dict(orient='records')})

def qv_data_view(request):
    params = {
        'area': [114, 32, 59, 20, 159, 202],
        'element': ['55', '58'],
        'item': ['15', '56', '27', '866', '486', '116'],
        'year': ['2019', '2020', '2021']
    }
    qv_data = get_data_df('QV', pars=params)
    return JsonResponse({'qv_data': qv_data.to_dict(orient='records')})

def pp_data_view(request):
    params = {
        'area': [114, 32, 59, 20, 159, 202],
        'element': [5531, 5530],
        'item': [15, 56, 27, 866, 486, 116],
        'month': 7012,
        'year': [2019, 2020, 2021]
    }
    pp_data = get_data_df('PP', pars=params)
    return JsonResponse({'pp_data': pp_data.to_dict(orient='records')})

def fbs_data_view(request):
    params = {
        'area': [114, 32, 59, 20, 159, 202],
        'element': [2300, 2141, 2510, 2610, 2910],
        'item': [15, 56, 27, 866, 486, 116],
        'year': [2019, 2020, 2021]
    }
    fbs_data = get_data_df('FBS', pars=params)
    return JsonResponse({'fbs_data': fbs_data.to_dict(orient='records')})

def ti_data_view(request):
    params = {
        'area': [114, 32, 59, 20, 159, 202],
        'element': [465, 495, 464, 494],
        'item': [15, 56, 27, 866, 486, 116],
        'year': [2019, 2020, 2021]
    }
    ti_data = get_data_df('TI', pars=params)
    return JsonResponse({'ti_data': ti_data.to_dict(orient='records')})

# Add views for the models and preferences

