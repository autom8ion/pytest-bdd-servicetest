@githubAPITest
Feature: GitHub API
	
	As a github user,
	I want to be able to call the Github API to Create new Repositories,
  	Get User Details, and Delete Repositories,
	So that the user doesn't have to use the github web UI

@smoke @get
Scenario: GET Call returns 200
	Given the user executes a GET User call
	Then the response status code is "200"

@smoke @get
Scenario: GET Call returns Data Correctly
	Given the user executes a GET User call
	Then the response status code is "200"
	And the user receives a response with the correct github project details

@smoke @post
Scenario: Create a new Repository in Github
	Given the user Creates a new GitHub Repository
	Then the github repository is created in the system

@smoke @delete
Scenario: Delete a Repository in Github
	Given the user Creates a new GitHub Repository to delete
	When the user Deletes the Github Repository
	Then the Github Repository no longer exists in the Github System


@get @check_errors @401
Scenario: GET User Call returns 401
    Given the user executes a GET User call without authentication
    Then the response status code is 401


@get @check_errors @404
Scenario: GET User Call returns 404
    Given the user executes a GET User call with an invalid route
    Then the response status code is 404
