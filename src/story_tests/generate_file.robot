*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Citations

*** Test Cases ***
List shows multiple citations
    Go To Home Page
    Create First Book Citation
    Create Second Book Citation
    Click Link  Get citations in BibTeX format
    Page Should Contain    @book
    Page Should Contain    title = {Testikirja},
    Page Should Contain    title = {Testikirja2},
    Page Should Contain    author = {Matti Meikalainen},
    Page Should Contain    author = {Teppo Teikalainen},
    Page Should Contain    year = {2024},
    Page Should Contain    year = {2025},
    Page Should Contain    isbn = {123-4567890123}
    Page Should Contain    isbn = {123-4567890124}

*** Keywords ***
Reset Citations
    Reset Database

Create First Book Citation
    Create Book Citation  Testikirja  Matti Meikalainen  Testijulkaisija  123-4567890123  2024

Create Second Book Citation
    Create Book Citation  Testikirja2  Teppo Teikalainen  Testijulkaisija2  123-4567890124  2025
