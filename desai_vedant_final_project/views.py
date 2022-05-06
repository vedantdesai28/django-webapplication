from django.shortcuts import redirect


def redirect_root_view(request):
    return redirect('bookinginfo_service_list_urlpattern')

