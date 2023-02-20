from django.shortcuts import get_object_or_404, render
from .models import Cryptid
from django.template import loader


# Here is the two views linked to the pages we can find in the app: index, for the index, and detail, seen when
# clicking on the cryptid we want to learn more about


def index(request):
    cryptids_list = Cryptid.objects.order_by('cryptid_name')
    template = loader.get_template('cryptids/index.html')
    context = {
        'cryptids_list': cryptids_list
    }
    return render(request, 'cryptids/index.html', context)


def detail(request, cryptid_id):

    cryptid = get_object_or_404(Cryptid, pk=cryptid_id)
    return render(request, 'cryptids/detail.html', {'cryptid': cryptid})

