*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Citations And Make Citation

*** Test Cases ***
Edit Citation Successfully
    Go To Home Page
    Main Page Should Be Open
    Page Should Contain  Matti Muokkaaja. Muokkauskirja. Muokkausjulkaisija, 2023. ISBN 987-6543210987
    Click Link  Edit
    Edit Citation Page Should Be Open
    Set Book Citation Fields  Muokattu Kirja  Muokattu Muokkaaja  Muokattu Julkaisija  111-2223334445  2022
    Click Button  Edit
    Main Page Should Be Open
    Page Should Contain  Muokattu Muokkaaja. Muokattu Kirja. Muokattu Julkaisija, 2022. ISBN 111-2223334445

Edit Citation With Empty Title
    Go To Home Page
    Main Page Should Be Open
    Page Should Contain  Matti Muokkaaja. Muokkauskirja. Muokkausjulkaisija, 2023. ISBN 987-6543210987
    Click Link  Edit
    Edit Citation Page Should Be Open
    Input Text  id=title  ${EMPTY}
    Click Button  Edit
    Edit Citation Page Should Be Open
    Page Should Contain  Title cannot be empty and the lenght must be less than 75 characters

Edit Citation With Invalid Year
    Go To Home Page
    Main Page Should Be Open
    Page Should Contain  Matti Muokkaaja. Muokkauskirja. Muokkausjulkaisija, 2023. ISBN 987-6543210987
    Click Link  Edit
    Edit Citation Page Should Be Open
    Input Text  id=year  9999
    Click Button  Edit
    Edit Citation Page Should Be Open

*** Keywords ***
Reset Citations And Make Citation
    Reset Database
    Create Book Citation  Muokkauskirja  Matti Muokkaaja  Muokkausjulkaisija  987-6543210987  2023

Edit Citation Page Should Be Open
    Page Should Contain  Edit citation

Set Book Citation Fields
    [Arguments]  ${title}  ${author}  ${publisher}  ${isbn}  ${year}
    Input Text  title  ${title}
    Input Text  author  ${author}
    Input Text  publisher  ${publisher}
    Input Text  isbn  ${isbn}
    Input Text  year  ${year}