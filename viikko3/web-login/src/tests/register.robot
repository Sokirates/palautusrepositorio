*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Registeration Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  matias
    Set Password  matias123
    Set Password Confirmation  matias123
    Submit Registeration Credentials
    Registeration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  as
    Set Password  matias123
    Set Password Confirmation  matias123
    Submit Registeration Credentials
    Registeration Should Fail With Message  Username should be at least 3 letters long


Register With Valid Username And Invalid Password
    Set Username  matiass
    Set Password  wrong
    Set Password Confirmation  wrong
    Submit Registeration Credentials
    Registeration Should Fail With Message  Invalid password


Register With Nonmatching Password And Password Confirmation
    Set Username  matiasss
    Set Password  matias123
    Set Password Confirmation  matias1234
    Submit Registeration Credentials
    Registeration Should Fail With Message  Password and password confirmation didn't match

Login After Succesful Registeration
    Set Username  hiiis
    Set Password  hiiis123
    Set Password Confirmation  hiiis123
    Submit Registeration Credentials

    Go To Login Page
    Set Username  hiiis
    Set Password  hiiis123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registeration
    Set Username  a
    Set Password  moiiiii8
    Set Password Confirmation  moiiiii8
    Submit Registeration Credentials

    Go To Login Page
    Set Username  a
    Set Password  moiiiii8
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

** Keywords ***
Registeration Should Succeed
    Welcome Page Should Be Open

Registeration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message  
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Registeration Credentials
    Click Button  Register

