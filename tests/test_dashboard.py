import pytest

from pages.dashboard_page import DashBoardPage


@pytest.mark.regression
@pytest.mark.dashboard
def test_dashboard_displaying(dashboard_page_with_state: DashBoardPage):
    dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    dashboard_page_with_state.sidebar.check_visible()

    dashboard_page_with_state.navbar.check_visible("username")

    dashboard_page_with_state.dashboard_title.check_visible()
    dashboard_page_with_state.students_chart_view.check_visible("Students")
    dashboard_page_with_state.activities_chart.check_visible("Activities")
    dashboard_page_with_state.scores_chart_view.check_visible("Scores")
    dashboard_page_with_state.courses_chart_view.check_visible("Courses")

