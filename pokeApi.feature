Feature: Automation test beahavior

    Scenario: Happy path result
        Given I want open results
        When I GET the URI
        Then I check that http response has status code 200

    Scenario Outline: ability
        Given I have this URI
            """
            https://pokeapi.co/api/v2/ability/7/
            """
            #  When I GET the URI with or without next param:
            | <name> | <value> |
        Then I check that http response has status code 200
        Examples:
            | name     | value |
            | agil     | 7     |
            | impostor | 150   |