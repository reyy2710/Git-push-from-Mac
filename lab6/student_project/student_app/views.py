from django.shortcuts import render, redirect
from .forms import StudentForm

# View for the first page (form submission)
def first_page(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # Store form data in session
            request.session['name'] = form.cleaned_data['name']
            request.session['roll'] = form.cleaned_data['roll']
            request.session['subject'] = form.cleaned_data['subject']
            request.session['mobile_number']=form.cleaned_data['mobile_number']
            return redirect('second_page')  # Redirect to second page
    else:
        form = StudentForm()

    return render(request, 'firstPage.html', {'form': form})

# View for the second page (display stored data)
def second_page(request):
    name = request.session.get('name', 'Unknown')
    roll = request.session.get('roll', 'Unknown')
    subject = request.session.get('subject', 'Unknown')
    mobile_number=request.session.get('mobile_number','Unknown')

    return render(request, 'secondPage.html', {'name': name, 'roll': roll, 'subject': subject,'mobile_number':mobile_number})
