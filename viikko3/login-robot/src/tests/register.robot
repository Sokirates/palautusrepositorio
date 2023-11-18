***Settings***
Resource  resource.robot
Test Setup  Create User And Input New Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallee  kalle1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password 
    Input Credentials  kalle  kalle123
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  username already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  toimiva123
    Output Should Contain  Username should be at least 3 letters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  12345  password123
    Output Should Contain  Username should contain only lowercase letters

Register With Valid Username And Too Short Password
    Input Credentials  kayttaja  aa
    Output Should Contain  Password should be at least 8 letters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kaapo  vaarasalasana
    Output Should Contain  Password should not contain only letters

*** Keywords ***
Create User And Input New Command
    Input New Command