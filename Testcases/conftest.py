import allure
import pytest
from selenium import webdriver
from Utilities import ConfigReader
from allure_commons.types import AttachmentType
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request, get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="login_selectors", attachment_type=AttachmentType.PNG)


@pytest.fixture(scope="class", autouse=True)
def get_browser(request):
    # driver = webdriver.Chrome(GeckoDriverManager().install())
    driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.get(ConfigReader.readConfig("paths", "url"))
    # driver.get(config('url'))
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()

# @pytest.fixture(scope="class", autouse=True)
# def teardown(request):
#     driver = webdriver.Firefox()
#     request.cls.driver = driver
#     driver.quit()
