from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import FriendShip
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from .forms import searchForm
from accounts.models import Profile
from django.contrib import messages


# Create your views here.
@login_required
def search(request):
    context=dict()
    context["friend"]=None

    if request.method == "POST":
        form=searchForm(request.POST)
        if(form.is_valid()):
            nickname=form.cleaned_data['nickname']
            phone_number=form.cleaned_data['phone_number']
            querySet=Profile.objects.all()

            if nickname != '':
                querySet = querySet.filter(nickname=nickname)
            if phone_number != '':
                querySet = querySet.filter(phone_number=phone_number)

            if(querySet[0].user == request.user):
                messages.add_message(request, messages.ERROR, '친구목록에 "나"는 포함될 수 없습니다. 친구를 다시 검색해주세요.')
                return render(request, "friend/friend_search.html",{
                                  'form':searchForm(),
                                  'friend':None
                              })

            context["friend"]=querySet[0]

    else:
        form=searchForm()

    context["form"]=form
    return render(request, "friend/friend_search.html", context)


@login_required
def myList(request):
    U=get_object_or_404(get_user_model(), username=request.user.username)
    List=[friendship.to_friend for friendship in U.friend_set.all()]

    context=dict()
    context["List"]=List
    return render(request, "friend/friend_list.html", context)


@login_required
def add(request):
    try:
        U1=request.user
        ref = get_object_or_404(Profile, nickname=request.POST["choice"])
        U2=ref.user
    except(Exception):
        return render(request, "friend/friend_search.html", {
            "comment" : "친구 ID를 입력해주세요."
        })
    else:
        try:
            FriendShip.objects.create(from_friend=U1, to_friend=U2)
            FriendShip.objects.create(from_friend=U2, to_friend=U1)
            return HttpResponseRedirect(reverse_lazy('friend:search'))
        except(IntegrityError):
            return render(request, "friend/friend_search.html",
                          {
                "error_msg" : "당신은 이미 이 사람과 친구입니다.",
                "form" : searchForm()
            })

