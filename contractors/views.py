from django.shortcuts import render, get_object_or_404, redirect
from .models import Contractor
from .forms import ContractorForm

def contractor_list(request):
    contractors = Contractor.objects.all()
    return render(request, 'contractors/contractor_list.html', {'contractors': contractors})

def contractor_detail(request, pk):
    contractor = get_object_or_404(Contractor, pk=pk)
    return render(request, 'contractors/contractor_detail.html', {'contractor': contractor})

def contractor_create(request):
    if request.method == 'POST':
        form = ContractorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contractor_list')
    else:
        form = ContractorForm()
    return render(request, 'contractors/contractor_form.html', {'form': form})

def contractor_update(request, pk):
    contractor = get_object_or_404(Contractor, pk=pk)
    if request.method == 'POST':
        form = ContractorForm(request.POST, instance=contractor)
        if form.is_valid():
            form.save()
            return redirect('contractor_list')
    else:
        form = ContractorForm(instance=contractor)
    return render(request, 'contractors/contractor_form.html', {'form': form})

def contractor_delete(request, pk):
    contractor = get_object_or_404(Contractor, pk=pk)
    if request.method == 'POST':
        contractor.delete()
        return redirect('contractor_list')
    return render(request, 'contractors/contractor_confirm_delete.html', {'contractor': contractor})
