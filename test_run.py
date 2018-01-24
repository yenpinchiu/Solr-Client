import solr_client
import random_test_case

if __name__ == "__main__":
    SC = solr_client.SolrClient()
    RTC = random_test_case.RandomTestCase(fields_scheme={"name", "field_0", "field_1", "field_2"})
    for i in range(0, 100):
        res = SC.update("Test-Collection", RTC.generate_random_case())
        print(res)
