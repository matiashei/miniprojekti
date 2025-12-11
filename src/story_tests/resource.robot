*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}        localhost:5001
${DELAY}         0.5 seconds
${HOME_URL}      http://${SERVER}
${RESET_URL}     http://${SERVER}/reset_db
${BROWSER}       chrome
${HEADLESS}      false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
        Call Method  ${options}  add_argument  --incognito
        Call Method  ${options}  add_argument  -disable-search-engine-choice-screen
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
        Call Method  ${options}  add_argument  --private-window
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0.05 seconds
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}
    Set Window Size  1920  1080

Go To Home Page
    Go To  ${HOME_URL}

Main Page Should Be Open
    Title Should Be  citation app

Add Citation Page Should Be Open
    Title Should Be  Create a new citation

Reset Citations And Go To Home Page
    Reset Database
    Go To Home Page

Set Book Tag
    [Arguments]    ${tags}
    Input Text    name:tags    ${tags}

Select Tag To Filter
    [Arguments]  ${tag}
    ${checkbox}=  Set Variable  css:input[type="checkbox"][value="${tag}"]
    Click Element  ${checkbox}

Select Filtering Method
    [Arguments]  ${option}
    Click Element  id:filtering_method
    Select From List By Label  match_all  ${option}