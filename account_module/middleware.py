from django.shortcuts import render,redirect
from django.urls import reverse


class AdminAccessControl:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and (not request.user.is_authenticated or not request.user.is_superuser):
            if not request.user.is_authenticated:
                return redirect(reverse('login_page'))
            return render(request, 'errors/404.html', status=404)
        return self.get_response(request)
