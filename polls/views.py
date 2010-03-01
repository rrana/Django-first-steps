from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from eVirtuve.polls.models import Poll, Choice
from django.http import HttpResponseRedirect, HttpResponse

# def index(request):
#     latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#     return render_to_response('polls/poll_list.html', {'latest_poll_list': latest_poll_list})
#     
# def detail(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     return render_to_response('polls/poll_detail.html', {'poll': p})
#     
# def results(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     return render_to_response('polls/results.html', {'poll': p})
    
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('polls/poll_detail.html',  {
            'object': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
    
def http404(request):
    return render_to_response('polls/404.html')