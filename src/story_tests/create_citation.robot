*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations And Go To Create Citation Page

*** Test Cases ***
Add Book Citation With Valid Inputs
    Select Citation Option From Dropwdown  Book
    Set Book Citation Fields  Testikirja  Matti Meikalainen  Testijulkaisija  123-4567890123  2020
    Click Button  Create
    Add Citation Should Succeed

Add Book Citation With Invalid Year
    Select Citation Option From Dropwdown  Book
    Set Book Citation Fields  Testikirja  Matti Meikalainen  Testijulkaisija  123-4567890123  9999
    Click Button  Create
    Form Submmission Should Fail

Add Book Sitation With Missing Title
    Select Citation Option From Dropwdown  Book
    Set Book Citation Fields  ${EMPTY}  Matti Meikalainen  Testijulkaisija  123-4567890123  2020
    Click Button  Create
    Add Citation Should Fail With Message  Title cannot be empty and the lenght must be less than 75 characters

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
    Input Text  isbn  ${ISBN}
    Input Text  year  ${year}

Select Citation Option From Dropwdown
    [Arguments]  ${option}
    Click Element  choice
    Select From List By Label  citation_type  ${option}

Reset Citations And Go To Create Citation Page
    Reset Database
    Go To Home Page
    Click Link  Create new citation
    Add Citation Page Should Be Open