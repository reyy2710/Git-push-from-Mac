from django.shortcuts import render

def student_form(request):
    data = ""
    percentage = None

    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        eng = int(request.POST.get('english'))
        phy = int(request.POST.get('physics'))
        chem = int(request.POST.get('chemistry'))

        total = eng + phy + chem
        percentage = round((total / 300) * 100, 2)

        data = f"Name: {name}\nDOB: {dob}\nAddress: {address}\nContact: {contact}\nEmail: {email}\nEnglish: {eng}, Physics: {phy}, Chemistry: {chem}\nTotal: {total}"

    return render(request, 'student_form.html', {'data': data, 'percentage': percentage})
