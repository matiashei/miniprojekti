*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations

*** Test Cases ***
At start there are no todos
    Go To  ${HOME_URL}
    Title Should Be  citation app
    Page Should Contain  Create new citation

After adding a todo, there is one
    Go To  ${HOME_URL}
    Click Link  Create new citation
    Input Text  citation  Testi
    Click Button  Create
    Page Should Contain  citation app
    Page Should Contain  Testi
