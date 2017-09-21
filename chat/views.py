from django.shortcuts import render, resolve_url
from django.contrib.auth.decorators import login_required
from .models import Room
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages


@login_required
def create(request):
    try:
        username_list=request.POST.getlist("chk_info[]")
        participants=[request.user, ]

        for name in username_list:
            participants.append(get_user_model().objects.get(username=name))

    except(KeyError):
        #       client의 비정상적 접근. 즉, friend_list 화면에서 친구를 선택하고
        #       채팅방 만들기로 접근해야한다. 하지만 friend_list를 거치지 않고 곧장
        #       chat:new_room 으로 접근한 경우이다.
        messages.add_message(request, messages.ERROR, '비정상적 접근입니다. \n' +
                        '친구 목록화면에서 친구를 선택하고 채팅방을 만들어야 합니다.\n' +
                        '친구 목록화면으로 이동합니다.')
        return HttpResponseRedirect(resolve_url('friend:list'))

    else:
        S=set(participants)
        candidate_rooms=Room.objects.annotate(c=Count('users')).filter(c=len(S))
        default=[]

        for USER in S:
            candidate_rooms=candidate_rooms.filter(users=USER)
            default.append(USER.profile.nickname)


        if(candidate_rooms):
            print("이미 방이 존재하고 있습니다. 채팅방으로 연결해드립니다.")
            #   redirection 시키는 코드 넣을 것.
            return HttpResponseRedirect(reverse('chat:enter'))


        #       여기서 새로운 방을 만드는 로직 작성.
        title=""
        if(request.POST['roomTitle'] == ''):
            default.sort()
            title="-".join(default)
        else:
            title=request.POST['roomTitle']

        instance = Room.objects.create(title=title)

        for USER in S:
            instance.users.add(USER)


        #       채팅방으로 입장하게끔 redirection 시켜준다.
        return HttpResponseRedirect(reverse('chat:enter'))



@login_required
def showroomList(request):
    context=dict()
    List=Room.objects.filter(users=request.user)
    context["List"]=List
    return render(request, "chat/room_list.html", context)



@login_required
def enter(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.filter(users=request.user)

    # Render that in the index template
    return render(request, "chat/index.html", {
        "rooms": rooms,
    })

