from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    search = request.GET.get('search', '')
    contacts = Contact.objects.filter(is_deleted=False)

    if search:
        contacts = contacts.filter(
            Q(name__icontains=search) | Q(email__icontains=search)
        )

    return render(request, 'contacts/list.html', {'contacts': contacts})


def contact_create(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, 'contacts/form.html', {'form': form})


def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, 'contacts/form.html', {'form': form})


def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.is_deleted = True
    contact.save()
    return redirect('contact_list')

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk, is_deleted=False)
    return render(request, 'contacts/detail.html', {'contact': contact})
