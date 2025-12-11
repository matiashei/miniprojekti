*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Citations and Go To Home Page

*** Test Cases ***
Select One Tag And Filter Citations
    Create Citations
    Go To Home Page
    Select Tag to Filter  kandi
    Select Filtering Method  Match one
    Click Button  Apply filters
    Page Should Contain  Kirja1
    Page Should Contain  Kirja2

Select Multiple Tags And Filter Citations With Match One
    Create Citations
    Go To Home Page
    Select Tag to Filter  kandi
    Select Tag to Filter  ei luettu
    Select Filtering Method  Match one
    Click Button  Apply filters
    Page Should Contain  Kirja1
    Page Should Contain  Kirja2

Select Multiple Tags And Filter Citations With Match All
    Create Citations
    Go To Home Page
    Select Tag to Filter  kandi
    Select Tag to Filter  luettu
    Select Filtering Method  Match all
    Click Button  Apply filters
    Page Should Contain  Kirja1
    Page Should Not Contain  Kirja2


*** Variables ***
@{TAGS1}  kandi  maisteri  luettu
@{TAGS2}  kandi  ei luettu

*** Keywords ***
Create Citations
    Create Book Citation  Kirja1  Matti Meikalainen  Testijulkaisija  123-4567890123  2024  ${TAGS1}
    Create Book Citation  Kirja2  Matti Meikalainen2  Testijulkaisija2  123-4567890127  2020  ${TAGS2}