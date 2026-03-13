from django.shortcuts import render

def bmi_calculator(request):
    bmi = None
    category = None

    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height_cm = float(request.POST.get('height'))
        height = height_cm / 100

        bmi = round(weight / (height ** 2), 2)

        if bmi < 20:
            category = 'Underweight'
        elif bmi < 25:
            category = 'Normal'
        else:
            category = 'Overweight'

    return render(request, 'bmi_app/bmi_form.html', {
        'bmi': bmi,
        'category': category,
    })
