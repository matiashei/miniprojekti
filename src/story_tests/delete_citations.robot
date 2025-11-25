*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Citations

*** Test Cases ***
At start there are no citations
    Go To Home Page
    Main Page Should Be Open
    Page Should Contain  citation app
    Page Should Contain  Create new citation
    Page Should Not Contain  Added citations:

Citation Gets Deleted
    Create First Book Citation
    Go To Home Page
    Main Page Should Be Open
    Page Should Contain  Matti Meikalainen. Testikirja. Testijulkaisija, 2024. ISBN 123-4567890123
    Select Checkbox  citation_id
    Click Button  deleteButton
    Handle Confirmation Popup
    Main Page Should Be Open
    Page Should Not Contain  Added citations:

Multiple Citations Get Deleted
    Create First Book Citation
    Create Second Book Citation
    Go To Home Page
    Main Page Should Be Open
    Page Should Contain  Matti Meikalainen. Testikirja. Testijulkaisija, 2024. ISBN 123-4567890123
    Page Should Contain  Matti Meikalainen2. Testikirja2. Testijulkaisija2, 2024. ISBN 123-4567890123
    Select All Checkboxes
    Click Button  deleteButton
    Handle Confirmation Popup
    Main Page Should Be Open
    Page Should Not Contain  Added citations:

*** Keywords ***
Reset Citations
    Reset Database

Create First Book Citation
    Create Book Citation  Testikirja  Matti Meikalainen  Testijulkaisija  123-4567890123  2024

Create Second Book Citation
    Create Book Citation  Testikirja2  Matti Meikalainen2  Testijulkaisija2  123-4567890123  2024

Handle Confirmation Popup
    ${alert}=  Handle Alert
    Log  Alert message: ${alert}

Select All Checkboxes
    ${checkboxes}=    Get WebElements    css:input[type='checkbox']
    FOR    ${checkbox}    IN    @{checkboxes}
        Select Checkbox   ${checkbox}
    END