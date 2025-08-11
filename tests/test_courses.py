from playwright.sync_api import expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_text).to_be_visible()

    view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(view_icon).to_be_visible()

    no_results_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_text).to_be_visible()

    results_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_text).to_be_visible()