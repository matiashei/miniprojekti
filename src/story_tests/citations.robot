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

List shows a single added citation
    Create First Book Citation
    Go To Home Page
    Main Page Should Be Open
    Page Should Contain  Matti Meikalainen. Testikirja. Testijulkaisija, 2024. ISBN 123-4567890123

List shows multiple citations
    Create First Book Citation
    Create Second Book Citation
    Go To Home Page
    Main Page Should Be Open
    Page Should Contain  Matti Meikalainen. Testikirja. Testijulkaisija, 2024. ISBN 123-4567890123
    Page Should Contain  Teppo Teikalainen. Testikirja2. Testijulkaisija2, 2025. ISBN 123-4567890124

*** Keywords ***
Reset Citations
    Reset Database

Create First Book Citation
    Create Book Citation  Testikirja  Matti Meikalainen  Testijulkaisija  123-4567890123  2024

Create Second Book Citation
    Create Book Citation  Testikirja2  Teppo Teikalainen  Testijulkaisija2  123-4567890124  2025
