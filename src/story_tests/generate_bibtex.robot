*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Citations And Go To Home Page

*** Test Cases ***
List Shows BibTeX For All Citations
    Create Citations
    Go To Home Page
    Click Button  Get citations in BibTeX format
    Page Should Contain    @book
    Page Should Contain    title = {Testikirja},
    Page Should Contain    title = {Testikirja2},
    Page Should Contain    author = {Matti Meikalainen},
    Page Should Contain    author = {Teppo Teikalainen},
    Page Should Contain    year = {2024},
    Page Should Contain    year = {2025},
    Page Should Contain    isbn = {123-4567890123}
    Page Should Contain    isbn = {123-4567890124}

List Shows BibTeX For Only Filtered Citations
    Create Citations
    Go To Home Page
    Select Tag to Filter  maisteri
    Select Filtering Method  Match all
    Click Button  Apply filters
    Click Button  Get citations in BibTeX format
    Page Should Contain    title = {Testikirja},
    Page Should Not Contain    title = {Testikirja2},


*** Variables ***
@{TAGS1}  kandi  maisteri  luettu
@{TAGS2}  kandi  ei luettu

*** Keywords ***
Create Citations
    Create Book Citation  Testikirja  Matti Meikalainen  Testijulkaisija  123-4567890123  2024  ${TAGS1}
    Create Book Citation  Testikirja2  Teppo Teikalainen  Testijulkaisija2  123-4567890124  2025  ${TAGS2}