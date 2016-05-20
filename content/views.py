from django.shortcuts import render, render_to_response

# Create your views here.


def main_page(request):

    output = {
        'user': request.user
    }
    print(output['user'].is_authenticated())
    print(output['user'].username)
    return render_to_response('main.html', output)

