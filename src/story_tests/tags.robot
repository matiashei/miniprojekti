*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Citations

*** Test Cases ***
Add Tags To A Citation
    Create First Book Citation
    Go To Home Page
    Click Link  Edit
    Set Book Tag  tag1 , tag2 ,tag3
    Click Button  Edit
    Page Should Contain  Tags:
    Page Should Contain  tag1,
    Page Should Contain  tag2,
    Page Should Contain  tag3

Add A Too Long Tag
    Create First Book Citation
    Go To Home Page
    Click Link  Edit
    Set Book Tag  thistagiswaytoolongtobevalid, valid
    Click Button  Edit
    Page Should Contain  Each tag must be less than 20 characters


*** Keywords ***
Reset Citations
    Reset Database

Create First Book Citation
    Create Book Citation  Testikirja  Matti Meikalainen  Testijulkaisija  123-4567890123  2024
