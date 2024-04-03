Feature: Stream data of new datacategory to Redshift

    Background:
      Given a custom url "{base_url}" and endpoint "/datacategory"

    Scenario: Lambda can send datacategory to Redshift succesfully
        Given a request json payload
                """
                {
                "data_id": 9999,
                "data_name": "test type"
                }
                """
        When the request sends PUT
        Then the response status is Ok
        And the response status is 200

  	Scenario Outline: Lambda can not send datacategory to Redshift because of invalid data
        Given a request json payload
                """
                {
                "data_id": <data_id>,
                "data_name": <data_name>
                }
                """
        When the request sends PUT
        Then the response status is <status>

        Examples:
        | data_id | data_name   | status |
        | null       | "TEST2"  | 400    |
        | 992        | null     | 400    |


    Scenario: Lambda can not send datacategory to Redshift because of empty payload
        Given a request json payload
                """
                {}
                """
        When the request sends POST
        Then the response status is 400