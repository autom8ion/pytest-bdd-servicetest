"""
This module contains step definitions for githubservice.feature.
It uses the requests package:
http://docs.python-requests.org/
"""
from approvaltests import Options
from approvaltests.reporters.report_with_beyond_compare import report_with_beyond_compare

from tests.Data.payloadbuilder import Builder
from tests.helpers import request_helpers
import json
from conftest import USER, USER_REPOS, OWNER, REPOS, HEADER, AUTH
import pytest_check as check
from approvaltests.approvals import verify, verify_all
from pytest_bdd import scenarios, given, when, then, parsers

# Scenarios

scenarios('../features/githubservice.feature')


# Given Steps

@given('the user executes a GET User call', target_fixture="gh_given_response")
def gh_given_response(urls):
    response = request_helpers.get(urls['githubBaseURL'] + USER, headers=HEADER, auth=AUTH)
    return response


@given('the user Creates a new GitHub Repository', target_fixture="gh_post_response")
def gh_post_response(urls):
    payload = Builder.build_payload()
    print(payload)
    response = request_helpers.post(urls['githubBaseURL'] + USER_REPOS, headers=HEADER, auth=AUTH, data=payload)
    return response


@given('the user Creates a new GitHub Repository to delete', target_fixture="gh_delete_response")
def gh_delete_response(urls):
    payload = Builder.build_payload()
    print(payload)
    response = request_helpers.post(urls['githubBaseURL'] + USER_REPOS, headers=HEADER, auth=AUTH, data=payload)
    return response


@given('the user executes a GET User call without authentication', target_fixture="given_response_401")
def given_response_401(urls):
    auth = ('Authorization', '')
    response = request_helpers.get(urls['githubBaseURL'] + USER, headers=HEADER, auth=auth)
    return response


@given('the user executes a GET User call with an invalid route', target_fixture="given_response_404")
def given_response_404(urls):
    response = request_helpers.get(urls['githubBaseURL'] + USER + '/invalidroute', headers=HEADER, auth=AUTH)
    return response


# When Steps

@when('the user Deletes the Github Repository')
def gh_when_response():
    print('when')


# Then Steps

@then('the user receives a response with the correct github project details')
def test_gh_response_content(gh_given_response):
    # remove dynamic items from the json so that the verification will pass
    data = gh_given_response.json()
    data.pop('public_repos')
    data.pop('disk_usage')
    data.pop('updated_at')
    jsonResult = json.dumps(data, indent=4)
    print(jsonResult)
    verify(jsonResult)


@then(parsers.parse('the response status code is "{code:d}"'))
def test_gh_response_code(gh_given_response, code):
    check.equal(gh_given_response.status_code, code)


@then('the github repository is created in the system')
def test_repository_content(gh_post_response):
    print(gh_post_response.json())
    check.equal(gh_post_response.status_code, 201)


@then('the Github Repository no longer exists in the Github System')
def test_gh_delete(urls, gh_delete_response):
    # retrieve the Github repository name
    repo_object = gh_delete_response.json()
    check.equal(gh_delete_response.status_code, 201)
    repo = repo_object['name']

    # delete the github repo
    response = request_helpers.delete(urls['githubBaseURL'] + REPOS + OWNER + '/' + repo, headers=HEADER, auth=AUTH)
    check.equal(response.status_code, 204)

    # try to retrieve the deleted repo.  Expected to receive a 404 Error
    not_found_response = request_helpers.get(urls['githubBaseURL'] + REPOS + OWNER + '/' + repo, headers=HEADER,
                                             auth=AUTH)
    check.equal(not_found_response.status_code, 404)


@then('the response status code is 401')
def test_response_code_401(given_response_401):
    check.equal(given_response_401.status_code, 401)


@then('the response status code is 404')
def test_response_code_404(given_response_404):
    check.equal(given_response_404.status_code, 404)
