import solr_client
import random_test_case

if __name__ == "__main__":
    sc = solr_client.Solr_client()
    rtc = random_test_case.random_test_case(fields_scheme={"name", "field_0", "field_1", "field_2"})
    for i in range(0, 1000):
        res = sc.update("Test-Collection", rtc.generate_random_case())
        print(res)