from ast import Add
from codecs import utf_8_encode
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponseRedirect
import requests
import urllib
import json

import search_for_candidates
from .models import Candidate
from .add_candidate import AddCandidate


def add_candidate(request, candidate_username):
    print(request.method)
    # get user data from github api
    response = requests.get(
        f'https://api.github.com/users/{candidate_username}')
    response_dict = json.loads(response.text)
    print(response_dict)

    # get user data from stack overflow api

    c = Candidate(
        candidate_username=response_dict['login'],
        candidate_name=response_dict['name'],
        candidate_url=response_dict['html_url'],
        candidate_avatar_url=response_dict['avatar_url'],
        candidate_company=response_dict['company'],
        candidate_blog_url=response_dict['blog'],
        candidate_location=response_dict['location'],
        candidate_email=response_dict['email'],
        candidate_bio=response_dict['bio'],
        candidate_repo_number=response_dict['public_repos'],
        candidate_gists_number=response_dict['public_gists'],
        candidate_follower_number=response_dict['followers'],
        candidate_following_number=response_dict['following'],
        candidate_join_date=response_dict['created_at']
    )

    check = (response_dict['name']) is None

    if not check:
        print("hello")
        query = "https://api.stackexchange.com/2.3/users?order=desc&sort=reputation&inname=" + urllib.parse.quote_plus(
                str(response_dict['name'])) + "&site=stackoverflow&filter=!azbR7sdYTRiPLf"
        stackoverflow_responses = requests.get(query)
        stackoverflow_response_dict = json.loads(
            stackoverflow_responses.text)['items']

        if len(stackoverflow_response_dict):

            stackoverflow_response_dict = stackoverflow_response_dict[0]
            c.stackoverflow_candidate_name = stackoverflow_response_dict['display_name']
            c.stackoverflow_candidate_url = stackoverflow_response_dict['link']
            c.stackoverflow_candidate_avatar_url = stackoverflow_response_dict['profile_image']
            c.stackoverflow_candidate_blog_url = stackoverflow_response_dict['website_url']
            c.stackoverflow_candidate_location = stackoverflow_response_dict.get(
                'location')
            c.stackoverflow_candidate_bio = stackoverflow_response_dict['about_me']
            c.stackoverflow_candidate_view_count = stackoverflow_response_dict['view_count']
            c.stackoverflow_candidate_up_vote_count = stackoverflow_response_dict[
                'up_vote_count']
            c.stackoverflow_candidate_answer_count = stackoverflow_response_dict['answer_count']
            c.stackoverflow_candidate_question_count = stackoverflow_response_dict[
                'question_count']
            c.stackoverflow_candidate_reputation = stackoverflow_response_dict['reputation']

    c.save()

    return redirect('search_for_candidates:search')


def delete_candidate(request, candidate_id):
    candidate = Candidate.objects.get(pk=candidate_id)
    candidate.delete()
    return redirect('search_for_candidates:all_candidates')


def update_candidate_notes(request, candidate_id):
    candidate = Candidate.objects.get(pk=candidate_id)
    form_data = request.POST
    candidate.candidate_notes = form_data['notes']
    candidate.save()
    return HttpResponseRedirect(reverse('search_for_candidates:detail', args=(candidate_id,)))
    # render(request, "{% url 'search_for_candidates:detail' candidate_id %}")


def search(request):
    print('The request method is:', request.method)

    if request.method == "POST" and len((request.POST)['q']):
        data = request.POST
        type = f" type:{data['type']}" if len(data['type']) else ""
        org = f" org:{data['org:name']}" if len(data['org:name']) else ""
        repos = f" repos:{data['repose']}" if len(data['repose']) else ""
        location = f" location:{data['location']}" if len(
            data['location']) else ""
        followers = f" followers:{data['followers']}" if len(
            data['followers']) else ""
        language = f" language:{data['language']}" if len(
            data['language']) else ""
        created = f" created:{data['created']}" if len(data['created']) else ""

        query_string = f"{data['q']}{type}{repos}{location}{followers}{language}{created}{org}"
        query = "per_page=100&q=" + urllib.parse.quote_plus(query_string)

        print(query)
        responses = requests.get(
            f'https://api.github.com/search/users?{query}')
        response_dict = json.loads(responses.text)['items']
        return render(request, "search_for_candidates/search.html", {"response_dict": response_dict})
    else:
        return render(request, "search_for_candidates/search.html")


def all_candidates(request):
    """"" name = urllib.parse.urlencode({'q': "backend", 'type': "User", 'location': "paris"})
    print(name)
    name = "q=" + \
        urllib.parse.quote("backend type:User location:paris language:java")
    responses = requests.get(f'https://api.github.com/search/users?{name}')
    """""
    candidates_list = Candidate.objects.all()
    context = {"candidates_list": candidates_list}
    return render(request, "search_for_candidates/all_candidates.html", context)


def detail(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    context = {'candidate': candidate, }
    return render(request, "search_for_candidates/detail.html", context)


# Create your views here.
