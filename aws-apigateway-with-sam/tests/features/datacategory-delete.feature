Feature: Delete datacategory data of Redshift

    Background:
        Given a custom url "{base_url}" and endpoint "/datacategory?data_id=9999"

    Scenario: Lambda can delete datacategory to Redshift succesfully
        When the request sends DELETE
        Then the response status is No Content
        And the response status is 204