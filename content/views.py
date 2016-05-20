from django.shortcuts import render, render_to_response, redirect
from content.models import Message, Group, UserGroupAssignment
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def main_page(request):

    output = {
        'user': request.user,
        'messages': Message.objects.all(),
        'groups': UserGroupAssignment.objects.filter(userId__user=request.user)
    }

    print(output['groups'])
    print(output['user'].is_authenticated())
    print(output['user'].username)
    return render_to_response('main.html', output)

@csrf_exempt
def add_message(request):

    group_assignment_id = request.POST.get('group')
    group_assignment = UserGroupAssignment.objects.filter(id=group_assignment_id)
    content = request.POST.get('content')
    print(group_assignment)
    print(content)
    message = Message(content=content, membershipId_id=group_assignment_id)
    message.save()
    return redirect("/main")


