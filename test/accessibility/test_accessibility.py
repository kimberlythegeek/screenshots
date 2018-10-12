import pytest
from pytest_axe.parameterize_tests import *  # NOQA


class TestHomePageAccessibility(object):
    params = {
        # Used by pytest-axe to generate tests and configure xfails
        "color-contrast": "Reason: GitHub issue #5014 https://github.com/mozilla-services/screenshots/issues/5014",
        "html-has-lang": "Reason: GitHub issue #5015 https://github.com/mozilla-services/screenshots/issues/5015",
        "landmark-one-main": "Reason: GitHub issue #5016 https://github.com/mozilla-services/screenshots/issues/5016",
        "link-name": "Reason: GitHub issue #5017 https://github.com/mozilla-services/screenshots/issues/5017",
        "meta-viewport": "Reason: GitHub issue #5018 https://github.com/mozilla-services/screenshots/issues/5018",
        "region": "Reason: GitHub issue #5016 https://github.com/mozilla-services/screenshots/issues/5016",
    }

    @pytest.mark.accessibility
    def test_home_page_accessibility(self, rule, home_page):
        """Run accessibility audits on the home page of Screenshots."""
        results = home_page.run_single_rule(rule)
        assert len(results) == 0, home_page.report(results)


# TODO: Configure test account setup to enable tests for My Shots page, and
# the single screenshot view.


class TestOnboardingFrameAccessibility(object):
    params = {}

    @pytest.mark.accessibility
    def test_onboarding_frame_accessibility(self, rule, onboarding_frame):
        """Run accessibility audits on the onboarding frame of Screenshots."""
        results = onboarding_frame.run_single_rule(rule)
        assert len(results) == 0, onboarding_frame.report(results)


class TestPreSelectionFrameAccessibility(object):
    params = {}

    @pytest.mark.accessibility
    def test_selection_frame_accessibility(self, rule, preselection_frame):
        """Run accessibility audits on the preselection frame of Screenshots."""
        results = preselection_frame.run_single_rule(rule)
        assert len(results) == 0, preselection_frame.report(results)


class TestSelectionFrameAccessibility(object):
    params = {}

    @pytest.mark.accessibility
    def test_selection_frame_accessibility(self, rule, selection_frame):
        """Run accessibility audits on the selection frame of Screenshots."""
        results = selection_frame.run_single_rule(rule)
        assert len(results) == 0, selection_frame.report(results)


class TestScreenshotPageAccessibility(object):
    params = {}

    @pytest.mark.accessibility
    def test_screenshot_page_accessibility(self, rule, screenshot_page):
        """Run accessibility audits on the selection frame of Screenshots."""
        results = screenshot_page.run_single_rule(rule)
        assert len(results) == 0, screenshot_page.report(results)
