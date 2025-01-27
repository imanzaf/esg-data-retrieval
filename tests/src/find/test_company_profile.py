from src.find.company_profile import CompanyProfile


class TestIsValidISIN:

    def test_with_valid_isin(self):
        ISIN = "GB00BNC5T391"
        result = CompanyProfile.is_valid_isin(ISIN)
        assert result is True

    def test_with_invalid_isin(self):
        ISIN = "apple"
        result = CompanyProfile.is_valid_isin(ISIN)
        assert result is False
