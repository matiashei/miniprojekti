*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations And Go To Create Citation Page

*** Test Cases ***
Add Book Citation With Valid Inputs
    Set Book Citation Fields  Testikirja  Matti Meikalainen  Testijulkaisija  123-4567890123  2020
    Click Button  Create
    Add Citation Should Succeed

Add Book Citation With Invalid Year
    Set Book Citation Fields  Testikirja  Matti Meikalainen  Testijulkaisija  123-4567890123  9999
    Click Button  Create
    Form Submmission Should Fail

Add Book Sitation With Missing Title
    Set Book Citation Fields  ${EMPTY}  Matti Meikalainen  Testijulkaisija  123-4567890123  2020
    Click Button  Create
    Add Citation Should Fail With Message  Title length must be less than 75 characters

*** Keywords ***
Add Citation Should Succeed
    Main Page Should Be Open

Form Submmission Should Fail
    Add Citation Page Should Be Open

Add Citation Should Fail With Message
    [Arguments]  ${message}
    Add Citation Page Should Be Open
    Page Should Contain  ${message}

Set Book Citation Fields
    [Arguments]  ${title}  ${author}  ${publisher}  ${ISBN}  ${year}
    Input Text  title  ${title}
    Input Text  author  ${author}
    Input Text  publisher  ${publisher}
    Input Text  ISBN  ${ISBN}
    Input Text  year  ${year}

Reset Citations And Go To Create Citation Page
    Reset Database
    Go To Home Page
    Click Link  Create new citation
    Add Citation Page Should Be Open