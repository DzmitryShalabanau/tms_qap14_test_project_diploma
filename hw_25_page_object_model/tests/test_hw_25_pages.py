import allure

from pages import AlertsPage, DownloadPage, IframePage, MainPage, UploadPage


@allure.suite('Alerts')
@allure.title('Work with alerts')
@allure.feature('Alerts')
@allure.story('Check how alerts work')
@allure.severity('blocker')
def test_alerts(driver):
    alerts = AlertsPage(driver)
    alerts.open()
    alerts.click_on_js_prompt_button()
    alerts.prompt_alert()
    alerts.assert_prompt_alert()


@allure.suite('Iframes')
@allure.title('Work with frames')
@allure.feature('Iframes')
@allure.story('Check how iframes work')
@allure.severity('critical')
def test_iframe(driver):
    iframe = IframePage(driver)
    iframe.open()
    iframe.switch_to_iframe()
    iframe.text_fill()
    iframe.assert_iframe()


@allure.suite('Main Page')
@allure.title('Work with windows')
@allure.feature('New window in browser')
@allure.story('Check how new window open works')
@allure.severity('normal')
def test_new_window(driver):
    main = MainPage(driver)
    main.open()
    main.open_new_window()
    main.open()
    main.assert_new_window()


@allure.suite('Uploads')
@allure.title('Work with uploads')
@allure.feature('Upload file')
@allure.story('Check how upload file works')
@allure.severity('minor')
def test_upload_file(driver):
    upload = UploadPage(driver)
    upload.open()
    upload.add_sample_file()
    upload.assert_upload()


@allure.suite('Downloads')
@allure.title('Work with downloads')
@allure.feature('Download file')
@allure.story('Check how download file works')
@allure.severity('trivial')
def test_download_file(driver):
    download = DownloadPage(driver)
    download.download_file()
    download.assert_if_file_exists()
