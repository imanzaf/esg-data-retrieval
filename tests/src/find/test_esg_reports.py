from datetime import datetime
from src.find.esg_reports import ESGReports, SearchResult


class TestScoreSearch:

    def test_score_search_zero(self):
        search = SearchResult(
            company_name="apple",
            url="amazon.com",
            title="macbook pro",
            description="product details",
        )
        score = search.score_search()
        assert score == 0

    def test_score_search_nonzero(self):
        current_year = str(datetime.now().year)
        search = SearchResult(
            company_name="Nvidia",
            url="www.nvidia.com",
            title=f"Nvidia ESG Report {current_year}",
            description="latest esg figures",
        )
        score = search.score_search()
        assert score == 5


class TestSortResults:

    def test_sort_results(self):
        current_year = str(datetime.now().year)
        company_name = "Apple"
        search_results = [
            {"title": "Amazon Report", "link": "www.amazon.com", "snippet": "report"},
            {
                "title": f"Apple Sustainability Report {current_year}",
                "link": "www.apple.com",
                "snippet": "ESG figures",
            },
            {
                "title": "2023 ESG report",
                "link": "www.apple-store.com",
                "snippet": "Sustainability report for Apple",
            },
        ]
        sorted_results = ESGReports._sort_search_reults(
            company_name=company_name, search_results=search_results
        )
        assert sorted_results[0] == search_results[1]
        assert sorted_results[1] == search_results[2]
        assert sorted_results[2] == search_results[0]
